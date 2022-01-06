from flask import Blueprint


bp = Blueprint('healthz', __name__, url_prefix='/')

@bp.route("/healthz")
def healthz():
    return {"status": "Happy"}, 200
