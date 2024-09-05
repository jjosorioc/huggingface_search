from huggingface_hub import HfApi, ModelCard
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import re

api = HfApi()



# List models with card data sorted by downloads in descending order
models = api.list_models(cardData=True, sort='downloads', direction=-1, limit=40000)

# Define relevant words for filtering
words = [
    "software engineering", "software development", "software", 
    "engineering", "development", "programming",
    "developer", "software developer", "software engineer", 
    "web development", "web developer", "web", "web design",
    "web designer", "code", "coding", "MLOps", "DevOps"
]

# Prepare list to hold data for the dataframe
data = []

# Function to process each model
def process_model(model):
    contains_paper = False
    if any("arxiv" in tag for tag in model.tags):
        contains_paper = True
    
    try:
        # Skip models with 0 downloads
        if model.downloads == 0:
            return None
        
        # Load the model card
        model_card = ModelCard.load(model.id)
        
        # Check if any relevant word is in the model card content
        for word in words:
            if word in model_card.content:
                # Extract the text that contains "arxiv" between white spaces
                arxiv_code_match = re.search(r'\S*arxiv\S*', model_card.content)
                paper_code = arxiv_code_match.group(0) if arxiv_code_match else None
                
                return {
                    "Model Name": model.id,
                    "Matching Word": word,
                    "Downloads": model.downloads,
                    "contains_paper": ("arxiv" in model_card.content or "paper" in model_card.content) or contains_paper,
                    "paper_code": paper_code
                }
    except Exception:
        return None

# Use ThreadPoolExecutor to process models concurrently
with ThreadPoolExecutor(max_workers=12) as executor:
    futures = [executor.submit(process_model, model) for model in models]
    
    # As completed threads return, collect the results
    for future in as_completed(futures):
        result = future.result()
        if result:
            data.append(result)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(data, columns=["Model Name", "Matching Word", "Downloads", "contains_paper", "paper_code"])

# Save DataFrame to Excel
output_file = "software_engineering_models.xlsx"
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")