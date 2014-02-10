Facebook Flask Demo App
=============

This is an example Flask application to demonstrate how to use the Facebook API. It's
pretty simple, and has the user log in with Facebook and displays their friends.
Written in Python, designed for deployment to Heroku: http://www.heroku.com/

Run locally
-----------

Set up a Virtualenv and install dependencies::

    virtualenv --no-site-packages env/
    source env/bin/activate
    pip install -r requirements.txt

`Create an app on Facebook`_ and set the Website URL to
``http://localhost:5000/``.

Copy the App ID and Secrets from the Facebook app settings page into
your ``.env``::

    echo FACEBOOK_APP_ID=12345 >> .env
    echo FACEBOOK_SECRET=abcde >> .env
    echo SECRET_KEY='secret' >> .env

Launch the app with Foreman_::

    foreman start

.. _Create an app on Facebook: https://developers.facebook.com/apps
.. _Foreman: http://blog.daviddollar.org/2011/05/06/introducing-foreman.html

Deploy to Heroku
----------------

Push this code to a new Heroku app on the Cedar stack, then copy the App ID and
Secrets into your config vars::

    heroku create --stack cedar
    git push heroku master
    heroku config:add FACEBOOK_APP_ID=12345 FACEBOOK_SECRET=abcde
    heroku config_add SECRET_KEY='secret'

Enter the URL for your Heroku app into the Website URL section of the
Facebook app settings page, hen you can visit your app on the web.
