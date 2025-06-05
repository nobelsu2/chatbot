from utils.chunker import chunkFiles
from utils.collection import createCollection
from utils.query import sendQuery
from utils.memory import addHistory, getHistory
from utils.rewrite import rewriteQuery
from utils.intent import classifyIntent

def retrieveResponse(q, collection, user):
    print("Retrieving...")
    addHistory(user, "user", q)
    print("Added to history...")
    rewrittenQuery = rewriteQuery(q, getHistory(user))
    print("Rewritten query to:", rewrittenQuery)
    intent = classifyIntent(rewrittenQuery)
    print("Classified intent to:", intent)
    if intent == "general":
        return "I'm sorry, I can't answer that question."
    else:
        return sendQuery(rewrittenQuery, collection)

def main():
    chunks = chunkFiles()
    collection = createCollection(chunks)
    query = input("Enter query: ")
    answer = retrieveResponse(query, collection, "1")
    print(answer)

if __name__ == "__main__":
    main()