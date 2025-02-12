# AI Search Index Creation

## Steps to Create Index:
### Requirements:
- Python 3.11
- AOAI resource with text embeddings deployment
- Azure AI Search resource (Standard tier or above)
- Azure Storage Account (with Azure storage table)

### Using ai-search/ai-search.py script
1. Create a virtual environment in your directory using `python -m venv .venv`
2. Replace .env.local with the appropriate AOAI, AI Search, and Storage account variables. Rename to `.env` 
3. Install required packages (`pip install -r requirements.txt`)
4. `cd ai-search`
5. `python ai-search.py`  

### Using ai-search/ai-search.ipynb Jupyter notebook
1. Select a Jupyter kernel using "Select Kernel" in VS code or preferred Jupyter environment
2. Execute cells in Jupyter notebook
