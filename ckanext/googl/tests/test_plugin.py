"""Tests for plugin.py."""
import ckanext.googl.plugin as plugin
import pylons.config as config

class StubPackageContext():
    dict = {}
    def as_dict(self):
        return self.dict
    def set_url(self, url):
        self.dict['ckan_url'] = url

def test_plugin():
    api_key = config.get('ckanext.googl.api_key')
    assert api_key is not None and api_key is not 'API_KEY'
    context = {'package': StubPackageContext()}
    context['package'].set_url('https://github.com/UoA-eResearch/ckanext-googl')
    instance = plugin.GooglPlugin()
    external_id = instance.get_external_id(context)
    assert 'https://goo.gl/' in external_id
    assert instance.get_pretty_name() == 'goo.gl'