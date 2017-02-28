Swiftwind for Heroku Deployment
===============================

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

The free plan for each of the following addons will be setup:

* Postgres
* Redis

Dokku
~~~~~

This project is also designed to support deployment to dokku. To do so you will need:

* A Postgres database (See `Postgres Dokku plugin`_)
* A Redis server (`Redis Dokku plugin`_)

You can deploy as follows::

    # Get the repo
    git clone https://github.com/adamcharnock/swiftwind-heroku.git
    cd swiftwind-heroku

    # Create the app and set the config
    dokku apps:create swiftwind
    dokku config:set SECRET_KEY=random-string

    dokku postgres:create swiftwind
    dokku postgres:link swiftwind swiftwind

    dokku redis:create swiftwind
    dokku redis:link swiftwind swiftwind

    git push dokku
    dokku run ./manage.py migrate
    # Create a user you will use to login as
    dokku run ./manage.py createsuperuser
    # Set currency as you wish (GBP, EUR, USD etc)
    dokku run ./manage.py create_chart_of_accounts --currency USD

Credits
-------

Developed by `Adam Charnock`_. I'm a freelance developer, so do get in touch if you have a project.

swiftwind-heroku is packaged using seed_.

.. _seed: https://github.com/adamcharnock/seed/
.. _Swiftwind project: https://github.com/adamcharnock/swiftwind
.. _Postgres Dokku plugin: https://github.com/dokku/dokku-postgres
.. _Redis Dokku plugin: https://github.com/dokku/dokku-redis
.. _Adam Charnock: https://adamcharnock.com
