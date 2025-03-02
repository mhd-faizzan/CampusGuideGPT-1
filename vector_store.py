import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load the CSV data
def load_data():
    return pd.read_csv("hochschule_harz_data.csv")

df = load_data()

# Convert text data to embeddings
def create_faiss_index(df):
    """Create FAISS index from the CSV data"""
    embeddings = model.encode(df["University Name,Program,Duration,Fees,Application Deadline,Requirements,FAQ"].tolist())
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings

index, embeddings = create_faiss_index(df)

def retrieve_similar_entry(query, df):
    """Find the closest matching entry in the dataset"""
    query_embedding = model.encode([query])
    _, indices = index.search(np.array(query_embedding), k=1)  # Get top 1 match
    
    if indices[0][0] != -1:
        return df.iloc[indices[0][0]]
    return None
