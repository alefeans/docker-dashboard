import logging
from json.decoder import JSONDecodeError
from requests_unixsocket import Session
from requests import RequestException
from docker_dashboard.settings import DOCKER_API

logger = logging.getLogger(__name__)


def docker_requester(func):
    def wrapper(*args, **kwargs):
        method, endpoint, data = func(*args, **kwargs)
        session = Session()
        try:
            call = getattr(session, method)
        except (AttributeError, TypeError):
            logger.error("Method '{}' does not exists in Session object".format(method))
            return False

        try:
            resp = call(DOCKER_API + endpoint, json=data, timeout=30)
        except RequestException as e:
            logger.error('Docker API request failed: {}'.format(e))
            return False

        logger.debug('Docker API response: {}, {}'.format(resp.status_code, resp.text))

        if resp.status_code == 204:
            return True
        if resp.status_code == 201 or resp.status_code == 200:
            try:
                return resp.json()
            except JSONDecodeError:
                return True
        return {}

    return wrapper


@docker_requester
def list_container():
    return 'get', 'containers/json?all=true', None


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
    endpoint = 'images/{}'.format(image)
    return 'delete', endpoint, None


@docker_requester
def pull_image(image, tag):
    if not tag:
        tag = 'latest'
    endpoint = 'images/create?fromImage={}&tag={}'.format(image, tag)
    return 'post', endpoint, None
