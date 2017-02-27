Swiftwind for Heroku Deployment
===============================

.. image:: https://badge.fury.io/py/swiftwind-heroku.png
    :target: https://badge.fury.io/py/swiftwind-heroku

.. image:: https://pypip.in/d/swiftwind-heroku/badge.png
    :target: https://pypi.python.org/pypi/swiftwind-heroku

For more details see the `Swiftwind project`_.

Installation
------------

.. image:: https://www.herokucdn.com/deploy/button.svg
    :target: https://heroku.com/deploy?template=https://github.com/adamcharnock/swiftwind-heroku

Environment variables::

    # Should be setup automatically for you:
    SECRET_KEY='<a random value>'
    DATABASE_URL='postgres://user:pasword@host/dbname'

    # If you are using HTTPS you may wish to set the following yourself:
    HTTPS=1  # Will ensure site is served over HTTPS only
    HSTS_SECONDS=100000  # Will enable HSTS, and set the seconds timeout
    HSTS_INCLUDE_SUBDOMAINS=1  # Apply HSTS to subdomains

Required Heroku Addons
~~~~~~~~~~~~~~~~~~~~~~

The following addons will be setup (on the free plan of each):

  * Postgres
  * Redis

Credits
-------

*Any credits here*

swiftwind-heroku is packaged using seed_.

.. _seed: https://github.com/adamcharnock/seed/
.. _Swiftwind project: https://github.com/adamcharnock/swiftwind
