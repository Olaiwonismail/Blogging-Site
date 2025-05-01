# Blogging Platform

A simple and elegant blogging platform built with Flask. Users can create accounts, write posts, and engage with other users by liking posts.

---

## 🌐 Features

- User registration, login, and profile management  
- Create, read, update, and delete blog posts  
- Like system to engage with content  
- Flash messaging for user feedback  
- Paginated homepage for posts  
- Bootstrap-styled interface  

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy  
- **Database**: SQLite or PostgreSQL  
- **Frontend**: HTML, CSS, Bootstrap  
- **Authentication**: Flask-Login  
- **ORM**: SQLAlchemy  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/blogging-app.git
cd blogging-app
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. (Optional) Insert dummy data

```bash
python insert_dummy_data.py
```

### 6. Run the app

```bash
flask run
```

---

## ✍️ Author

**Olaiwon Ismail**  
GitHub: [@Olaiwonismail](https://github.com/Olaiwonismail)  
LinkedIn: [Ismail Olaiwon](https://linkedin.com/in/ismail-olaiwon-186938324)

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

