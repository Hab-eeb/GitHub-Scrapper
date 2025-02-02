from flask import render_template, jsonify, request, abort, make_response
from app import app
from .scrapper import scrapper

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrapper/<string:username>', methods=['GET'])
def scrape(username):
    if username == '':
        abort(400)

    data = scrapper(username)
    
    return jsonify(data)