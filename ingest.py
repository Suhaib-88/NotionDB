from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.cohere import CohereEmbeddings
import pickle, faiss

path_files= list(Path("Notion_DB").glob("**.*.md"))

data= []

sources=[]
for file in path_files:
    with open(file) as f:
        data.append(f.read())
    sources.append(file)

text_splitter= CharacterTextSplitter(chunk_size=1500, separator="\n")
docs= []
metadatas=[]

for i, d in enumerate(data):
    splits= text_splitter.split_text(d)
    docs.extend(splits)
    metadatas.extend([{"source":sources[i]}]* len(splits))

store= FAISS.from_texts(docs, CohereEmbeddings(), metadatas= metadatas)

faiss.write_index(store.index,'docs.index')
store.index= None

with open("faiss_store.pkl",'wb') as f:
    pickle.dump(store, f)