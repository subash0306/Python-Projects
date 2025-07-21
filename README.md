🖼️Image Converter Web App (Django + Pillow)
This is a Django-based web application that allows users to upload multiple images and convert them into a different format (like .jpg, .png, .webp, etc.). Built using the Django framework and Pillow (Python Imaging Library).

✅ Features
Upload multiple images at once
  1. Choose target output format (jpg, png, webp, etc.)
  2. Optional resizing support (if included in your app)
  3. Auto-generated download links for converted files
  4. Clean and user-friendly web interface

🛠️ Technologies Used
  1. Django – Web framework for Python
  2. Pillow – Python Imaging Library for image processing
  3. HTML/CSS – For basic frontend
  4. UUID – For handling unique file names

📦 Requirements
bash:
  pip install django pillow

🚀 How to Run the Project
1. Clone the repository:
   bash:
    git clone https://github.com/subash0306/Python-Projects.git
    cd Python-Projects/image\ converter/image_converter

3. Run migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver

5. Open your browser and go to:
  👉 http://127.0.0.1:8000/

📂 Project Structure
image_converter/
├── converter/            # Django app
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── media/                # Uploaded/converted images (runtime)
├── image_converter/      # Django project config
│   └── settings.py
├── manage.py
└── README.md

🧠 Learning Objectives
  1. File upload handling in Django
  2. Image processing with Pillow
  3. Working with request.FILES and uuid for unique file names
  4. Building user-friendly web tools with Django
