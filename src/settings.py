from dotenv import load_dotenv
import os

load_dotenv()

BATCH_SIZE = int(os.getenv("BATCH_SIZE"))

OMETRIA_URL = os.getenv("OMETRIA_URL")
API_KEY_OMETRIA = os.getenv("API_KEY_OMETRIA")

MAILCHIMP_SERVER = os.getenv("MAILCHIMP_SERVER")
API_KEY_MAILCHIMP = os.getenv("API_KEY_MAILCHIMP")
