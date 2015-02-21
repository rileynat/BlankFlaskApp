
from flask import *

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def main_route():
    return render_template("index.html")

@main.route('/input')
def input():
    return render_template("input.html")

@main.route('/guess')
def guess():
	puzzle = getPuzzle()
	return render_template("guess.html")