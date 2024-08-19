import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    def test_jenkins_working_page(self):
        response = self.client.get('/jenkins_working')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'How Jenkins Works', response.data) 

    def test_jenkins_uses_page(self):
        response = self.client.get('/jenkins_uses')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Uses of Jenkins', response.data) 

    def test_jenkins_architecture_page(self):
        response = self.client.get('/jenkins_architecture')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jenkins Architecture', response.data)

    def test_jenkins_pipeline_page(self):
        response = self.client.get('/jenkins_pipeline')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jenkins Pipeline', response.data)

    def test_non_existing_page(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

#main 
if __name__ == '__main__':
    unittest.main()

