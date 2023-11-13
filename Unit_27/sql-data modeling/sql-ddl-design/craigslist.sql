--Design a schema for Craigslist! Your schema should keep track o f the following
    --The region of the craigslist post (San Francisco, Atlanta, Seattle, etc)
    --Users and preferred region
    --Posts: contains title, text, the user who has posted, the location of the posting, the region of the posting
    --Categories that each post belongs to

CREATE TABLE regions(
    id SERIAL PRIMARY KEY,
    region TEXT NOT NULL,
)

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    location TEXT NOT NULL,
    region_id INTEGER REFERENCES regions,
    post_id INTEGER REFERENCES posts,
)

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    post TEXT NOT NULL,
    user_id INTEGER REFERENCES users,
    region_id INTEGER REFERENCES regions,
)

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL,
    post_id INTEGER REFERENCES posts
)
