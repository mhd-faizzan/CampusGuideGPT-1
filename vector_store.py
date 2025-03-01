import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def load_data():
    return pd.read_csv("hochschule_harz_data.csv")

def embed_text(texts, model):
    return model.encode(texts, convert_to_numpy=True)

def create_faiss_index(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = df.apply(lambda row: " ".join(row.astype(str)), axis=1).tolist()
    
    embeddings = embed_text(texts, model)
    index = faiss.IndexFlatL2(embeddings.shape[1])  
    index.add(np.array(embeddings, dtype=np.float32))
    
    return index, model, texts

df = load_data()
faiss_index, embed_model, text_data = create_faiss_index(df)

def retrieve_similar_entry(query):
    query_embedding = embed_text([query], embed_model)
    _, idx = faiss_index.search(np.array(query_embedding, dtype=np.float32), 1)
    return df.iloc[idx[0][0]]
