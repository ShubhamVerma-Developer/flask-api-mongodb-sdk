from setuptools import setup, find_packages

setup(
    name='flask_mongo_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    description='Python SDK for interacting with a Flask app using MongoDB',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/ShubhamVerma-Developer/flask-api-mongodb-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
