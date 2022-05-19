from database import df
from txtai.embeddings import Embeddings

embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})

data=[]
for content in df['content']:
    data.append(str(content))

embeddings.index([(uid, text, None) for uid, text in enumerate(data)])
query=str(input("Enter Query : "))

for i in range(5):
    print(embeddings.search(query, 5)[i]['text'])