from flask import Blueprint
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "The Main Endpoint"
