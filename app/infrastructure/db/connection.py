from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from flask import g, current_app, Flask
from flask.cli import with_appcontext
import click


def get_db() -> Connection:
    if "db" not in g:
        engine = create_engine("sqlite+pysqlite://{db_path}".format(db_path=current_app.config.get("DATABASE")))
        g.db = engine.connect()

    return g.db


def close_db(e=None) -> None:
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
