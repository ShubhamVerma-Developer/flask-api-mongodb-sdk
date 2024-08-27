import requests

class FlaskMongoSDK:
    def __init__(self, base_url):
        """
        Initialize the SDK with the base URL of the Flask application.
        
        :param base_url: Base URL of the Flask API (e.g., 'http://localhost:5000')
        """
        self.base_url = base_url

    def get_all_users(self):
        """
        Retrieve all users from the Flask application.
        
        :return: A list of users in JSON format.
        """
        url = f"{self.base_url}/api/users"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def create_user(self, name, email, contact=None, address=None):
        """
        Create a new user.
        
        :param name: The name of the new user.
        :param email: The email of the new user.
        :param contact: The contact information of the new user.
        :param address: The address of the new user.
        :return: The response JSON containing the new user data.
        """
        url = f"{self.base_url}/api/users"
        data = {
            'name': name,
            'email': email,
            'contact': contact,
            'address': address
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_user_by_id(self, user_id):
        """
        Retrieve a user by ID.
        
        :param user_id: The ID of the user to retrieve.
        :return: The response JSON containing the user data.
        """
        url = f"{self.base_url}/api/user/{user_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id, name=None, email=None, contact=None, address=None):
        """
        Update an existing user's information.
        
        :param user_id: The ID of the user to update.
        :param name: The new name for the user.
        :param email: The new email for the user.
        :param contact: The new contact information for the user.
        :param address: The new address for the user.
        :return: The response JSON containing the updated user data.
        """
        url = f"{self.base_url}/api/users/{user_id}"
        data = {
            'name': name,
            'email': email,
            'contact': contact,
            'address': address
        }
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete_user_by_id(self, user_id):
        """
        Delete a user by ID.
        
        :param user_id: The ID of the user to delete.
        :return: The response JSON confirming deletion.
        """
        url = f"{self.base_url}/api/users/{user_id}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()
