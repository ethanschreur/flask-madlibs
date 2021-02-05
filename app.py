from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def prompts():
    return (render_template('app.html', blanks = story.prompts))

@app.route('/story')
def to_story():
    answers = story.generate(request.args)
    return render_template('story.html', story = answers)