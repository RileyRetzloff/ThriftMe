from flask import Blueprint, render_template, request, redirect, url_for
import random

community = Blueprint('community', __name__)

@community.route('/community')
def community_page():


    """
    TODO
    Fix template elemetns so that the webpage should 
    """

    """
    community page must always be a multiple of 3 
    to get the correct "grid" effect
    """
    num_pages = random.randint(1,6) * 3 
    

    
    return render_template('community.html', num_pages=num_pages)