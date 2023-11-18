from app import app, db
from app.models import User, Message
from flask import request, redirect, render_template

@app.route('/register', methods=['POST'])
def register():
    data_username = request.form.get("username")
    data_password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if data_password != confirm_password:
        return "Passwords do not match.Please give your password!"

    existing_user = User.query.filter_by(username=data_username).first()
    if existing_user:
        return "Username already exists. Choose another one, please."

    new_user = User(username=data_username, password=data_password)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/all")

@app.route('/send', methods=['POST'])
def send_message():
    data_username = request.form.get("username")
    data_password = request.form.get("password")
    content = request.form.get("content")

    user = User.query.filter_by(username=data_username, password=data_password).first()
    if not user:
        return "Uncorrect username or password.Please, write again!"

    new_message = Message(content=content, user=user)
    db.session.add(new_message)
    db.session.commit()

    return redirect("/all")

@app.route('/all')
def get_all_messages():
    messages = Message.query.all()
    return render_template('all.html', messages=messages)
