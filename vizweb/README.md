# VizWeb

Built with Django 3.1.

## Video Demonstration

[Web demo](https://entuedu-my.sharepoint.com/:v:/g/personal/call0001_e_ntu_edu_sg/EQwF2diFVwJFvMdn0Y26m0UBnrZ8E5d0UxrmSwzOmEiXkQ?e=CNEgmh)

[Mobile demo](https://entuedu-my.sharepoint.com/:v:/g/personal/call0001_e_ntu_edu_sg/EajjEoioLuFHrPopQgWGcX0BBFMrAosmwnlo3cQS8yDNQQ?e=h6pfqr)

## Local Setup Instructions

#### 1. Set up environment variables

Replace the variables in `.env.example` with your own values and rename the file to `.env`. You must own IBM Cloud and AWS accounts and activate their [Visual Recognition](https://www.ibm.com/cloud/watson-visual-recognition) and [S3](https://aws.amazon.com/s3/) services respectively.

#### 2. Download Dependencies

<ins>With Poetry as a package manager</ins>

Download Poetry [here](https://python-poetry.org/docs/#installation) first.

```
cd vizweb
poetry install # create virtual environment and download dependencies
poetry shell   # activate virtual environment
```

<ins>With Pip as a package manager</ins>

Create and activate a virtual environment first with instructions [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (optional).

```
cd vizweb
pip install -r requirements.txt
```

#### 3. Migrate Database Schema

```
python manage.py makemigrations
python manage.py migrate
```

#### 4. Start Local Server (Port 8000)

```
python manage.py runserver
```
