from flask import Flask, redirect, url_for, render_template, request, session, flash
from chatterbot import ChatBot, comparisons, response_selection
from chatterbot.trainers import ChatterBotCorpusTrainer
from medbot import joke, fact, checkDisease, getDisease, getAnswer, saveUnknown, checkSymptoms
import random
from datetime import timedelta
import json
import string
from flask_sqlalchemy import SQLAlchemy

import en_core_web_sm
nlp = en_core_web_sm.load()

app = Flask(__name__)
app.secret_key = "proest"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medbot_users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

chatbot = ChatBot(
    'MedBot - Beta 1.0',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
     preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": comparisons.JaccardSimilarity,
            "response_selection_method": response_selection.get_first_response,
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///medbot_15_database.sqlite3?check_same_thread=False'
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.medbot'
)

with open("diseases.json", encoding="utf-8") as file:
    data = json.load(file)

class users (db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(30))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


@app.route("/login", methods = ["POST", "GET"])
def login():
    if "email" in session:
        return redirect(url_for("medbot"))
    else:
        if request.method == "POST":
            if request.form["email"]:
                if request.form["password"]:
                    find_em = request.form["email"]
                    find_ps = request.form["password"]
                    
                    found_user = users.query.filter_by(email = find_em).first()

                    if found_user:
                        if found_user.password == find_ps:
                            session["email"] = find_em
                            return redirect(url_for("medbot"))
                        else:
                            flash("Wrong Password.", "error")
                            session.pop("user", None)
                            return redirect(url_for("login"))
                    else:
                        flash("User not found.", "error")
                        session.pop("user", None)
                        return redirect(url_for("login"))
                else:
                    flash("Password missing.", "error")
                    session.pop("user", None)
                    return redirect(url_for("login"))
            else:
                temp_user = users("Anonymous", "User", "Anonymous", "1234")
                session["email"] = temp_user.email
                return redirect(url_for("medbot"))
        else:
            return render_template("welcome.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if "email" in session:
        user = session["email"]
        return render_template("medbot.html", usr = user)
    else:
        if request.method == "GET":
            return render_template("register.html")
        else:
            first_name = request.form['f_name']
            last_name = request.form['l_name']
            email = request.form['email']
            password = request.form['password']

            found_user = users.query.filter_by(email = email).first()

            if found_user:
                flash("Email already in use.", "error")
                return redirect(url_for("login"))
            
            else:
                usr = users(first_name, last_name, email, password)

                db.session.add(usr)
                db.session.commit()

                flash("Register Successful.", "info")

                return redirect(url_for("login"))

@app.route("/medbot", methods = ["POST", "GET"])
def medbot():
    if "email" in session:
        email = session["email"]
        if request.method == "POST":
            session.pop("email", None)
            return redirect(url_for("login"))
        else:
            if email != "Anonymous":
                found_user = users.query.filter_by(email = email).first()
                first_name = found_user.first_name
                return render_template("medbot.html", usr = first_name)
            else:
                return render_template("medbot.html", usr = "Anonymous")
    else:
        flash("You must log in, first.", "warning")
        return redirect(url_for("login"))

@app.route("/diseases",  methods = ["GET", "POST"])
def diseases():
    if "email" in session:
        if request.method == "POST":
            session.pop("email", None)
            return redirect(url_for("welcome"))
        else:
            return render_template("diseases.html", dis = data, number = len(data))
    else:
        flash("You must log in, first.", "warning")
        return redirect(url_for("login"))

@app.route("/profile",  methods = ["GET", "POST"])
def profile():
    if "email" in session:
        if request.method == "POST":
            session.pop("email", None)
            return redirect(url_for("medbot"))
        else:
            email = session["email"]
            if email != "Anonymous":
                found_user = users.query.filter_by(email = email).first()

                f_name = found_user.first_name
                l_name = found_user.last_name

                words = []

                try:
                    with open("./files/%s_search_list.txt"%(email), "r") as file:
                        for line in file:
                            words.append(line)
                except (FileNotFoundError):
                    pass
                
                words = set(words)
                words = sorted(words)
                
                return render_template("profile.html", fm = f_name, lm = l_name, em = email, us = words)
            else:
                words = ["You", "Have", "No", "Power", "Here", ":D"]
                return render_template("profile.html", fm = "Anonymous", lm = "User", em = "Anonymous", us = words)
    else:
        flash("You must log in, first.", "warning")
        return redirect(url_for("login"))

@app.route("/extras",  methods = ["GET", "POST"])
def extras():
    if "email" in session:
        if request.method == "POST":
            session.pop("email", None)
            return redirect(url_for("medbot"))
        else:
            email = session["email"]
            if email != "Anonymous":
                found_user = users.query.filter_by(email = email).first()

                f_name = found_user.first_name
                
                return render_template("extras.html", fm = f_name)
            else:
                return render_template("extras.html", fm = "Anonymous")
    else:
        return redirect(url_for("medbot"))

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    if "email" in session:
        email = session["email"]

    if checkDisease(user_input): # Verify is disease exists in input
        disease = getDisease(user_input) # Gets the disease

        if disease != None:
            session["previous_disease"] = disease
        else:
            disease = session["previous_disease"]

        with open("./files/%s_search_list.txt"%(email), "a") as file:
                file.write(disease + "\n")

        return(getAnswer(user_input, disease)) # Gets the proper answer based on the disease and input

    elif checkSymptoms(user_input):
        return(checkSymptoms(user_input))

    else:
        if (fact(user_input) != None):
            return(str(fact(user_input)))

        elif (joke(user_input) != None):
            return(str(joke(user_input)))

        elif "how many diseases" in user_input.lower():
            return("I know " + str(len(data)) + " diseases.") # Returns the number of diseases in .json file

        elif "random disease" in user_input.lower():
            return("Here's one: " + random.choice(list(data.keys()))  + "!") # Returns a random disease

        else:
            answer = chatbot.get_response(user_input)
            if str(answer) == "I am sorry, but I do not understand.": # Bot doesn't know how to answer
                message = session["email"] + " | " + user_input
                saveUnknown(message) # Saves user name + input to .txt file
                return(str(answer))
            else:
                return(str(answer)) # Returns bot answer based on .yml files 

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
