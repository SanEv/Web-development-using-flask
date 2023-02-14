from flask import Flask, render_template, request,redirect,session
from db import Database
import api

app = Flask(__name__)
## Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


dbo = Database()
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html',message="Registration successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email, password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message="Incorrect email/password")

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')
@app.route('/Named Entity Recognition')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text=request.form.get('ner_text')
        response=api.ner(text)
        print(response)

        return render_template('ner.html',response=response)
    else:
        return redirect('/')

@app.route('/Sentiment Analysis')
def sa():
    if session:
        return render_template('sa.html')
    else:
        return redirect('/')


@app.route('/perform_sa',methods=['post'])
def perform_sa():
    if session:
        text=request.form.get('sa_text')
        response=api.sa(text)
        print(response)
        return render_template('sa.html', response=response)
    else:
        return redirect('/')


@app.route('/Abuse Detection')
def ad():
    if session:
        return render_template('abuse_detec.html')
    else:
        return redirect('/')

@app.route('/perform_abusedetec',methods=['post'])
def perform_ad():
    if session:
        text=request.form.get('abuse_text')
        response=api.abuse_detec(text)
        print(response)

        return render_template('abuse_detec.html',response=response)
    else:
        return redirect('/')



app.run(debug=True)
