from flask import Flask, jsonify



app = Flask(__name__, static_folder='static', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/', methods=['GET'])
def hello():
    return app.send_static_file('index.html')

@app.route('/gello', methods=['GET'])
def gello():
    resp = jsonify({'data': 'gello'})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/hiii', methods=['GET'])
def hiii():
    resp = jsonify({'data': 'hi'})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp



if __name__ == '__main__':
    app.run()