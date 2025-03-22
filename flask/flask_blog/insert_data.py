import json
from app import db
from app.models import User, Post  # Ensure correct import
from werkzeug.security import generate_password_hash

from app import create_app

app = create_app()
app.app_context().push()


# Load data from JSON
with open("dummy_data.json") as f:
    data = json.load(f)

# Insert users
for user_data in data["users"]:
    user = User(
        username=user_data["username"],
        email=user_data["email"],
        image_file=user_data["image_file"],
        password=generate_password_hash(user_data["password"])
    )
    db.session.add(user)

db.session.commit()  # Commit users first to get valid user IDs

# Insert posts
for post_data in data["posts"]:
    post = Post(
        title=post_data["title"],
        content=post_data["content"],
        user_id=post_data["user_id"]
    )
    db.session.add(post)

db.session.commit()  # Commit posts

print("Dummy data inserted successfully!")
