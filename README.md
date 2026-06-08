# 📺 Semi-Restful TV Shows — With Validation

A full-stack Django web application for managing TV shows, built with the **MTV architecture** (Model-Template-View). This project demonstrates full CRUD operations with server-side validation to prevent dirty data from entering the database.

---

## 🚀 Features

- View all TV shows in a table
- Add a new TV show with a form
- View a single show's details
- Edit and update an existing show
- Delete a show
- **Server-side validation** on both Create and Update forms
- Errors displayed on the same page without losing user input

---

## 🗂️ Project Structure

```
tv_project_valid/
├── tv_project/          # Main Django project (settings, urls)
├── shows_app/           # The app
│   ├── models.py        # Show model
│   ├── views.py         # All logic + validations
│   ├── urls.py          # URL routes
│   └── templates/
│       └── shows/
│           ├── index.html   # All shows
│           ├── new.html     # Add show form
│           ├── show.html    # Show detail
│           └── edit.html    # Edit show form
└── manage.py
```

---

## 🔗 Routes (Semi-RESTful)

| Method | URL                        | Action         |
|--------|----------------------------|----------------|
| GET    | `/shows/`                  | All shows      |
| GET    | `/shows/new/`              | Add show form  |
| POST   | `/shows/create/`           | Save new show  |
| GET    | `/shows/<id>/`             | Show detail    |
| GET    | `/shows/<id>/edit/`        | Edit show form |
| POST   | `/shows/<id>/update/`      | Save changes   |
| POST   | `/shows/<id>/destroy/`     | Delete show    |

---

## 🧱 Model — `Show`

```python
class Show(models.Model):
    title        = models.CharField(max_length=255)
    network      = models.CharField(max_length=255)
    release_date = models.DateField()
    description  = models.TextField()
    updated_at   = models.DateTimeField(auto_now=True)
```

---

## ✅ Validation Rules

Validation runs in the view **before** saving to the database:

| Field         | Rule                              |
|---------------|-----------------------------------|
| Title         | Required, at least 2 characters   |
| Network       | Required                          |
| Release Date  | Required                          |
| Description   | Required, at least 10 characters  |

### How it works

1. User submits the form (POST request)
2. View collects all field values from `request.POST`
3. Each field is checked — if invalid, an error message is added to an `errors` dictionary
4. If `errors` is not empty → re-render the form with errors displayed in red, and user's input preserved
5. If `errors` is empty → save to DB and redirect

```python
errors = {}

if len(title) < 2:
    errors['title'] = 'Title must be at least 2 characters.'

if errors:
    return render(request, 'shows/new.html', {
        'errors': errors,
        'data': request.POST   # keeps the user's input in the form
    })

# No errors — safe to save
Show.objects.create(...)
```

---

## 🖥️ How to Run

```bash
# 1. Activate virtual environment
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install django

# 3. Run migrations
python manage.py migrate

# 4. Start the server
python manage.py runserver

# 5. Open in browser
http://localhost:8000/
```

---

## 🛠️ Built With

- Python 3.13
- Django 6.x
- SQLite (default Django DB)
- HTML / CSS (minimal, no frameworks)

---

## 👨‍💻 Author

**Ahmad Shweiki** — Full Stack Development Student @ AXSOS Academy