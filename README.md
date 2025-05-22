# 📘 MedicalConsulting

## 1. Overview

### 📝 Project description
MedicalConsulting is a medical consultation management application. Clients consult doctors on specific dates and are prescribed medications. Each medication has an associated cost and can be dispensed in specific quantities.

### 🎯 Objective
The primary objective is to streamline the management of medical consultations and prescriptions efficiently.

---

## 2. Features

### ✅ Features list
<!--
- User authentication (login, registration, logout)
- Interactive dashboard
- CRUD operations for managing data
- Export data in CSV/PDF formats
- Mobile-responsive interface
- Real-time notifications
-->

---

## 3. Requirements

### 🛠️ Required environment
- **Operating System**: Windows / macOS / Linux
- **Languages & Frameworks**: Odoo 18, Python 3.11.9
- **Database**: PostgreSQL

---

## 4. Installation

🔧 Installation instructions :

### Cloner the repository
```bash
git clone https://github.com/tafita37/MedicalConsulting.git
```

### Setup the project in the Odoo modules directory, create a virtual environment, install dependencies, and run the project:

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python odoo-bin -c odoo.conf -u <module_name> -d <base_name> --dev xml
```