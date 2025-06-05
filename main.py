from utils.chunker import chunkFiles
from utils.collection import createCollection
from utils.query import sendQuery
from utils.memory import addHistory, getHistory
from utils.rewrite import rewriteQuery
from utils.intent import classifyIntent
import streamlit as st
import random
import time

def retrieveResponse(q, collection, user):
    print("Retrieving...")
    addHistory(user, "user", q)
    print("Added to history...")
    rewrittenQuery = rewriteQuery(q, getHistory(user))
    print("Rewritten query to:", rewrittenQuery)
    intent = classifyIntent(rewrittenQuery)
    print("Classified intent to:", intent)
    if intent == "general":
        response = "I'm sorry, I can't answer that question."
    else:
        response = sendQuery(rewrittenQuery, collection)
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

@st.cache_resource
def initialize():
    chunks = chunkFiles()
    collection = createCollection(chunks)
    return collection

def main():
    collection = initialize()

    st.title("Simple chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(retrieveResponse(prompt, collection, "1"))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # query = input("Enter query: ")
    # answer = retrieveResponse(query, collection, "1")
    # print(answer)

if __name__ == "__main__":
    main()