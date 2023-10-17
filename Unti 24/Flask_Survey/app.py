from flask import Flask, request, render_template, redirect, flash, session
#from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'topsecret'
#toolbar = DebugToolbarExtension(app)


SURVEY_RESPONSES = "responses"

#Responses = []

@app.route("/")
def show_survey():
    """Shows surveys to select"""
    return render_template("begin_survey.html", survey=survey)

@app.route("/begin", methods=["POST"])
def begin_survey():
    """Clear survery responses"""
    session[SURVEY_RESPONSES]= []

    return redirect("/questions/0")

@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and move to next question"""

    choice = request.form['answer']

    responses = session[SURVEY_RESPONSES]
    responses.append(choice)
    session[SURVEY_RESPONSES] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def show_question(qid):
    """Shows current question>"""
    responses = session.get(SURVEY_RESPONSES)

    if (responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")

    if (len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template("questions.html", question_num=qid, question=question)

@app.route("/complete")
def complete():
    """Survey completed, shows completion page"""

    return render_template("completion.html")
    




