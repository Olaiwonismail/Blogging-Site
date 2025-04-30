import json
from datetime import datetime
from app import db, create_app
from app.models import User, Post, Like
from werkzeug.security import generate_password_hash

# Initialize Flask app and database
app = create_app()
app.app_context().push()
db.create_all()

# Load data from JSON file
with open("dummy_data_.json") as f:
    data = json.load(f)

# Insert users
for user_data in data["users"]:
    user = User(
        username=user_data["username"],
        email=user_data["email"],
        image_file=user_data.get("image_file", User.image_file.default.arg),
        password=generate_password_hash(user_data["password"])
    )
    db.session.add(user)

# Commit users to assign IDs
db.session.commit()

# Insert posts
for post_data in data["posts"]:
    # Parse ISO timestamp, fallback to current time
    try:
        date_posted = datetime.strptime(post_data["date_posted"], "%Y-%m-%dT%H:%M:%SZ")
    except (KeyError, ValueError):
        date_posted = datetime.utcnow()

    post = Post(
        title=post_data["title"],
        content=post_data["content"],
        date_posted=date_posted,
        user_id=post_data["user_id"]
    )
    db.session.add(post)

# Commit posts to assign post IDs
db.session.commit()

# Insert likes
for like_data in data.get("likes", []):
    like = Like(
        user_id=like_data["user_id"],
        post_id=like_data["post_id"]
    )
    db.session.add(like)

# Commit likes
db.session.commit()

print("Dummy data inserted successfully!")