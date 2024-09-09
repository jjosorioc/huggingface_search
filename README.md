# Huggingface Model Search Tool

This repository provides tools to search Huggingface models based on specific keywords and extract metadata from the model cards. It is particularly useful for searching models related to fields such as software engineering, programming, development, and other technical domains using the Huggingface API.

## Features

- **Search models by keywords:** The script searches models containing specific words related to software engineering and development.
- **Filter models with relevant papers:** Models containing links to papers (like Arxiv) can be filtered to include additional information such as the Arxiv code.
- **Concurrent processing:** The script uses multithreading to handle a large number of models efficiently.
- **Model card extraction:** The repository allows extraction of metadata from model cards, which can be useful for researchers and developers working with Huggingface models.
- **Output to Excel:** The results are saved into an Excel file for further analysis.

## How it Works

### main.py

The `main.py` script provides a high-level implementation of searching for Huggingface models based on predefined keywords, extracting the relevant model information, and saving the results into an Excel file.

#### Key Components

1. **Search Terms:**
   A list of predefined words related to software engineering and development is used to filter models. These include:
   - "software engineering", "programming", "development", "MLOps", "DevOps", etc.

2. **Huggingface API:**  
   The `HfApi` from Huggingface is used to fetch models with their metadata and model cards. Model cards provide additional information, including papers and tags.

3. **Multithreading:**  
   The script uses a thread pool to process models concurrently, speeding up the extraction of relevant model data.

4. **Filtering for Papers:**  
   The script searches for models that mention "arxiv" or "paper" and extracts Arxiv codes if available.

5. **Data Output:**  
   The extracted data, including model name, matching keyword, download counts, and Arxiv paper codes (if available), is saved to an Excel file.

#### Example Usage

To run the script:

```bash
python main.py
```

The script will process the models and save the output to an Excel file (`software_engineering_models.xlsx`).

### Jupyter Notebook

The Jupyter notebook provides an interactive way to search for models using the Huggingface API. It allows for searching models by keyword or tag and prints out relevant model information, including the number of downloads and associated tags.

#### Key Components

1. **Search by Keywords:**
   The notebook allows searching for models related to "software engineering," "software development," and other fields using the Huggingface API's search functionality.

2. **Search by Tags:**  
   Models can also be searched using specific tags like "software engineering" to narrow down the search to relevant models.

3. **Logging and Error Handling:**  
   The notebook suppresses logging from Huggingface to provide clean output and focuses on displaying relevant information.

#### Example Usage

To use the notebook, you can run the cells interactively:

1. Search for models related to software engineering:
   ```python
   software_engineering_models = api.list_models(search="software engineering", cardData=True, sort='downloads', direction=-1)
   ```
2. Search for models related to software development:
   ```python
   software_development_models = api.list_models(search="software development", cardData=True, sort='downloads', direction=-1)
   ```
3. Search by tags (e.g., "software engineering"):
   ```python
   software_engineering_models_tags = api.list_models(tags=["software engineering"], cardData=True, sort='downloads', direction=-1)
   ```

## Applications

This tool can be useful for:

- **Researchers:** Searching for models with relevant papers and studies related to specific fields.
- **Developers:** Finding pre-trained models in specific technical domains.
- **Data Scientists:** Exploring models by tags and metadata to discover suitable models for their projects.
  
By utilizing model cards, users can extract deeper insights into how models are trained and their potential applications.

