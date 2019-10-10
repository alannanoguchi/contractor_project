from unittest import TestCase, main as unittest_main
from app import app

class InventoryTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True



    def test_index(self):
        """Test the homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Collections', result.data)   


    def test_inventory(self):
        """Test the new playlist creation page."""
        result = self.client.get('/inventory')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Inventory', result.data) 

if __name__ == '__main__':
    unittest_main()