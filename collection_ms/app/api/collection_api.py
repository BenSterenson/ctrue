import logging

logger = logging.getLogger('micro_service')


def get_greeting(name):
    return 'Hello {name}'.format(name=name)
