
--This is a script to test queries on and generate dummy data for the database
--The Thriftme script was getting too long


--generate some users to test the cascade
INSERT INTO users (username, password, email, profile_picture, public_access)
VALUES
    ('real_person', 'password1', 'user1@example.com', E'\\x89504e470d0a1a0a', true), -- Hexadecimal representation of a profile picture
    ('real_shopper', 'password2', 'user2@example.com', E'\\x89504e470d0a1a0a', true),
    ('real_person_community', 'password3', 'user3@example.com', E'\\x89504e470d0a1a0a', true);

select * from users;

INSERT INTO albums (user_id, album_name)
VALUES (1, 'Averys Post Album');


select * from albums;

INSERT INTO posts (user_id, post_content, album_id)
VALUES (1, 'This is the first users post!', 1);


select * from posts;

INSERT INTO photos (album_id, photo_data)
VALUES (1, E'\\x89504E470D0A1A0A0000000D49484452');

select * from photos;


INSERT INTO likes (user_id, post_id)
VALUES (2, 1);

-- User 3 likes the first user's post
INSERT INTO likes (user_id, post_id)
VALUES (3, 1);

select * from likes;

INSERT INTO comments (user_id, post_id, comment_content)
VALUES (2, 1, 'Great post!');

INSERT INTO comments (user_id, post_id, comment_content)
VALUES (3, 1, 'Awesome!');


--delete records because i messed up

delete from comments
where comment_id in(
select comment_id
from comments order by
comment_id desc
limit 2
);

--query to get comments from a post
select comment_content from comments
left join posts p on comments.post_id = p.post_id
where p.user_id != comment_id;

-- query to get a generic post with its content
select count(l.user_id), post_content,photo_data from posts
inner join likes l on posts.post_id = l.post_id
inner join photos p on posts.album_id = p.album_id
where posts.user_id = :user_id
group by post_content, photo_data, posts.album_id;

--query to get a single post, a caption, and its photo content
SELECT
    COUNT(l.user_id) AS like_count,
    posts.post_content,
    photo_data
FROM
    posts
INNER JOIN
    likes l ON posts.post_id = l.post_id
INNER JOIN
    photos p ON posts.album_id = p.album_id
WHERE
    posts.user_id = :user_id
GROUP BY
    posts.post_content,
    photo_data,
    posts.album_id;


--Query to get a "Timeline" of posts in chronological order
SELECT
    posts.post_id,
    posts.post_content,
    posts.post_date,
    COUNT(likes.user_id) AS like_count
FROM
    posts
LEFT JOIN
    likes ON posts.post_id = likes.post_id
WHERE
    posts.user_id = :user_id
GROUP BY
    posts.post_id, posts.post_content, posts.post_date
ORDER BY
    posts.post_date DESC;


--get a timeline of posts from
SELECT
    posts.post_id,
    posts.post_content,
    posts.post_date,
    COUNT(likes.user_id) AS like_count
FROM
    posts
JOIN
    followers ON posts.user_id = followers.user_id --get posts from accounts that the user follows
LEFT JOIN
    likes ON posts.post_id = likes.post_id
WHERE
    followers.follower_id = :user_id
GROUP BY
    posts.post_id, posts.post_content, posts.post_date
ORDER BY
    posts.post_date DESC;


--test if cascade works -> it works
--dangerous query
DELETE from users; --delete all users and their associated tables
ALTER SEQUENCE users_user_id_seq RESTART WITH 1; -- reset the sequence
ALTER SEQUENCE photos_photo_id_seq RESTART WITH 1;
ALTER SEQUENCE albums_album_id_seq RESTART WITH 1;
ALTER SEQUENCE community_posts_community_post_id_seq RESTART WITH 1;

INSERT INTO users (username, password, email, profile_picture, public_access)
VALUES
    ('real_person', 'password1', 'user1@example.com', E'\\x89504e470d0a1a0a', true), -- Hexadecimal representation of a profile picture
    ('real_shopper', 'password2', 'user2@example.com', E'\\x89504e470d0a1a0a', true),
    ('real_person_community', 'password3', 'user3@example.com', E'\\x89504e470d0a1a0a', true);

select * from users; -- check if the data is cleared


-- Insert 100 albums with identical photos
INSERT INTO albums (user_id, album_name)
SELECT 3, 'Community Album ' || generate_series(1, 100);

-- Insert 100 identical photos
INSERT INTO photos (album_id, photo_data)
SELECT
    a.album_id,
    '/static/images/ThriftMe_logo.png'
FROM albums a;

-- Insert 100 community posts referencing different albums with identical photos
INSERT INTO community_posts (user_id, post_content, album_id)
SELECT
    3,
    'Community Post ' || a.album_id,
    a.album_id
FROM albums a;

-- Verify the inserted community posts
SELECT * FROM community_posts;


delete from community_posts;
select * from photos;
select * from albums;


--translate this to SQLAlchemy later > done

SELECT
    cp.post_content,
    cp.post_date
    p.photo_data
FROM
    community_posts cp
JOIN
    albums a ON cp.album_id = a.album_id
LEFT JOIN
    photos p ON a.album_id = p.album_id;
