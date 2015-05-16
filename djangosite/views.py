import os

from django.shortcuts import render
from django.conf import settings

from react.render import render_component


def index(request):
    # Render the App component down to HTML
    markup = render_component(
        # Abs Path required
        os.path.join(settings.BASE_DIR, 'djangosite', 'static', 'components/App.jsx'),

        # We can pass data along to the component which will be
        # accessible from the component via its `this.props` property
        props={
            'comment': 'This is state passed from py to js',
        },

        # Ensure that the source code is translated to JS from JSX & ES6/7.
        # This enables us to use future-facing JS in across the client-side
        # and server-side
        translate=True,
    )

    return render(request, 'index.html', {
        'title': 'Example App',
        'markup': markup,
    })    
    
