from flask import Flask, request, redirect, url_for, flash, session, send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Admin' and password == '12341234':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    return send_from_directory('static', 'login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_from_directory('templates', 'Homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
