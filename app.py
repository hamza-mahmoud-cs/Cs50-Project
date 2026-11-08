from flask import Flask, session, flash, render_template, request, redirect, url_for, jsonify
from helpers import apology, login_required, usd
from google import genai
from google.genai import types
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'
db = sqlite3.connect("project.db", check_same_thread=False)
db.row_factory = sqlite3.Row
app.jinja_env.filters["usd"] = usd
client = genai.Client(api_key=os.environ.get("GEMENI_API_KEY", "AQ.Ab8RN6LLjo4PJK3Xmjw7yz8jpcOkBKWsjXSHbdz3iZhcCQCaxw"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form.get("page") == "patient":
            return redirect("/patient")
        elif request.form.get("page") == "pharmacy":
            return render_template("main.html")
        elif request.form.get("account") == "register":
            return redirect("/register")
        else:
            return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        #make the register.html
        return render_template("register.html")
    else:
        # save the pharmacy in the data base
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        addres = request.form.get("addres")
        phone = request.form.get("phone")
        workHours = request.form.get("working hours")

        if not password:
            return apology("you should enter a password")

        elif not addres:
            return apology("you should enter an addres")

        elif not workHours:
            return apology("you should enter a work hours")

        elif not name:
            return apology("you should enter a pharmacy name")

        elif not username:
            return apology("you should enter a username")

        elif not phone:
            return apology("you should enter a phone number")

        elif db.execute("SELECT * FROM pharmacies WHERE phone = ?", (phone,)).fetchall():
            return apology("phone number already used")
        elif db.execute("SELECT * FROM pharmacies WHERE username= ?", (username,)).fetchall():
            return apology("user name already exists")
        db.execute("INSERT INTO pharmacies (phone, work_hours, username,address, name, password) VALUES (?, ?, ?, ?, ?, ?)", (phone, workHours, username, addres, name, password))
        db.commit()
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        if "user_id" in session:
            return redirect("/pharmacy")
        return render_template("login.html")
    else:
        #check for t basehe name and password in the data
        #then make the pharmacy ui
        username = request.form.get("username")
        password = request.form.get("password")
        if not db.execute("SELECT * FROM pharmacies WHERE username = ?", (username,)).fetchall():
            return apology("username not in the data base")
        elif password != db.execute("SELECT password FROM pharmacies WHERE username = ?", (username,)).fetchone()["password"]:
            return apology("wrong password")
        else:
            session["user_id"] = db.execute("SELECT id FROM pharmacies WHERE username = ?", (username,)).fetchone()["id"]
            return redirect("/pharmacy")

@app.route("/logout")
@login_required
def log_out():
    session.clear()
    return redirect("/pharmacy")

@app.route("/pharmacy", methods=["GET", "POST"])
@login_required
def pharmacy():
    if request.method == "GET":
        data = db.execute("SELECT price, medicines.name as name, description, parcode, medicine_id, available FROM pharmacies JOIN medicine_available ON pharmacy_id = pharmacies.id JOIN medicines ON medicine_id = medicines.id WHERE pharmacies.id = ?;", (session["user_id"],)).fetchall()
    else:
        db.execute("UPDATE medicine_available SET available = 1 - available WHERE pharmacy_id = ? AND medicine_id = ?", (session["user_id"], request.form.get('availability')))
        db.commit()
        data = db.execute("SELECT price, medicines.name as name, description, parcode, medicine_id, available FROM pharmacies JOIN medicine_available ON pharmacy_id = pharmacies.id JOIN medicines ON medicine_id = medicines.id WHERE pharmacies.id = ?;", (session["user_id"],)).fetchall()
    return render_template("pharmacy.html", data=data)

@app.route("/add_medicine", methods=["GET", "POST"])
@login_required
def add_medicine():
    if request.method == "GET":
        return render_template("add_medicine.html")
    else:
        name = request.form.get("medicine name")
        price = request.form.get("price")
        description = request.form.get("description")
        parcode = request.form.get("parcode")
        if not name:
            return apology("you have to enter a name")
        elif not price:
            return apology("you have to enter a price")
        elif not description:
            return apology("you have to enter a description")
        elif not parcode:
            return apology("you have to enter a parcode")
        
        try:
            price = float(price)
        except TypeError:
            return apology("price should be a number")
        if not db.execute("SELECT id FROM medicines WHERE parcode = ?", (parcode, )).fetchall():
           db.execute("INSERT INTO medicines (name, parcode, description) VALUES (?, ?, ?)", (name, parcode, description))
        
        medicine_id = db.execute("SELECT id FROM medicines WHERE parcode = ?", (parcode, )).fetchone()["id"]

        if db.execute("SELECT * FROM medicine_available WHERE pharmacy_id = ? AND medicine_id = ?", (session["user_id"], medicine_id)).fetchone():
            return apology("the medicine already exist in the pharmacy")

        db.execute("INSERT INTO medicine_available (price, pharmacy_id, medicine_id) VALUES(?, ?, ?)", (price, session["user_id"], medicine_id))
        db.commit()
        flash('medicine added successfully', 'success')
        return redirect("/add_medicine")

@app.route("/patient")
def patient():
    data = db.execute("SELECT phone, work_hours, address, pharmacies.name as pharmacy_name, medicines.name as medicine_name, parcode, description, price FROM pharmacies JOIN medicine_available ON pharmacy_id = pharmacies.id JOIN medicines ON medicine_id = medicines.id WHERE available = 1").fetchall()
    return render_template("patient.html", data=data)

@app.route("/ai", methods=["GET", "POST"])
def ai():
    if request.method == 'GET':
        return render_template("ai.html")
    else:
        data = request.get_json()
        user_message = data.get('message', '')        
        SYSTEM_PROMPT = "you are a kind ai helpers helps patients to find the medicine they need in my website and you should always remind patients to ask a doctor"

        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents= user_message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7
            )
        )
        return jsonify({'reply': response.text})