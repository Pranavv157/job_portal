# Job Portal – Django Backend Project

A role-based job portal built using Django, focused on backend architecture, clean code practices, and real-world features.

---

##   Features

### Authentication & Roles
- User registration and login
- Role-based access control (Recruiter / Candidate)
- Automatic role-based routing after login

### Recruiter
- Post jobs
- View posted jobs
- View applicants
- Search, filter, and paginate jobs
- Dynamic location filtering

### Candidate
- Browse jobs
- Search by title or company
- Filter by location (dynamic from DB)
- Apply to jobs with resume upload
- Prevent duplicate applications
- View applied jobs (“My Applications”)

---

##  Backend Concepts Used

- Django ORM & ForeignKey relationships
- Database-level constraints (unique job application)
- Custom decorators for role-based access
- Service layer for reusable filtering logic
- Pagination with query preservation
- File uploads handling
- Clean separation of concerns

---


---

## 🛠 Tech Stack

- Python
- Django
- SQLite (development)
- HTML / CSS (Django Templates)

---

## 📌 Notes

This project focuses on backend correctness and architecture rather than frontend frameworks.
It demonstrates patterns commonly used in production Django applications.

---

## 👤 Author

Built by **<Pranav Shinde>**


