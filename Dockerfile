FROM python:3.8

RUN apt-get update -y

COPY . /project

WORKDIR /project

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Add necessary folders
RUN mkdir logs logs/uwsgi

# EXPOSE 8000

# Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

# CMD ["python", "projectile/manage.py", "runserver", "0:8080", "--settings", "projectile.settings_live"]
# CMD ["uwsgi", "--http", ":8080", "--wsgi-file", "conf/wsgi/docker.wsgi"]
CMD ["uwsgi", "--ini", "conf/uwsgi/docker.ini"]