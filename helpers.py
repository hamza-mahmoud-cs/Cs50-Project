from flask import Flask, session, flash, render_template, request, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def usd(value):
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return value

def apology(message):
    return render_template("error.html", message=message)
