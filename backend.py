import pandas as pd
from vector_store import retrieve_similar_entry

# Load CSV data
df = pd.read_csv("hochschule_harz_data.csv")

def get_university_info(query):
    """Retrieve relevant university information using FAISS"""
    return retrieve_similar_entry(query, df)
