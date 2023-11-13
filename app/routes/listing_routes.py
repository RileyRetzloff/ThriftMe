from flask import Blueprint, render_template, request, redirect, url_for

listing = Blueprint('listing', __name__)

listing.route('/listing')
def listing():
    return render_template('listing.html')