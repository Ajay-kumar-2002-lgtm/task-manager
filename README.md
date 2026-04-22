# 🚀 Task Manager (Full Stack Application)

A modern full-stack Task Manager application built using React (Frontend) and Django REST Framework (Backend).

This application allows users to create, update, delete, and filter tasks with a clean and responsive user interface.

---

## 📌 Features

### ✅ Backend (Django API)
- RESTful API design
- Create new tasks
- Retrieve all tasks
- Update task status (Pending ↔ Completed)
- Delete tasks
- SQLite database integration
- Error handling and validation

### ✅ Frontend (React UI)
- Add new tasks
- View task list
- Toggle task completion
- Delete tasks
- Filter tasks:
  - All
  - Pending
  - Completed
- Responsive and modern UI
- Optimistic UI updates (no unnecessary reloads)

---

## 🧠 Tech Stack

- Frontend: React.js, CSS
- Backend: Django, Django REST Framework
- Database: SQLite
- API Calls: Axios

---

## ⚙️ Backend Setup (Django)

1. Navigate to backend folder
cd backend

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install django djangorestframework django-cors-headers

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Start server
python manage.py runserver

Backend runs at:
http://127.0.0.1:8000/

---

## 🔗 API Endpoints

GET     /api/tasks              → Get all tasks  
POST    /api/tasks/create       → Create new task  
PUT     /api/tasks/:id          → Toggle task status  
DELETE  /api/tasks/delete/:id   → Delete task  

---

## 🎨 Frontend Setup (React)

1. Navigate to frontend folder
cd frontend

2. Install dependencies
npm install
npm install axios

3. Start React app
npm start

Frontend runs at:
http://localhost:3000/

---

## 🔄 Frontend-Backend Integration

React communicates with Django using Axios.

Base API URL:
http://127.0.0.1:8000/api

Data Flow:
React → API → Django → Database → Response → UI

---

## 🧩 Functional Overview

🔹 Add Task  
- User enters task  
- React sends POST request  
- Django saves it in database  

🔹 Toggle Task  
- Click task → switches between pending and completed  
- Backend updates status  
- UI updates instantly  

🔹 Delete Task  
- Click delete button  
- Task removed from database and UI  

🔹 Filter Tasks  
- All / Pending / Completed  
- Implemented using:
filteredTasks = tasks.filter(...)

---

## 🎨 UI Features

- Gradient background  
- Glassmorphism card design  
- Smooth hover animations  
- Clean and responsive layout  

---

## ⚡ Performance Features

- Optimistic UI updates  
- Efficient state management  
- Reduced API calls  

---

## ❗ Error Handling

- Prevents empty task submission  
- Handles API errors with try/catch  
- Displays user-friendly messages  

---

## 🚀 Future Improvements

- Authentication (Login/Signup)  
- Search functionality  
- Drag & Drop tasks  
- Task deadlines  
- Deployment  

---

## 👨‍💻 Author

Ajay Kumar

---

## 📌 Conclusion

This project demonstrates:
- Full-stack development skills  
- API integration  
- Clean UI/UX design  
- Maintainable and scalable code  

## 📸 Screenshots

### 🏠 Main Dashboard
![Home](screenshots/home.png)

### ➕ Add Task
![Add Task](screenshots/add-task.png)
