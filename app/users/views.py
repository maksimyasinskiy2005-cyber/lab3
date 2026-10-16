from flask import Blueprint, render_template, request, redirect, url_for

user_bp = Blueprint('users', __name__, template_folder='templates')

@user_bp.route("/hi/<string:name>")
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, type=int)
    return render_template("users/hi.html", name=name, age=age)

@user_bp.route("/admin")
def admin():
    to_url = url_for("users.greetings", name="administrator", age=45, _external=True)
    return redirect(to_url)
