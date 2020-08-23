
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, json
app = Flask(__name__)


# @app.route('/')
# def home_page():
#     return render_template("main.html")

@app.route('/', methods=['GET', 'POST'])
def login_page():
    #error = ' '

# try:

    if request.method == "POST":
        attempted_username = request.form['Username']
        attempted_password = request.form['Password']
        attempted_email = request.form['Email']
        
        d = {}
        with open('data.json', 'r') as outfile:  
            json.load(d, outfile)
            
            d['user']=attempted_username
            d['pass']=attempted_password
            d['email']=attempted_email

        if request.form['Username'] == d['user'] and request.form['Password'] == d['pass'] and request.form['Email'] == d['email']:
           #return 'SUCCESSFULLY LOGGEDIN'
                #error = 'Invalid Credentials. Please try again.'
            return render_template('bcd.html')
        else:
            return 'invalid '
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)




        