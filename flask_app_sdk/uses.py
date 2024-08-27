from flask_mongo_sdk.client import FlaskMongoSDK

sdk = FlaskMongoSDK(base_url='http://localhost:5000')




# Get all users
users = sdk.get_all_users()


# Create a user
new_user = sdk.create_user(name='exampleuser1', email='example@example.com1', contact='1231654654654', address='ahmedabad')

print(new_user)
print(users)

# Get user details
user_details = sdk.get_user_by_id(user_id=new_user['id'])

print(user_details)

# # Update user
# updated_user = sdk.update_user(user_id=new_user['id'], name='newname')

# # Delete user
# delete_response = sdk.delete_user_by_id(user_id=new_user['id'])
