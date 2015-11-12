import logging
import requests

import pylons.config as config

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.external_id.interfaces import IExternalIDProvider

log = logging.getLogger(__name__)

class GooglPlugin(plugins.SingletonPlugin):
    plugins.implements(IExternalIDProvider)

    def get_external_id(self, context):
        ckan_url = context['package'].as_dict()['ckan_url']
        log.info('shortening %s' % ckan_url)
        key = config.get('ckanext.googl.api_key')
        api_url = 'https://www.googleapis.com/urlshortener/v1/url?key=%s' % key
        r = requests.post(api_url,
                          json = {'longUrl': ckan_url},
                          headers = {'Content-Type':'application/json'})
        log.info('UrlShortener reply: %s' % r.json())
        return r.json()['id']

    def get_pretty_name(self):
        return "goo.gl"