# FastAPI Feedback Application

This is a simple Feedback API built with FastAPI, SQLAlchemy (asyncpg), PostgreSQL, and Alembic for handling database migrations. The application allows users to create, read, update, and delete feedback entries.

## Table of Contents

- [FastAPI Feedback Application](#fastapi-feedback-application)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Database Migration](#database-migration)
  - [Running the Application](#running-the-application)

## Features

- **Create Feedback**: Allows adding new feedback entries.
- **Read Feedback**: Retrieve all feedback entries.
- **Update Feedback**: Modify existing feedback entries.
- **Delete Feedback**: Remove feedback entries.

## Prerequisites

- Python 3.8+
- PostgreSQL
- `pip` for package management

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/1stdeddy2nd/feedback-app-be.git
   cd feedback-app-be
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create .env File**

   Create a .env file in the root directory of your project with the following content:

   ```bash
   DATABASE_URL="postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>"
   ```

   Replace `user`, `password`, `host`, `port`, and `database` with your PostgreSQL database credentials.

## Database Migration

1. **Migrate with alembic**

   ```bash
   alembic upgrade head
   ```

## Running the Application

1. **Start the FastAPI Server in Dev**

   ```bash
   fastapi dev app/main.py
   ```

2. **Access the API**

   Open your browser and go to `http://localhost:8000` to access the API. You can also access the automatic interactive API documentation at:

   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`
