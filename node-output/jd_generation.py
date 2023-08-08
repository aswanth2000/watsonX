import os
import pandas as pd
from genai.credentials import Credentials
from genai.schemas import GenerateParams
from genai.model import Model
from dotenv import load_dotenv

load_dotenv()
api_key = "pak-J3FKwlwCdeZY63Fomc4ybzNkHGsskrT6IAseMH4Hz8s"
api_url = "https://bam-api.res.ibm.com/v1/"
#url="https://us-south.ml.cloud.ibm.com"
creds = Credentials(api_key=api_key, api_endpoint=api_url)
params = GenerateParams(decoding_method="greedy", min_new_tokens=1, max_new_tokens=500)
model = Model("google/flan-t5-xxl", params=params, credentials=creds)

# prompt = "Generate a 100 sentence job offer letter for a user experience designer with the following characteristics:\nCompany - IBM\nlocation - London\nEducation - Bachelors in User Experience Design\ - User experience for consumer and business applications\nRequired Skills - Ability to understand business metrics and translate company goals and objectives into digital experiences; Excellent interpersonal and communication skills to communicate ideas to developers; Knowledge of industry tools like Adobe, Zeplin, OmniGraffle, Illustrator and Sketch;Problem-solving skills to determine solutions to user interface challenges; Multi-tasking and time management skills, with the ability to prioritize tasks; Analytical mind with business acumen; Ability to work both independently and in a team; Attention to detail and mastery of information design\n\n"
# response = model.generate([prompt])
# print(response[0].generated_text)
def generat(prompt):
    response = model.generate([prompt])
    return response[0].generated_text