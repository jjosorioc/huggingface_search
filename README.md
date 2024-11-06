# Huggingface Model Search Tool

This repository provides tools to search Huggingface models based on specific keywords and extract metadata from the model cards. It is designed for users interested in fields such as software engineering, programming, development, and other technical domains, leveraging the Huggingface API for seamless searching and metadata extraction.

## Features

- **Keyword-Based Search:** Search for models containing terms related to software engineering and development.
- **Filter by Research Papers:** Extract models linking to papers (e.g., Arxiv) and obtain additional information such as Arxiv codes.
- **Concurrent Processing:** Multithreading is used to handle a large volume of models efficiently.
- **Model Card Metadata Extraction:** Extracts detailed metadata from model cards, aiding researchers and developers in finding models relevant to their work.
- **Excel Export:** Saves results in an Excel file for further analysis.

## How it Works

### Jupyter Notebooks

This repository contains Jupyter notebooks for an interactive experience, allowing for model searching, metadata extraction, and CSV cleaning:

1. **Search Terms:** A predefined list of terms related to software engineering and development, including:
   - "software engineering", "programming", "development", "MLOps", "DevOps", etc.
   
2. **Huggingface API:** Uses the `HfApi` from Huggingface to fetch models with metadata, including tags and links to papers.
   
3. **Concurrent Processing:** Threads are used to speed up data extraction, making the search and extraction process more efficient.

4. **Paper Filter:** Filters models that mention "arxiv" or "paper," pulling Arxiv codes if available.

5. **Excel Output:** The extracted data—including model name, matching keywords, download counts, and Arxiv codes (if available)—is saved to an Excel file for convenient analysis.

#### Example Usage

To search for models, interact with the cells in the notebook:

1. Search for models related to software engineering:
   ```python
   software_engineering_models = api.list_models(search="software engineering", cardData=True, sort='downloads', direction=-1)
   ```
2. Search for models related to software development:
   ```python
   software_development_models = api.list_models(search="software development", cardData=True, sort='downloads', direction=-1)
   ```
3. Search by specific tags:
   ```python
   software_engineering_models_tags = api.list_models(tags=["software engineering"], cardData=True, sort='downloads', direction=-1)
   ```

## Applications

This tool is valuable for:

- **Researchers:** Finding models linked with research papers for specific domains.
- **Developers:** Discovering pre-trained models in technical domains.
- **Data Scientists:** Exploring models by tags and metadata for suitable project models.
  
By leveraging model cards, users gain deeper insights into model training details and potential applications.
