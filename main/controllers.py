from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import login_required, login_user, logout_user
from forms import LoginForm
from utils import route_exists

import config
import flask
import main

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("main.jinja")

@main_bp.route("/login/", methods=["GET", "POST"])
def login():
    from flask.ext.login import current_user
    from models import User
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.main_username.data,
          is_user_active=True).first()

        if user and user.password == form.main_password.data:
            login_user(user)
            next_url = flask.request.args.get("next")

            if next_url and not route_exists(next_url):
                return flask.abort(400)

            return redirect(next_url or url_for("main.dash"), code=302)
        else:
            flash("Wrong user credentials")
    elif not current_user.is_anonymous():
        return redirect(url_for("main.dash"))

    return render_template("login.jinja", form=form)

@main_bp.route("/dashboard")
@login_required
def dash():
    return ""
    
@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
