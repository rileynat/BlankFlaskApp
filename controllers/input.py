
from flask import *

main = Blueprint('input', __name__, template_folder='views')

@main.route('/input')
def main_route():
    return render_template("input.html")