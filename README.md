Isomorphic javascript powered by django-react 
=============================================

A basic isomorphic JavaScript application with [React](http://facebook.github.io/react/), 
and [Django](https://www.djangoproject.com/).

The example App here is adapted from the [Smashing Magazine Ariticle](http://www.smashingmagazine.com/2015/04/21/react-to-the-future-with-isomorphic-apps/),
and heavily inspired by the [django-react example](https://github.com/markfinger/django-react/tree/master/example).



Install
-------

```bash
# Create a virtual environment for the example
virtualenv pydev
source pydev/bin/activate

# Install the project's python dependencies
pip install -r requirements.txt

# Install the project's JS dependencies
./manage.py install_package_dependencies
```



Run
---


```bash
# Start the node server that we use to render and bundle components
./manage.py start_node_server

# In another shell, start the django devserver
./manage.py runserver
```

And visit [http://127.0.0.1:8000](http://127.0.0.1:8000)


