# 23Z PZSP2

---

## About the project 
The aim of the project is to create a system to support the organization of bicycle races in league format. The system should support organizers in organizing races and users in participating in races.
Organizers define a league as a series of short races of 2-3 laps on a track in the form of loops, from which results are collected and aggregated over the course of about 10 races. This makes it possible to determine which participant is the best.

This is the main project repository. 
- For backend, visit [this repo](https://github.com/SNURTEL/sigmacats-backend)
- Web Flutter app is available [here](https://github.com/SNURTEL/sigmacats-web)
- If you are looking for the mobile app, check [here](https://github.com/SNURTEL/sigmacats-mobile).

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
to copy the default envfile, login to Oracle Container Image Repository, update git submodules and setup Cloudbeaver.

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

### Wipe the DB
```shell
./cleanup.sh
```

## Try it out

Although the app's not doing much for now, you can check some basic tools that may come in handy later:
- App runs at [port 80](http://localhost)
- API documentation is available at [/docs](http://localhost/docs)
- Cloudbeaver is available at [/cloudbeaver](http://localhost/cloudbeaver)
  - Use default credentials to log in
- Celery worker is running by default. Check [/celery](http://localhost/celery) to schedule a simple 3-second task.
  - To see available workers, current tasks and the message queue, check Flower at [/flower](http://localhost/flower)
- To check if DB connection is working, visit [/db](http://localhost/db). Response should contain all account in DB 
  (by default - one account).

## Default configuration
Default config is stored in `.env.sample`. Default credentials included:

| Type                                     | Username                    | Password         |
|------------------------------------------|-----------------------------|------------------|
| Dummy rider account                      | `rider@default.sigma`       | `rider123`       |
| Dummy coordinator account                | `coordinator@default.sigma` | `coordinator123` |
| Dummy admin account                      | `admin@default.sigma`       | `admin123`       |
| Oracle DB admin                          | `system`                    | `oracle`         |
| Oracle user                              | `user1`                     | `user1`          |
| Cloudbeaver admin                        | `rootbeaver`                | `cloudbeaver`    |
| Cloudbeaver user (currently unavailable) | `user1`                     | `user1`          |

**In you're running in production, remember to change those!**

### Documentation
- Non-technical project documentation is available on [project Google Drive](https://drive.google.com/drive/folders/1Zp6dHEMV8WkCuym4bZPDuKnoiORsDU2a).
- API documentation is available at [/docs](http://localhost/docs) 

### Contributing
- Project development is managed in a GitHub project [issue board](https://github.com/users/SNURTEL/projects/1/views/1)
- For code structure and task workflow description check [CONTRIBUTING.md](CONTRIBUTING.md)
- [Backend README.md](backend/README.md)
