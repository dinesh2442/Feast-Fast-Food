# 🍔 Feast Fast Food

Feast Fast Food is a full-stack **Django web application** that allows users to browse, order, and manage fast food
items with a smooth and responsive UI. It features **user authentication**, **Add to Cart**, **Order Management**, *
*Email Notifications**, and **Admin Controls** — all in one dynamic, mobile-friendly platform.

---

## 🚀 Features

### 👤 User Features

- 📝 **Register / Login / Logout**
- 🔐 **Change Password** & **Forgot Password (Email Notification)**
- 🛒 **Add to Cart** functionality with:
    - ➕ / ➖ Quantity adjustment
    - 💰 Real-time total price update per product
    - 🧾 Grand total displayed in cart
- 📦 **Place Order** – Generates unique order ID and stores order details
- 📧 **Email Notifications** for:
    - Successful registration
    - Password reset
    - Order confirmation
    - Order status updates (Ready / Delivered)

---

### 🧑‍💼 Admin Features

- ➕ Add / Edit / Delete **Categories** and **Products**
- 🧾 View all **User Orders** and **Order Details**
- 🔄 Update **Order Status** → Ready / Delivery (Triggers user email)
- 📊 Manage all users, orders, and food items efficiently

---

## 🛠️ Tech Stack

| Component             | Technology                       |
|-----------------------|----------------------------------|
| 💻 **Frontend**       | HTML, CSS, JavaScript, Bootstrap |
| ⚙️ **Backend**        | Django Web Framework             |
| 🐍 **Python Version** | Python 3.13.7                    |
| 🗄️ **Database**      | PostgreSQL                       |
| 🧰 **IDE / Tools**    | PyCharm, pgAdmin                 |
| 🌐 **Web Server**     | Django Development Server        |

---

## 📦 Python Packages Used

asgiref==3.9.1
Django==5.2.6
django-admin-sortable2==2.2.8
pillow==11.3.0
psycopg2==2.9.10
sqlparse==0.5.3
tzdata==2025.2


---

## 🗃️ Database Setup

1. Open **pgAdmin** or **psql** terminal.

2. Create a new database named:

   ```sql
   CREATE DATABASE fastfoodapp;

3.Update your Django project’s settings.py file with your PostgreSQL credentials:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'fastfoodapp',
'USER': 'your_postgres_username',
'PASSWORD': 'your_postgres_password',
'HOST': 'localhost',
'PORT': '5432',
}
}

⚙️ Installation & Setup Guide
Follow these steps to get the project running locally 👇

1️⃣ Clone the repository
git clone https://github.com/yourusername/feast-fast-food.git
cd feast-fast-food

2️⃣ Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate # For Windows

# OR

source venv/bin/activate # For macOS/Linux

3️⃣ Install all dependencies
pip install -r requirements.txt

4️⃣ Apply database migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (for admin access)
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

7️⃣ Access the site

* 🌐 Frontend: http://127.0.0.1:8000/
* 🔑 Admin Panel: http://127.0.0.1:8000/admin/

📱 Responsive Design
Feast Fast Food is fully responsive and mobile-friendly, built using:

⚡ Bootstrap

* 🎨 Custom CSS

* 📲 Works seamlessly on mobile, tablet, and desktop

💌 Email Notifications
All user-related emails (registration, password reset, order updates) are sent using Django Signals and the configured
email backend in settings.py.

📬 Future Enhancements

* 💳 Online Payment Gateway Integration

* 🗺️ Real-time Delivery Tracking

* ⭐ Customer Reviews and Ratings

👨‍💻 Author
Developed by: Dinesh T
💡 Tools used: PyCharm, PostgreSQL, Django, Bootstrap, HTML/CSS/JS

🏁 License
This project is open-source and available for educational and portfolio purposes.
Feel free to modify and enhance it as needed. ❤️

✨ “Feast Fast Food — Order Fast, Eat Fresh!” 🍕🍟


---



