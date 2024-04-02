from dotenv import load_dotenv
import os
# load_dotenv()

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path)

user_db = os.environ.get('USER_DB')
paswor_db = os.environ.get('PASWOR_DB')