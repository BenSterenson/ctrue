import logging

logger = logging.getLogger('micro_service')


def post_greeting(name):
    return 'Hello {name}'.format(name=name)