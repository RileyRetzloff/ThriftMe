from flask import Blueprint, render_template, request, redirect, url_for

create_listing = Blueprint('create_listing', __name__)

create_listing.route('/create_listing')
def create_listing():
    return render_template('index.html')