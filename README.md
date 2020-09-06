# fastapi-tdd-docker
Learn how to build, test, and deploy a text summarization microservice with Python, FastAPI, and Docker


## Table of Contents

- [About](#about)
- [Built With](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contributing](#contributing)

## About

**fastapi-tdd-docker** is a code-along (with minor differences) to the course **[Test-Driven Development with FastAPI and Docker][tddfastapi]** by Michael Herman.

### Built With

- Docker & Docker Compose
- [FastAPI](https://fastapi.tiangolo.com/)

## Installation

#### Prerequisites:

- Python 3.8+
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

#### 1. Clone the repository:

```bash
$ git clone https://github.com/imtanmoy/fastapi-tdd-docker.git && cd fastapi-tdd-docker
```

#### 2. Use Docker and Docker Compose

```bash
$ docker-compose up -d --build
```

#### 3. Apply Migrations

```bash
$ docker-compose exec web python app/db.py
```

## Usage

```bash
$ docker-compose up -d
```

Go to [`http://localhost:8002/docs`](http://localhost:8002/docs).

## Tests

```bash
$ docker-compose exec web python -m pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please see the [original repo](https://github.com/testdrivenio/fastapi-tdd-docker) for details.

[tddfastapi]: https://testdriven.io/courses/tdd-fastapi/
