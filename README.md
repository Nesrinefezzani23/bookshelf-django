# 📚 bookshelf-django

![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Stars](https://img.shields.io/github/stars/Nesrinefezzani23/bookshelf-django?style=social)

A stylish Django web app for managing your personal bookshelf. Easily add, organize, and favorite books—all with a clean interface!

---

## ✨ Features

- 📝 **Book Management:** Add, edit, and remove books from your personal collection.
- ⭐ **Favorites:** Mark and view your favorite titles in a dedicated section.
- 📚 **Search & Filter:** Quickly find books by title, author, or genre.
- 🗄️ **Book Covers:** Upload images for each book.
- 🔒 **User Authentication:** Register, login, and keep your bookshelf private.
- 📊 **Responsive Design:** Works beautifully on desktop and mobile.
- 🛠️ **Secure & Extensible:** Built with Django's robust security and easy to extend.

---

## 🚀 Quick Start

```bash
git clone https://github.com/Nesrinefezzani23/bookshelf-django.git
cd bookshelf-django
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## 🖼️ Screenshot

![Screenshot 2025-07-03 3 33 43 PM](https://github.com/user-attachments/assets/512b1c14-3c85-45b4-8135-ecb7b90f1714)

---

## 🗂️ Project Structure

```text
bookshelf-django/
├── bookstore/                 # Main Django project
├── hkeyet/                    # Main books application
├── media/                     # Uploaded media files
├── venv/                      # Virtual environment (should be in .gitignore)
├── book_detail.html           # HTML template (book detail page)
├── booksApp_favorites.html    # HTML template (favorites page)
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django management script
```
---

## 🛠️ Built With

- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/index.html) (default, easy to swap)
- [Bootstrap](https://getbootstrap.com/) or your CSS framework

---

## 🙋‍♀️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 📃 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

- Nesrine Fezzani – [GitHub](https://github.com/Nesrinefezzani23)

---

> _“A room without books is like a body without a soul.”_
