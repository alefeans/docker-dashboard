# Docker Dashboard
[![Build Status](https://travis-ci.org/alefeans/docker_dashboard.svg?branch=master)](https://travis-ci.org/alefeans/docke_dashboard) [![Python](https://img.shields.io/badge/python-3.7-blue.svg)]() [![Python](https://img.shields.io/badge/python-3.6-blue.svg)]() [![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE)

A simple Dashboard to manage your **Docker** containers and images !

![](/imgs/dashboard_usage.gif)

# Getting Started

## Installing

To install the _Docker Dashboard_ you will need to:

```
git clone https://github.com/alefeans/docker-dashboard.git && cd docker-dashboard
pip install -r requirements.txt
```

## Usage

Start your Docker engine (e.g in Fedora: `systemctl start docker`), use one of the options to start the Docker Dashboard below and open your browser on `localhost:8000`:

### Development

```
python manage.py runserver
```

### Production

```
gunicorn  -b :8000 -w 3 --access-logfile - --error-logfile - docker_dashboard.wsgi:application
```

## Docker

To use the Docker image, you'll need to _bind_ your Docker unix socket `/var/run/docker.sock` in a volume:

```
# Builds the image
docker build -t docker_dashboard .

# And starts a new container
docker run -d -p 8000:8000 \
-v /var/run/docker.sock:/var/run/docker.sock \
--name docker_dashboard \
docker_dashboard
```

## To Do

- Include unit tests.
- Add Docker multi-stage builds.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
