# CHILDGUARD:Smart Monitoring & Identification System for Missing Children
AI-powered Missing Children Identification System using Django and Computer Vision
# CHILDGUARD:Smart Monitoring & Identification System for Missing Children

An AI-powered Missing Children Identification and Tracking System designed to help identify missing children using facial recognition technology and support location-based tracking.

## 📌 Project Overview

CHILDGUARD is a web-based application developed using Python and Django. It uses Artificial Intelligence and facial recognition to assist in identifying missing children by comparing facial images against registered records.

The system also integrates geographical location services to help visualize and track reported missing-child cases.

The primary objective is to provide a technology-driven platform that connects users, authorities, and communities to support missing-child identification and recovery.

## 🎯 Objectives

- Develop an AI-powered facial recognition system for identifying missing children.
- Compare uploaded facial images with registered missing-child records.
- Support location-based tracking of missing-child reports.
- Provide a centralized platform for managing missing-child information.
- Improve communication between users, helplines, and administrators.

## ✨ Key Features

### 1. AI-Based Facial Recognition
- Face detection using RetinaFace.
- Facial recognition using DeepFace.
- ArcFace facial recognition model.
- Facial similarity comparison to identify potential matches.

### 2. Missing Child Registration
- Register missing-child information.
- Upload photographs and relevant details.
- Maintain missing-child records.

### 3. Location-Based Tracking
- Geographical location identification.
- Distance calculation using the Haversine formula.
- Location services using Geopy and OpenStreetMap Nominatim.
- Interactive map visualization using Leaflet.

### 4. User Management
- User registration and authentication.
- Submit missing-child reports.
- Access relevant information.

### 5. Administrative Management
- Manage registered users.
- Manage missing-child records.
- Review and monitor submitted reports.

### 6. Helpline and Society Support
- Dedicated helpline functionality.
- Community-oriented information sharing.
- Support for coordinated missing-child reporting.

## 🛠️ Technologies Used

| Category | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Django 4.2.23 |
| Database | SQLite |
| AI / Deep Learning | DeepFace |
| Face Detection | RetinaFace |
| Face Recognition Model | ArcFace |
| Geolocation | Geopy |
| Distance Calculation | Haversine Formula |
| Map Visualization | Leaflet |
| Map Data | OpenStreetMap |
| Frontend | HTML, CSS, JavaScript |

## 🧠 AI Implementation

CHILDGUARD integrates facial recognition technology through the DeepFace framework.

**Workflow:**

1. A missing-child photograph is registered in the system.
2. The system detects the face using RetinaFace.
3. ArcFace generates facial representations.
4. When a new image is uploaded, its facial representation is extracted.
5. The system compares the facial representations.
6. Potential matches are identified based on a configurable similarity threshold.

Note: Facial recognition results are potential matches, not proof of identity. Human verification is essential.

## 📂 Project Structure

```text
CHILDGUARD/
│
├── childmissed/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   ├── profile/
│   ├── userphoto/
│   └── ...
│
├── templates/
├── static/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

*The structure above is a representative layout; adjust it to match the actual repository.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or compatible version.
- pip package manager.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CHILDGUARD.git
```

### 2. Navigate to the Project

```bash
cd CHILDGUARD
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000/

## 🔐 Security and Privacy

CHILDGUARD handles sensitive personal information, particularly photographs and missing-child records.

Security considerations include:

- Protecting personal information and uploaded photographs.
- Keeping secret keys and credentials outside the public repository.
- Disabling Django DEBUG mode in production.
- Using secure authentication and authorization.
- Restricting access to sensitive records.
- Obtaining appropriate consent and following applicable child-data protection requirements.

## 🚀 Future Enhancements

- Cloud-based deployment.
- Improved facial recognition accuracy.
- Real-time notification system.
- Integration with authorized child protection organizations.
- Enhanced geolocation and tracking functionality.
- Mobile application integration.
- Stronger data encryption and privacy controls.

## 👩‍💻 Developer

**Varada Devan**

B.Voc Mathematics and Artificial Intelligence

St. Joseph's College (Autonomous), Irinjalakuda

Project: CHILDGUARD – Missing Children Identification System

## 📜 Disclaimer

CHILDGUARD is an academic technology project developed to demonstrate the application of Artificial Intelligence, facial recognition, web development, and geolocation technologies.

It is not an official government missing-child database or an independently verified child identification service. Facial recognition outputs must be reviewed by authorized personnel.

---

**CHILDGUARD – Technology for a Safer Tomorrow.**
