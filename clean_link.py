import pandas as pd
import re

df_name = './code_generation_models.csv'

df = pd.read_csv(df_name)

def extract_links_or_names(text):
    # Ensure the input is a string, otherwise return an empty string
    if isinstance(text, str):
        # Use regex to find full links starting with https://arxiv.org/abs/ or https://arxiv.org/pdf/
        links_or_names = re.findall(r'(https://arxiv.org/(abs|pdf)/\d+\.\d+(?:v\d+)?)', text)
        # Extract the full match from the tuple and return
        return ' '.join([link[0] for link in links_or_names])
    else:
        return pd.NA


# Apply the function to the 'paper_code' column
df['paper_code_clean'] = df['paper_code'].apply(extract_links_or_names)

df.to_csv(df_name, index=False)
