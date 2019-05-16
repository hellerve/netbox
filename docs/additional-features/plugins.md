# Plugins

If you’re a software developer looking to add features to Netbox that might not
find a place in core, you might be interested in plugins. Plugins are simple
extensions to Netbox that cann add new models, widgets, and even middleware.

Each plugin is a Django app that may depend on Netbox internals. It provides a
class that implements `Plugin` from `netbox.plugins`. It could look like this:

```python
from netbox.plugins import registry, Plugin

class MyPlugin(Plugin):
    """
    The only function a plugin really **needs** to implement is `namespace`.
    """
    def namespace(self):
        """
        this will be the URL namespace that your URLs will find themselves
        inside of
        """
        return 'mine'

    def urls(self):
        """
        These are the URLs that you export. We advise you to load them lazily,
        since Django might not be ready yet when this module gets loaded.
        """
        from mymodule import urls
        return urls.urlpatterns

    def navbar_elements(self):
        """
        This is arbitrary HTML that will be inlined into the navigation bar.
        """
        return ['mymodule/navbar.html']

    def widgets(self):
        """
        This is arbitrary HTML that will be inlined into the list of widgets.
        """
        return ['mymodule/widget.html']

registry.register(MyPlugin())
```

And that’s it! The rest is up to you and Django to figure out. If you need a
template to get started, you might want to look at [this Github repository](#todo).
