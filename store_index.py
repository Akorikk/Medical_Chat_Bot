from src.helper import load_pdf, text_split, download_hugging_face_embedding
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os 

load_dotenv()

PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
