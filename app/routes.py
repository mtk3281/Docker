from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/jenkins_working')
def jenkins_working():
    return render_template('jenkins_working.html', title='How Does Jenkins Work?')

@app.route('/jenkins_uses')
def jenkins_uses():
    return render_template('jenkins_uses.html', title='Uses of Jenkins')

@app.route('/jenkins_architecture')
def jenkins_architecture():
    return render_template('jenkins_architecture.html', title='Jenkins Architecture')

@app.route('/jenkins_pipeline')
def jenkins_pipeline():
    return render_template('jenkins_pipeline.html', title='Pipeline Working')