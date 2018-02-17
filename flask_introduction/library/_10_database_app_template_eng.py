"""
Requirements:
 * A database created with some data about authors inside.
"""
import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.before_request
def before_request():
    print ("hello")
    g.db = connect_db()

@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/authors_template_engine.html', authors=authors)

@app.route('/extra')
def hello_world1():
    cursor = g.db.execute('SELECT id, name FROM country;')
    country = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/authors_template_engine.html', authors=country)
