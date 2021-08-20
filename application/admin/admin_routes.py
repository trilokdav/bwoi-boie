from flask import Blueprint, render_template, flash, session, Flask

admin = Blueprint('admin', __name__, template_folder='../assets/templates/admin', static_folder='../assets/static')

from app import mysql


@admin.route('/')
def test():
    return "<h1>hello</h1>"
