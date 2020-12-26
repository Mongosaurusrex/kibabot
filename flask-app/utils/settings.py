from os import environ
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

MONGODB_CONNECTION_STRING = environ.get('MONGODB_CONNECTION_STRING')
