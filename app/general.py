from flask import Blueprint


bp = Blueprint('general', __name__, url_prefix='/')

@bp.route("/healthz")
def healthz():
    return {"status": "Happy"}, 200
