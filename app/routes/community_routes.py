from flask import Blueprint, render_template, request,session,redirect,jsonify,url_for
from sqlalchemy import asc,alias,func

from ..models.pipeline import CommunityPost,Album,Photo,db
community = Blueprint('community', __name__)


batch_limit = 9 #9 per batch is ideal since the community page will generate 3x3 grids at a time
page_num = 1 #start at one for the page number then increment on each request
total_limit = 45

#just to test infinite scrolling
def generate_data():
    global page_num
    
    ## offset to increment the query for the posts
    offset = (page_num-1) * batch_limit
    page_num+=1
    community_data = session.get('community_data')

    #check for problematic comunity data
    if community_data is None:
        print('problematic')
        return
    

    ##Query to get just the post content, date, and photo_data
    ##TODO add likes and comments to the post
    temp = (db.session.query(
        CommunityPost.post_content,
        CommunityPost.community_post_id,
        Photo.photo_data
    )
    .join(Album, CommunityPost.album_id == Album.album_id)
    .join(Photo, Album.album_id == Photo.album_id)
    .order_by(asc(CommunityPost.post_date))
    .offset(offset).limit(batch_limit)
    .all()
    )
    
    #convert to a list of tuples that have objects in them kinda like [(CommunityPost(),Photo()),...]
    processed_temp = [tuple(row) for row in temp if not(row is None)]


    #add the batch of posts to the total amount of posts the user has generated
    #set operation for lazy data integrity may unsort the list
    community_data.extend(list(set(processed_temp))) 
    #IMPORTANT update the session data
    session['community_data'] = community_data

    #return the batch when ONLY when below the limit
    return processed_temp

    

@community.route('/community') 
def community_page():


    username = session.get('username')
    community_data = session.get('community_data')

        
    #handles if the user has clicked off the page and decided to return before the limit
    if username in session.values() and len(community_data) < total_limit:
        generate_data()
        return render_template('community.html', community_data = community_data)
    
    #if the user returns to the page just serve them back the posts that they generated
    elif username in session.values() and len(community_data) >= total_limit:
        
        full_set = list(set(community_data))
        print(full_set)
        return  render_template('community.html', community_data=full_set)
    else:
        return redirect('/')


#Send data to the webpage
@community.route('/get_data')
def more_posts():

    username = session.get('username')
    community_data = session.get('community_data')

    if username not in session.values():
        return redirect('/')
    
    #if the user hit the psot limit then yell at the javascript on the page 
    if len(community_data) >= total_limit:
        print('works')
        return 'STOP'
    else:
        temp = generate_data()
        return  jsonify ({'html': render_template('community_posts_batch.html', temp=temp)})
    


#Get a single instance of a community post
#TODO link likes and comments to the community post and add design elements
@community.route('/community_post/<int:community_post_id>',methods=['POST','GET'])
def community_post_(community_post_id):
    print('works')
    post = (db.session.query(
        CommunityPost.post_content,
        CommunityPost.album_id,
        Photo.photo_data
    )
    .join(Album, CommunityPost.album_id == Album.album_id)
    .join(Photo, Album.album_id == Photo.album_id)
    .filter(CommunityPost.community_post_id == community_post_id)
    .first()
    )

    
    return render_template('community_singleton.html',
                           community_post_id=community_post_id,
                           post_content=post[0],
                           album_id=post[1],
                           photo_data=post[2])

