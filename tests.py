from django.test import TestCase

class ClientTest(TestCase):

    def testGET(self):
        # Create an instance of a GET request.
        response = self.client.get('/api/add/')
        self.assertEqual(response.status_code, 200)
