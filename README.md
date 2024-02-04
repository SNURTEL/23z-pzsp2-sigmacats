# Bicycle league  racing 
### 23Z PZSP2

---

## About the project 
The aim of the project was to create a system for organizing and conducting bicycle races in league format. 


This is the main project repository. 
- For backend, visit [this repo](https://github.com/SNURTEL/sigmacats-backend)
- Flutter web app is available [here](https://github.com/SNURTEL/sigmacats-web)
- If you are looking for the mobile app, check [here](https://github.com/SNURTEL/sigmacats-mobile).

#### SIGMACATS team:
- Jakub Jóźwiak
- Miłosz Mizak
- Tomasz Owienko
- Anna Schäfer

## Built with
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D) ![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white) ![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white) ![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Dependabot](https://img.shields.io/badge/dependabot-025E8C?style=for-the-badge&logo=dependabot&logoColor=white) 

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
to copy the default envfile, login to Oracle Container Image Repository, update git submodules and setup Cloudbeaver. Most of the app should be good to go, but some variables may need adjustment in `.env` - for example, password reset functionality will not work without setting SMTP sever details.

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

- App runs at [port 80](http://localhost)
- API documentation is available at [/api/docs](http://localhost/api/docs)
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
| Dummy rider account 1                    | `firstrider@default.sigma`  | `rider123`       |
| Dummy rider account 2                    | `secondrider@default.sigma` | `rider123`       |
| Dummy coordinator account                | `coordinator@default.sigma` | `coordinator123` |
| Dummy admin account                      | `admin@default.sigma`       | `admin123`       |
| Oracle DB admin                          | `system`                    | `oracle`         |
| Oracle user                              | `user1`                     | `user1`          |
| Cloudbeaver admin                        | `rootbeaver`                | `cloudbeaver`    |

**In you're running in production, remember to change those!**

### Documentation
- Non-technical project documentation is available on [project Google Drive](https://drive.google.com/drive/folders/1Zp6dHEMV8WkCuym4bZPDuKnoiORsDU2a).
- API documentation is available at [/api/docs](http://localhost/api/docs) 

### Contributing
- Project development is managed in a GitHub project [issue board](https://github.com/users/SNURTEL/projects/1/views/1)
- For code structure and task workflow description check [CONTRIBUTING.md](CONTRIBUTING.md)
- [Backend README.md](backend/README.md)
