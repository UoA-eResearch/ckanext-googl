=============
ckanext-googl
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

This extension provides an interface to `goo.gl
<https://goo.gl/>`_ for `ckanext-external_id
<https://github.com/UoA-eResearch/ckanext-external_id>`_.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-googl:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-googl Python package into your virtual environment::

     cd src
     git clone https://github.com/UoA-eResearch/ckanext-googl.git
     cd ckanext-googl
     python setup.py develop
     
3. Add ``googl`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Set your goo.gl API key with the key ckan.googl_api_key in your CKAN config
   file

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

