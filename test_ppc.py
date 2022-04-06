import ppc
import unittest


class PpcTestCase(unittest.TestCase):
    def setUp(self):
        ppc.app.testing = True
        self.app = ppc.app.test_client()

    def test_items(self):
        result = self.app.post('/items', data="[{'a':1}, {'b':2}, {'c':'third'}]")
        self.assertEqual(result,'post complete')

        result = self.app.get('/items')
        self.assertEqual(result, "[{'a':1}, {'b':2}, {'c':'third'}]")

        result = self.app.delete('/items')
        self.assertEqual(result, 'items have been discarded')

        result = self.app.get('/items')
        self.assertEqual(result, 'no items')
        
