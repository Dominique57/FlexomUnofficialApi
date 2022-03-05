import os
from dotenv import load_dotenv

load_dotenv()

USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASS = os.environ.get("USER_PASS")
