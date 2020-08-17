docker build -t django-app .
docker run --network="host" --env-file=/home/django/.env -d -p 8080:8080 django-app