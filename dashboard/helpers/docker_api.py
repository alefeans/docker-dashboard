import logging
from requests_unixsocket import Session
from requests import RequestException
from docker_dashboard.settings import DOCKER_API

logger = logging.getLogger(__name__)


def docker_requester(func):
    def wrapper(*args, **kwargs):
        method, endpoint, data = func(*args, **kwargs)
        print(endpoint)
        session = Session()
        try:
            call = getattr(session, method)
        except (AttributeError, TypeError):
            logger.error("Method '{}' does not exists in Session object".format(method))

        try:
            resp = call(DOCKER_API + endpoint, json=data, timeout=30)
        except RequestException as e:
            logger.error('Docker API request failed: {}'.format(e))

        logger.debug('Docker API response: {}, {}'.format(resp.status_code, resp.text))

        if resp.status_code == 204:
            return True
        if resp.status_code == 201 or resp.status_code == 200:
            return resp.json()
        return {}

    return wrapper


@docker_requester
def list_container():
    return 'get', 'containers/json?all=True', None


@docker_requester
def start_container(container):
    endpoint = 'containers/{}/start'.format(container)
    return 'post', endpoint, None


@docker_requester
def stop_container(container):
    endpoint = 'containers/{}/stop'.format(container)
    return 'post', endpoint, None


@docker_requester
def create_container(image):
    return 'post', 'containers/create', image


@docker_requester
def delete_container(container):
    endpoint = 'containers/{}?force=True'.format(container)
    return 'delete', endpoint, None


@docker_requester
def list_image():
    return 'get', 'images/json', None


@docker_requester
def delete_image(image):
    endpoint = 'images/{}?force=True'.format(image)
    return 'delete', endpoint, None
