from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from huggingface_hub import HfApi, ModelCard
import pandas as pd

api = HfApi()

# Define relevant words for filtering
words = [
    "code generation", "code-generation", "codegeneration", "code-gen", "code gen", "code-gen", "codegen",
]

# List models with card data sorted by downloads in descending order
models = api.list_models(cardData=True, sort='downloads', direction=-1, limit=40000)  # Adjusted limit for performance

# Prepare list to hold data for the dataframe
data = []

# Function to process each model
def process_code_generation_model(model):
    try:
        # Skip models with 0 downloads
        if model.downloads == 0:
            return None
        
        # Convert tags to lowercase
        model_tags_lower = [tag.lower() for tag in model.tags]
        
        # Check if 'arxiv' is in tags or card content to set contains_paper
        contains_paper = any("arxiv" in tag for tag in model_tags_lower)
        
        # Load the model card
        model_card = ModelCard.load(model.id)
        
        # Check if any relevant word is in the model card content or tags
        for word in words:
            word_lower = word.lower()
            if word_lower in model_card.content.lower() or word_lower in model_tags_lower:
                # Extract the text that contains "arxiv"
                arxiv_code_match = re.search(r'\S*arxiv\S*', model_card.content)
                paper_code = arxiv_code_match.group(0) if arxiv_code_match else None
                
                # Return the relevant data
                return {
                    "Model Name": model.id,
                    "Matching Word": word,
                    "created_at": model.created_at,
                    "last_modified": model.last_modified if model.last_modified else model.created_at,
                    "Downloads": model.downloads,
                    "contains_paper": contains_paper,
                    "paper_code": paper_code
                }
    except Exception as e:
        print(f"Error processing model {model.id}: {e}")
        return None


# Use ThreadPoolExecutor to process models concurrently
with ThreadPoolExecutor(max_workers=12) as executor:
    futures = [executor.submit(process_code_generation_model, model) for model in models]
    
    # Collect results as threads complete
    for future in as_completed(futures):
        result = future.result()
        if result:
            data.append(result)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(data, columns=["Model Name", "Matching Word", "Downloads", "created_at", "last_modified","contains_paper", "paper_code"])

# Save DataFrame to CSV
output_file = "code_generation_models.csv"
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")
