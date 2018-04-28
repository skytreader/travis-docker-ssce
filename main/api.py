import json
import pytz
import flask

from datetime import datetime

from main import main, db
from flask import Blueprint, request
from flask.ext.login import login_required
from models import get_or_create
from sqlalchemy.exc import IntegrityError

import re
import traceback

main_api = Blueprint("main_api", __name__)


@main_api.route("/api/util/servertime")
def servertime():
    return flask.jsonify({"now": str(datetime.now(tz=pytz.utc).isoformat())})
