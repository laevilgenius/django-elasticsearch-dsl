from django.utils.module_loading import autodiscover_modules

from .documents import DocType  # noqa
from .indices import Index  # noqa
from .fields import *  # noqa

__version__ = '7.0.0'


def autodiscover():
    autodiscover_modules('documents')


default_app_config = 'django_elasticsearch_dsl.apps.DEDConfig'
