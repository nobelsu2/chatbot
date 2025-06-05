from utils.chunker import chunkFiles
from utils.collection import createCollection
from utils.query import sendQuery

def main():
    chunks = chunkFiles()
    collection = createCollection(chunks)
    query = "What is the budget allocated for railways?"
    print(sendQuery(query, collection))

if __name__ == "__main__":
    main()