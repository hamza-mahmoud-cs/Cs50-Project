# [your pharmacy]

#### Video Demo: <https://youtu.be/lVEZQBoy2DQ>

#### Description:
my porject is a web app that is designed to make it easier for the patients to know which pharmacy offers their medicines at which price and if it available or not

and lets the small pharmacies offers their medicines so anyone can know what are they offering.

I chose to build this project because I think it is a big problem that needs to be solved and I myself has suffered from it and because I have the ability to build so I chose to do it.

I used what I learnt in the course to build I used sqlite because I think it's enough to do the job and used flask because it is so useful and easy to handle and used javascript to staff dynamically like the live search and used bootstrap, css and html to adjust the appearance of my web app.

I have built a number of routes to make the big problem several small problems that I can handle I made a main page to let the user choose is he a pharmacy owner or a patient I used html to build the page and made the buttons and used flask and python to route the user to deffernt routes. 

the pharmacy route I used html again to build the buttons I made two choices register to make a new account and login so the user can login into his account and I used the session module in the flask framework so I can handle cookies and the user can login immediatly so he doesn't need to enter his informations each time and I made a login_required decorator function and used wraps wich was a new information I searched to know it.

the register route I used the methods parameter in the route decorator function in flask to let the user enter his information and to save in the database I used several if elif lines to handle any errors the user may do and used some query lines to make sure this user is uniqe.

the login function here I letted the user login into his account and if he is already logeed in he will be redirected to the pharmacy route.

the pharmacy route this is the main page for the pharmacies owners here the can add a midicine or set it to unavailable as they want and they can search a medicine by it's information parcode, name, price, or even the discription and used javascript to make this possible at first the data was already in the table by the sqlite queries and flask and also this was a new information I searched for because I didn't know what is a cursor and I didn't know that I should use fetchall function to to get a list of the rows and I didn't know that I need to use Row module to get the data by the name but eventually I did and everything worked but no I needed to learn how to do the search I used javascript to iterate into all the table body rows and if the row have the search in it I let it and if else I change it's display into none so it's not visible.

now for the patient route I used the same search technich in the pharmacy route but now I have to show the information about every medicine and every pharmacy and also I added an ai helpers that I used an ai api in it.

project.db the data base file I used here is three tables a table for the medicines so I don't need to save the same medicine several times and pharmacies table the table that has the data about each pharmacy and the medicine_available it's the table that makes many to many relation works and has two foreign keys each one related to a the primary key id in the other two tables.

#### Author Details:
* **Name:** Hamza Mahmoud
* **GitHub Username:** Hamza-electo
* **edx Username:** hamza1121
* **City:** Minya
* **Country:** Egypt

## File structure:
* app.py: the main code file of the programm that has in it all the routes and all the back end work.
* helpers.py : another code file that has in it three function one is a decorator and the other a configuration for jinja and the third is an error function that shows an error message to the user.
* the templates: the folder that has all the html files needed for the routes of the programm.
* index.html: a html file that works as the first page the user see when he inters the app.
* patient.html: user interface for the patients so they can search for their medicines or they can ask the ai helper.
    * ai.html: it works as the chat interface so the user can ask the ai helper.
* main.html: the page that the user will see if he chose to enter as a pharmacy owner he can shoose register or login.
    * register.html: here the user can enter his data to make a new account.
    * login.html: here the user can enter his data to login into his account.
* pharmacy.html: here the pharmacy owner can control over his account.
    * add_medicine.html: here the pharmacy owner can add a new medicine into his collection of medicines or change the availability of his medicines.
* error.html: the html file that used for the apology function in the helpers.py file.
* layout.html: here is the html pattern that all the html files use.
* static: the directory that has all the static staff in the web app.
    * js: directory that has all the java script files.
        * search_table.js: the code for the search of the patient and the pharmacy page.
        * chatbot.js: the code for the chat screen in the ai help page.
        * bootstrap.bundle.min.js: bootstrap file that I downloaded to use the bootstrap.
    * css: here all the css files I used
        * bootstrap.min.css: bootstrap file that I downloaded to use the bootstrap library in my code.
        * style.css: the file I wrote to adjust my web app.
* project.db: the data base of my web app.
* requirements.txt: a file that has all the libraries used in the code.

## Technologies Used:
* **Language:** Python / HTML / CSS / JAVASCRIPT
* **Framework:** Flask
* **Api:** genai
* **Database:** SQlite

## How to Run the Project
1. Clone or navigate to the project directory:
    ```bash
    cd My_project
2. Install the requirements:
    ```bash
    pip install -r requirements.txt
3. run flask:
    ```bash
    run flask