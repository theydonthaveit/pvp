from flask import Flask, render_template, send_from_directory, url_for, request, redirect, flash, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.secret_key = 'xxxxx'
CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'fine'
    return jsonify({'dude':'You are in the safe zone'})


# @app.route('/riot')
# def riot():
#     return send_from_directory(app.static_folder, 'riot.txt')


# @app.route('/build_gamer_profile/<int:user_id>', methods=['GET', 'POST'])
# def buildGamerProfile(user_id):
#     if request.method == 'POST':
#         data = request.get_json()
#         profile = ProfileBuilderService()
#         pbp = profile.build_profile(data, user_id)
#         return pbp
#     else:
#         return 'You need to submit profile related things via POST'


if __name__ == '__main__':
    app.run(
        debug=True,
        use_reloader=True
    )