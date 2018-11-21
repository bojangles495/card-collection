from flask import Blueprint
import requests

cards = Blueprint('cards', __name__)

@cards.route('/')
def index():
    return "The Cards Endpoint"
