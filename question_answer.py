import faiss
from langchain.chat_models.cohere import ChatCohere
import pickle, argparse
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

parser= argparse.ArgumentParser(description="Ask the question to notion DB")
parser.add_argument("--question", type=str, help="question to ask")
argparse= parser.parse_args()


index= faiss.read_index("docs.index")
with o[]