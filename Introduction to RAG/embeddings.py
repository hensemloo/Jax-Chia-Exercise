# embeddings.py (part 1)
import os
from dotenv import load_dotenv
from langchain_core.embeddings import Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

_base = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    output_dimensionality=768,  # must match the Atlas index
)

# embeddings.py (part 2)
class PrefixedEmbeddings(Embeddings):
    """gemini-embedding-2 reads the task from a prefix."""

    def embed_documents(self, texts):
        return _base.embed_documents(
            [f"title: none | text: {t}" for t in texts]
        )

    def embed_query(self, text):
        return _base.embed_query(
            f"task: search result | query: {text}"
        )

embeddings = PrefixedEmbeddings()

# # example_1.py (part 2)
# 19 # Instantiate the vector store
# 20 vector_store = MongoDBAtlasVectorSearch(
# 21     collection=MONGODB_COLLECTION,
# 22     embedding=embeddings,
# 23     index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
# 24     relevance_score_fn="cosine",
# 25 )
# 26
# 27 # Create the vector search index
# 28 print("Creating vector search index...")
# 29 vector_store.create_vector_search_index(
# 30     dimensions=768, wait_until_complete=60
# 31 )
# 32 print("Vector Store Created!")
# 33
# 34 client.close()