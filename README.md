# 📺 Semi-Restful TV Shows

A Django web application that implements full CRUD functionality for managing TV shows, following RESTful routing conventions.

---

## 🎯 Objectives

- Practice ORM queries from the controller
- Practice RESTful routing
- Practice rendering query results to templates
- Practice using form input to create and update database records

---

## 🛠️ Tech Stack

- **Backend:** Python / Django 6.0
- **Database:** SQLite3
- **Frontend:** HTML5 / Django Templates
- **Architecture:** MTV (Model - Template - View)

---

## 📁 Project Structure

```
tv_project/
├── tv_project/
│   ├── settings.py
│   └── urls.py
├── shows_app/
│   ├── templates/
│   │   └── shows/
│   │       ├── index.html     ← All shows list
│   │       ├── new.html       ← Add new show form
│   │       ├── show.html      ← Single show detail
│   │       └── edit.html      ← Edit show form
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── manage.py
```

---

## 🗃️ Model

```python
class Show(models.Model):
    title        = models.CharField(max_length=200)
    network      = models.CharField(max_length=100)
    release_date = models.DateField()
    description  = models.TextField()
    updated_at   = models.DateTimeField(auto_now=True)
```

---

## 🔀 RESTful Routes

| Method | Route | Action | Description |
|--------|-------|--------|-------------|
| GET | `/shows/` | `all_shows` | Display all TV shows in a table |
| GET | `/shows/new/` | `new_show` | Show form to add a new show |
| POST | `/shows/create/` | `create_show` | Save new show, redirect to `/shows/<id>/` |
| GET | `/shows/<id>/` | `show_detail` | Display one show's details |
| GET | `/shows/<id>/edit/` | `edit_show` | Show form pre-filled with show data |
| POST | `/shows/<id>/update/` | `update_show` | Update show, redirect to `/shows/<id>/` |
| POST | `/shows/<id>/destroy/` | `destroy_show` | Delete show, redirect to `/shows/` |

> ⚠️ `shows/new/` and `shows/create/` must be defined **before** `shows/<int:show_id>/` in `urls.py` — Django reads URLs top-to-bottom.

---

## ⚙️ Setup & Installation

```bash
# 1. Clone or create the project
django-admin startproject tv_project
cd tv_project
python manage.py startapp shows_app

# 2. Add 'shows_app' to INSTALLED_APPS in settings.py

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start the server
python manage.py runserver
```

Then open your browser at: `http://127.0.0.1:8000/`

The root `/` automatically redirects to `/shows/`.

---

## 💡 Key Concepts

### Why POST for Delete and Update?
HTML `<a href>` tags always send **GET** requests. Since delete and update modify data, they must use **POST** via a `<form>` tag.

### Why `{% csrf_token %}`?
Django's built-in security. Every POST form requires this token or Django will reject the request with a 403 error.

### Why `|date:'Y-m-d'` filter?
The `<input type="date">` HTML element requires the format `YYYY-MM-DD`. Without this filter, the date field renders blank in the edit form.

### Why `auto_now=True` on `updated_at`?
Every time `.save()` is called on a model instance, Django automatically updates this field to the current timestamp — no manual update needed.

---

## 🧪 Testing the App

| Step | URL | Expected Result |
|------|-----|-----------------|
| 1 | `localhost:8000/` | Redirects to `/shows/` |
| 2 | `localhost:8000/shows/` | Shows table with all records |
| 3 | `localhost:8000/shows/new/` | Empty form to add a show |
| 4 | Submit form | Redirects to new show's detail page |
| 5 | Click Edit | Form pre-filled with current data |
| 6 | Submit update | Redirects back to show detail |
| 7 | Click Delete | Show removed, back to `/shows/` |

---

## 👨‍💻 Author

Built as part of the **AXSOS Academy** Full Stack Development Program.