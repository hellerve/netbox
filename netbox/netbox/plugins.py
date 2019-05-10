from django.conf.urls import url, include

class PluginUrls:
    def __init__(self, name, urls):
        self.app_name = name
        self.urlpatterns = urls


class PluginRegistry:
    def __init__(self):
        self.plugins = set()

    def register(self, plugin):
        self.plugins.add(plugin)

    def navbar_elements(self):
        return [elem for p in self.plugins for elem in p.navbar_elements()]

    def widgets(self):
        return [elem for p in self.plugins for elem in p.widgets()]

    def urls(self):
        return [
            url(r'^{}/'.format(p.namespace()), include(PluginUrls(p.namespace(), p.urls())))
            for p in self.plugins
        ]


registry = PluginRegistry()


class Plugin:
    def namespace(self):
        return None

    def navbar_elements(self):
        return []

    def widgets(self):
        return []

    def urls(self):
        return []
