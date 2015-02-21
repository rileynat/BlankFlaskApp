
from flask import *
from firebase_wrapper import getPuzzle

main = Blueprint('main', __name__, template_folder='views')

@main.route('/guess')
def main_route():
	puzzle = getPuzzle()
	return render_template("guess.html")