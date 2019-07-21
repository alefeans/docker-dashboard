# Docker Dashboard
[![Python](https://img.shields.io/badge/python-3.7-blue.svg)]() [![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE)

A simple Dashboard to manage your **Docker** containers and images !

# Getting Started

## Installing

To install the _Docker Dashboard_ you will need to:

```
git clone https://github.com/alefeans/docker_dashboard.git .
pip install -r requirements.txt
```

## Usage

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
- Search bar to pull new Docker images from Docker Hub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
