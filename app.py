import pyrebase
from flask import *
app = Flask(__name__)

config = {
    "apiKey": "AIzaSyA3gD0IpCTJ6ffDKAuli8tWN9n1z4Up5cE",
    "authDomain": "test-3586b.firebaseapp.com",
    "databaseURL": "https://test-3586b.firebaseio.com",
    "projectId": "test-3586b",
    "storageBucket": "test-3586b.appspot.com",
    "messagingSenderId": "651421238353",
    "appId": "1:651421238353:web:5a564422937d406e906470",
    "measurementId": "G-28T2QZQ6L6"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/',methods = ['GET','POST'])
def basic():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        try:
            auth.sign_in_with_email_and_password(email,password)
            return render_template('after_login.html')
        except:
            return 'check your credentials'

    return render_template('main_page.html')

if __name__ == '__main__':
    app.run()
