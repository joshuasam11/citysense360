import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(text):
    chunks = text.split(".")
    chunks = [c.strip() for c in chunks if c.strip()]

    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, chunks

def answer_question(index, chunks, question):
    q_vec = model.encode([question])
    distances, ids = index.search(q_vec, 3)

    retrieved = [chunks[i] for i in ids[0]]

    return " ".join(retrieved)
