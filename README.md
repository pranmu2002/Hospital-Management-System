# Hospital Management System

A comprehensive web-based **Hospital Management System** built with **Django** to manage doctors, patients, beds, appointments, payments, and enquiries efficiently.

## Table of Contents

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Screenshots](#screenshots)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## About the Project

This Hospital Management System is a full-featured web application designed to simplify the day-to-day operations of a hospital. It helps hospital administrators and staff manage doctors, patients, beds, payments, and enquiries all in one place. Built on Django, it offers a secure and scalable platform to improve hospital workflow and patient care.

## Features

- Doctor Management: Add, update, view, and delete doctor profiles.
- Patient Management: Register patients, update their details, and assign beds.
- Bed Management: Track availability and allocation of hospital beds.
- Appointment Scheduling: Book, view, edit, and cancel patient appointments with doctors.
- Payment Handling: Manage payments, including total fees, paid and unpaid amounts with automatic calculations.
- Enquiry Management: Handle patient or visitor enquiries efficiently.
- Search Functionality: Quickly find doctors, patients, appointments, and payments.
- User-friendly Admin Panel: Easy navigation and management of all modules.
- Responsive design with Bootstrap for a clean and intuitive UI.

## Technology Stack

- Backend: Python, Django  
- Frontend: HTML5, CSS3, Bootstrap 3  
- Database: SQLite (default Django DB, easily switchable)  
- Version Control: Git, GitHub  

## Installation

## Clone the repo

   ```bash
   git clone https://github.com/pranmu2002/Hospital-Management-System.git
   cd Hospital-Management-System
Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

## Create a superuser (admin account)

python manage.py createsuperuser

## Run the development server

    python manage.py runserver

    Open your browser and go to http://127.0.0.1:8000/ to see the application.

Usage

    Log in as admin to access the dashboard.

    Navigate through sections for Doctors, Patients, Beds, Appointments, Payments, and Enquiries.

    Add, edit, or delete records as required.

    Use the search bars to quickly locate specific entries.

    Manage payments with automatic unpaid fee calculations.

    Download payment receipts directly from the payment section.

## Project Structure

Hospital-Management-System/
│
├── hospital_management/
├── app/
├── static/
├── templates/
├── requirements.txt
├── manage.py
└── README.md




    Author: Pranmu and Ananya-Das-Diya

    GitHub: https://github.com/pranmu2002

    Email: swagatoroy2002@gmail.com  and  ananya.das.diya.10@gmail.com

