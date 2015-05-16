Isomorphic javascript powered by python-react 
=============================================

A basic isomorphic JavaScript application with [React](http://facebook.github.io/react/), 
and [Django](https://www.djangoproject.com/).

The example App here is adapted from the [Smashing Magazine Ariticle](http://www.smashingmagazine.com/2015/04/21/react-to-the-future-with-isomorphic-apps/),
but using the [python-react example](https://github.com/markfinger/python-react/tree/master/example).


Install
-------

1. Create a virtual environment for the example

        virtualenv pydev
        source pydev/bin/activate

2. Install the project's python dependencies:

        pip install -r requirements.txt

3. Install the project's JS dependencies (assumes you already have node installed):

        npm install .



Run
---

Start the django devserver

    ./manage.py runserver


And visit [http://127.0.0.1:8000](http://127.0.0.1:8000)


