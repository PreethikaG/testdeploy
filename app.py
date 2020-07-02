import os
from os import environ
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


# Create an instance of Flask
app = Flask(__name__)

# Setup SQLAlchemy with flask
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)
# Create engine
conn_str = "postgres://yilylfzrtybpfj:0f41aebf672658b13fe423d08212077ec97d182109280f4fa13f256e3964c7bb@ec2-54-159-138-67.compute-1.amazonaws.com:5432/d84qcd7siep7il"
engine = create_engine(conn_str)
# Reflect the database 
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Return template and data
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
