from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user_list.html')

@app.route('/user_list')
def user_list():
    return render_template('user_list.html')

@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route('/user_roles')
def user_roles():
    return render_template('user_roles.html')

@app.route('/room_list')
def room_list():
    return render_template('room_list.html')

@app.route('/add_room')
def add_room():
    return render_template('add_room.html')

@app.route('/allocate_room')
def allocate_room():
    return render_template('allocate_room.html')

@app.route('/room_statistics')
def room_statistics():
    return render_template('room_statistics.html')

if __name__ == '__main__':
    app.run(debug=True)
