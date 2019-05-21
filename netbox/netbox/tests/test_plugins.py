from django.test import TestCase
from netbox.plugins import Plugin, PluginRegistry


class TestPlugin(Plugin):
    def namespace(self):
        return 'test'

    def navbar_elements(self):
        return ['test/navbar.html']

    def widgets(self):
        return ['test/widget.html']

    def urls(self):
        return ['testurl']


class AnimalTestCase(TestCase):
    def setUp(self):
        self.plugin = TestPlugin()
        self.registry = PluginRegistry()

    def test_registering_plugins(self):
        self.assertEqual(len(self.registry.plugins), 0)
        self.registry.register(self.plugin)
        self.assertEqual(len(self.registry.plugins), 1)
        self.registry.unregister(self.plugin)
        self.assertEqual(len(self.registry.plugins), 0)

    def test_initial_registry_behavior(self):
        self.assertEqual(self.registry.urls(), [])
        self.assertEqual(self.registry.navbar_elements(), [])
        self.assertEqual(self.registry.widgets(), [])

    def test_adding_plugins_to_registry(self):
        self.registry.register(self.plugin)

        self.assertEqual(self.registry.navbar_elements(), ['test/navbar.html'])
        self.assertEqual(self.registry.widgets(), ['test/widget.html'])
        # we registered one url resolver, but theyre hard to match against
        # lets just assume its the right one for now
        self.assertEqual(len(self.registry.urls()), 1)

        self.registry.unregister(self.plugin)
