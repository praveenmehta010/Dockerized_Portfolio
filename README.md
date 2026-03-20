# 🚀 Praveen Mehta Portfolio

A modern developer portfolio built using **FastAPI, MongoDB Atlas, and HTML/CSS/JS**.
This project showcases work, skills, and allows users to contact through a fully functional contact form. This data get saved in database

---

## 📌 Features

* 🧑‍💻 Personal portfolio website
* 📂 Dynamic project listing (fetched from MongoDB)
* 📩 Contact form (stores messages in database)
* ⚡ FastAPI backend (fast & efficient)
* 🎨 Clean, responsive UI

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Database:** MongoDB Atlas
* **Templating:** Jinja2

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/praveenmehta010/Portfolio2.git
cd Portfolio2
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

#### Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` file

Create a `.env` file in the root directory:

```env
MONGO_URI=""

example
MONGO_URI="mongodb+srv://username:password@database.net/" // you can get the URI from mongodb atlas

```

---

### ⚠️ Important

* Replace `username` and `password` with your MongoDB credentials
* Never share your `.env` file publicly
* Add `.env` to `.gitignore`

---

### 5️⃣ Run the server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
project/
├── app/
│──── config/
│     ├── mongo_db_connection.py
│──── models/
│     ├── contact.py
│──── routes/
│     ├── my_routes.py
├──── static/
│     ├── style.css
│     ├── script.js
├──── templates/
│     ├── index.html
│──── main.py
│
│── requirements.txt
│── .env
│── .gitignore
│── README.md
```

---

## 📸 Features Overview

* Projects are dynamically loaded from MongoDB Atlas
* Contact form saves messages to database
* Fully responsive and modern UI

---

## 🚀 Future Improvements

* 🔐 Admin dashboard for managing projects
* 📝 Add/Edit projects via UI
* ☁️ Cloud deployment (Render / Railway)

---

## 📬 Contact

Feel free to reach out through the contact form on the website 🚀

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
