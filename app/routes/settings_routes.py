from flask import Blueprint, render_template, request, redirect, url_for

# Create Blueprint
settings = Blueprint('settings', __name__)


#SETTINGS PAGE
@settings.route('/settings')
def render_settings():
    return render_template('settings.html')
