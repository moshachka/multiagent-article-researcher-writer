import warnings
warnings.filterwarnings("ignore")

from crewai import Agent, Task, Crew

import os
from utils import get_openai_api_key

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

