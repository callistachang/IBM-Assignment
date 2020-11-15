# VizWeb

Built with Django 3.1.

## Video Demonstration

[here](https://ibm-vizapp.s3.us-east-2.amazonaws.com/video-demo.mp4)

## Local Setup Instructions

#### 1. Set up environment variables

Replace the variables in `.env.example` with your own values and rename the file to `.env`.

#### 2. Download Dependencies

<ins>With Poetry as a package manager</ins>

Download Poetry [here](https://python-poetry.org/docs/#installation) first.

```
cd vizweb
poetry install
poetry shell
```

<ins>With Pip as a package manager</ins>

Create a virtual environment first (optional).

```
cd vizweb
pip install -r requirements.txt
```

#### 3. Migrate Database Schema

```
cd vizweb
python manage.py makemigrations
python manage.py migrate
```

#### 4. Start Local Server (Port 8000)

```
cd vizweb
python manage.py runserver
```
