from flask import Blueprint
from sqlalchemy import select
from .infrastructure.db import connection


bp = Blueprint('general', __name__, url_prefix='/')


@bp.route("/healthz")
def healthz():
    try:
        connection.get_db().execute(select([1]))
    except Exception as e:
        print(e)
        return {"status": "DB is dead"}, 500
    return {"status": "Happy"}, 200
