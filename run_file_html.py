import os
from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from db_html_connect import ConnectHTMLSQL
import sqlite3

# initializing sqlite3 datatbase called ebooks
connection = sqlite3.connect('ebooks.db')
cursor = connection.cursor()
# Creating ebook table
# cursor.execute(""" CREATE TABLE ebooks (
#     id INTEGER,
#     title TEXT,
#     author TEXT,
#     genre TEXT,
#     image TEXT
# )
# """)
# connection.commit()
# connection.close()
# cursor.execute()

# Linking to ebooks db though SQLAlchemy
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:////{}".format(os.path.join(project_dir, "ebooks.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    author = db.Column(db.String(25))
    genre = db.Column(db.String(20))
    image = db.Column(db.String(20))


@app.route("/")
@app.route("/index")
def index():
    return render_template("home.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    # searchForm = searchForm()
    # courses = models.Course.query
    all_tables = ConnectHTMLSQL().create_all_tables()

    # if all_tables.validate_on_submit():
    #     names = all_tables.filter(all_tables.users.name.like('%' + all_tables.name.data + '%'))

    # names = all_tables #.order_by(all_tables.users.name).all()

    return render_template('search_form.html')

@app.route('/catalog')
def catalog():
    return render_template('ebook_catalog.html')


@app.route('/all_tables', methods=["GET", "POST"])
def home():
    all_tables = ConnectHTMLSQL().create_all_tables()
        # try:
        #     # all_tables.session.post()
        #     # all_tables.session.get()
        #     all_tables.session.add()
        #     all_tables.session.commit()
        # except Exception as e:
        #     print("Failed to add book")
        #     print(e)
        #     all_tables.query.all()
    return render_template("/home.html")




@app.route("/update", methods=["POST"])
def add():
    # try:
    #     all_tables.form.get()
    #     all_tables.form.get()
    #     all_tables.query.filter_by(title='').first()
    #     all_tables.session.commit()
    # except Exception as e:
    #     print("Couldn't update book title")
    #     print(e)
    return redirect("home.html")


# @app.route("/delete", methods=["POST"])
# def delete():
#     # all_tables.request.form.get()
#     # all_tables.query.filter_by(title='').first()
#     # all_tables.session.delete()
#     # all_tables.session.commit()
#     return redirect("home.html")


if __name__ == "__main__":
    app.run(debug=1, host='0.0.0.0')
