import unittest
from flask_mongo_sdk.client import FlaskMongoSDK

class TestFlaskMongoSDK(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sdk = FlaskMongoSDK(base_url='http://localhost:5000')

    def test_get_all_users(self):
        response = self.sdk.get_all_users()
        self.assertIsInstance(response, list)

    def test_create_user(self):
        response = self.sdk.create_user(name='testuser', email='test@example.com')
        self.assertIn('id', response)

    def test_get_user_by_id(self):
        created_user = self.sdk.create_user(name='testuser2', email='test2@example.com')
        user_id = created_user['id']
        response = self.sdk.get_user_by_id(user_id=user_id)
        self.assertEqual(response['name'], 'testuser2')

    def test_update_user(self):
        created_user = self.sdk.create_user(name='testuser3', email='test3@example.com')
        user_id = created_user['id']
        updated_user = self.sdk.update_user(user_id=user_id, name='updateduser')
        self.assertEqual(updated_user['msg'], 'User Updated Successfully')

    def test_delete_user_by_id(self):
        created_user = self.sdk.create_user(name='testuser4', email='test4@example.com')
        user_id = created_user['id']
        response = self.sdk.delete_user_by_id(user_id=user_id)
        self.assertEqual(response['msg'], 'User Deleted Successfully')

if __name__ == '__main__':
    unittest.main()
