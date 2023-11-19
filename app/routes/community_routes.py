from flask import Blueprint, render_template, request, redirect, url_for

community = Blueprint('community', __name__)

@community.route('/community')
def community_page():
    return render_template('community.html')