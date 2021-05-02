from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autocomplete(db.Model):
    __tablename__ = 'gene_autocomplete'

    species = db.Column(db.String(255), primary_key=True)
    stable_id = db.Column(db.String(128), nullable=False, primary_key=True)
    display_label = db.Column(db.String(128), primary_key=True)
    location = db.Column(db.String(60))
