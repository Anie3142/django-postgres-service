## Compose Sample Application with PostgreSQL

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/django-postgres)

### Django Application with PostgreSQL in Dev Mode

Project structure:
```
.
├── .env
├── docker-compose.yml
├── app
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py
└── postgres_data (Docker volume)

```

[_docker-compose.yml_](docker-compose.yml)
```yaml
version: '3'

services:
  web:
    build:
      context: .
      target: builder
    ports:
      - '8000:8000'
    depends_on:
      - db
    environment:
      - DATABASE_HOST=db
      - DATABASE_USER=postgres
      - DATABASE_PASSWORD=postgres
      - DATABASE_NAME=postgres
      - DATABASE_PORT=5432

  db:
    image: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

volumes:
  postgres_data:
```

## Deploy with Docker Compose

First, create a `.env` file in the root directory with the following content:
```
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

Then, deploy your application:
```
$ docker compose up -d
Creating network "django_postgres_default" with the default driver
Building web
Step 1/6 : FROM python:3.7-alpine
...
...
Status: Downloaded newer image for python:3.7-alpine
Creating django_postgres_db_1 ... done
Creating django_postgres_web_1 ... done

```

## Expected Result

Listing containers must show two containers running and the port mapping for the web service as below:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
3adaea94142d        django_postgres_web "python3 manage.py r…"   About a minute ago  Up About a minute   0.0.0.0:8000->8000/tcp   django_postgres_web_1
e8af03d3b6a1        postgres            "docker-entrypoint.s…"   About a minute ago  Up About a minute   5432/tcp                 django_postgres_db_1
```

After the application starts, navigate to `http://localhost:8000` in your web browser.

Stop and remove the containers and the network:
```
$ docker compose down
```

---

This README provides a guide for setting up and running a Django application with a PostgreSQL database using Docker Compose. Remember to adjust the database credentials in the `.env` file as needed, especially for production environments.