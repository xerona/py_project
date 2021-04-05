import os
from flask import render_template, current_app, send_from_directory, Response, redirect, url_for, request, abort
from flask_login import login_required, login_user, logout_user
from app import app, db

from models.user import User


@app.route("/app/<path:path>")
@login_required
def b(path):
    return render_template("app.html", path=path)


@app.route("/static/js/<path:path>.js")
def static_js(path):
    return send_from_directory(
        os.path.join(current_app.root_path, "static", "js"), f"{path}.js"
    )


@app.route("/static/css/<path:path>.css")
def static_css(path):
    return send_from_directory(
        os.path.join(current_app.root_path, "static", "css"), f"{path}.css"
    )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, "static"), "favicon.ico"
    )



# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = db.session.query(User).filter(
                User.email == email,
                User.password == password
            ).one()
        except:
            return abort(401)
        login_user(user)
        return redirect(url_for("b", path="player"))
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=email>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
