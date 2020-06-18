from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField
from random import  *
import string
from flask_navigation import Navigation
import re

value = string.ascii_letters + string.punctuation + string.digits + string.ascii_lowercase + string.ascii_uppercase

EXPLAIN_TEMPLATE_LOADING=False
print(EXPLAIN_TEMPLATE_LOADING)


DEBUG = True
app = Flask(__name__)
app = Flask(__name__, template_folder='./templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    website = TextField('website:', validators=[validators.data_required()])
    username = TextField('username:', validators=[validators.data_required()])
    pwlen = IntegerField('pwlen:', validators=[validators.data_required()])

##############################################################################

@app.route('/')
def home():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        return render_template('index.html', form=form)
    return render_template('home.html')



@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        return render_template("index.html")
    return render_template('index.html')

###############################################################################

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = ReusableForm(request.form)


    if request.method == 'POST':
        website=request.form['website']
        username=request.form['username']
        email=request.form['email']
        pwlen=request.form['pwlen']
        res = int(pwlen)
        y = "".join(choice(value) for x in range(res))
        file = open('ReqInfo.log', 'a+')
        file.write("Website: " + website + ' | ' "Username: " + username + ' | ' "Email: " + email + ' | ' "Password: " + y + "\r\n")
        file.close

    if form.validate():
            flash('Your password for {}, with username: {}, has the following password - {}'.format(website, username, y ))

    elif():
            flash('Error: All Fields are Required')

    return render_template('create.html', form=form)


############################################################################


@app.route("/recover", methods=['GET', 'POST'])
def recover():

    form = ReusableForm(request.form)

    if request.method == 'POST':
        website=request.form['website']
        username=request.form['username']
        email=request.form['email']

        search = website, username, email
        print(search)

        tomatch = ('Website: ' + website + ' | Username: ' + username + ' | Email: ' + email)

        with open('ReqInfo.log', 'r') as file:
            for line in file.readlines():
                line = line.strip()
                for word in search:
                    if tomatch in line:
                        print(line)
                        flash(line)
                        break
                    elif():
                        print('No Value')

    if form.validate():
            flash('{}'.format(line))


    elif():
            flash('Error: All Fields are Required, {}'.format(line))

    return render_template('recover.html', form=form)

#####################################################################################



if __name__ == "__main__":
    app.run()

# def findPW():
#file = open('ReqInfo.log', 'r')
#f1 =file.readlines()
#tomatch = website + email + username
#with open('ReqInfo.log', r) as file:
#for line in file:
#if username and website and email in line:
#tomatch = line
#print(tomatch)
