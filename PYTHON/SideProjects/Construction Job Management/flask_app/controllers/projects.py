from crypt import methods
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.project import Project

@app.route('/projects/dash')

@app.route('/projects/<int:id>')

@app.route('/projects/edit/<int:id>')

@app.route('/projects/edit/commit', methods=('POST'))