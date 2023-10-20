from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)

boggle_game = Boggle()

@app.route('/')
def homepage():
    """Reveal game board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    return render_template('index.html', board=board, highscore=highscore, nplays=nplays)

@app.route('/checkword')
def checkword():
    """Verify word is in dictionary"""

    word = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route('/post-score', methods=["POST"])
def post_score():
    """Gets the score and updates number of plays (nplays) and the high score when appropriate"""

    score = request.json['score']
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    session['nplay'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
