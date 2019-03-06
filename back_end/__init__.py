from flask import Flask

from back_end.Catalog.Main import main
from back_end.Catalog.Cards import cards
from back_end.Catalog.Card import card

# some comment

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(main, url_prefix='/api')
app.register_blueprint(cards, url_prefix='/api/cards')
app.register_blueprint(card, url_prefix='/api/card')
