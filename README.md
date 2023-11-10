# 23Z PZSP2

---

## About the project 
Put some fancy description here.

This is the main project repository. If you are looking for the mobile app, check [here](https://cat-bounce.com/).

#### SIGMACATS team:
- Jakub Jóźwiak
- Miłosz Mizak
- Tomasz Owienko
- Anna Schäfer

## Built with
- FastAPI for backend
- Oracle Database for persistence
- Celery and Redis for task management
- Docker and Docker Compose for containerization
- GitHub Actions for CI

## Getting started

Get the project up & running with Docker.

### Prerequisites
- Docker Compose to run the containers
  - [Docker](https://docs.docker.com/engine/install/)
  - [Docker compose](https://docs.docker.com/compose/install/)
- An Oracle account to pull the DB container image
  - [Create one here](https://profile.oracle.com/myprofile/account/create-account.jspx)
- A Linux host

### Setup 
```shell
chmod +x setup.sh
./setup.sh
```
to copy the default envfile and login to Oracle Container Image Repository.

### Build
```shell
docker compose build
```
to build container images. You can also specify `--build-arg BUILD_ENV=(development|test|production)` to use a specific build config.

### Run
After building the containers, run:
```shell
docker compose up
```
or 
```shell
docker compose up --detach
```
to run in detached mode.

### Run tests
```shell
docker compose up --detach
docker exec fastapi-backend "pytest"
```

## Try it out

Although the app's not doing much for now, you can check some basic tools that may come in handy later:
- App runs at [port 8000](localhost:8000)
- API documentation is available at [/docs](localhost:8000/docs)
- Cloudbeaver is available at [port 8080](localhost:8080)
  - For now, the DB connection has to be set up manually (only for the first time). Use SID `FREE`, port 1521 and 
    default credentials.
- Celery worker is running by default. Check [/celery](localhost:8000/celery) to schedule a simple 3-second task.
  - To see available workers, current tasks and the message queue, check Flower at [port 5555](localhost:5555)
- To check if DB connection is working, visit [/db](localhost:8000/db). The response should contain some scary 
  looking Oracle table names.

## Default configuration
Default config is stored in `.env.sample`. Default credentials included:

| Type            | Username | Password |
|-----------------|----------|----------|
| Oracle DB admin | `system`  | `oracle`  |
| Oracle user (currently unavailable) | `user1` | `user1` |
| Cloudbeaver admin | `rootbeaver` | `cloudbeaver` |
| Cloudbeaver user (currently unavailable) | `user1` | `user1` |

**In you're running in production, remember to change those!**

### Documentation
Non-technical project documentation is available on [project Google Drive](https://drive.google.com/drive/folders/1Zp6dHEMV8WkCuym4bZPDuKnoiORsDU2a).

### Contributing
- Project development is managed in a [GitLab Issue Board](https://gitlab-stud.elka.pw.edu.pl/towienko/23z-pzsp2-sigmacats/-/boards/1050) (not anymore!)
- For code structure and task workflow description check [CONTRIBUTING.md](CONTRIBUTING.md)

