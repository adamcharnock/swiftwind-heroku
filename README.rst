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

The following addons will be setup (on the free plan of each):

  * Postgres
  * Redis

Dokku
~~~~~

This project is also designed to support deployment to dokku. You can do so as follows:

    dokku apps:create swiftwind
    dokku config:set SECRET_KEY=random-string
    dokku config:set DATABASE_URL=postgres://user:password@host/dbname
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
