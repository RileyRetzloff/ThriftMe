from flask import Blueprint, render_template, request, redirect, url_for

sell = Blueprint('sell', __name__)

@sell.route('/sell')
def create_listing():
    return render_template('sell.html')