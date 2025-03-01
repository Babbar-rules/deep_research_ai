import streamlit as st
from langchain.schema import HumanMessage
from utils.graph import graph

st.set_page_config(page_title="AI Research Assistant", page_icon="🤖")
st.title("Ask me anything")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process query using LangGraph
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        response_text = ""
        for event in graph.stream({"messages": [HumanMessage(content=prompt)], "search_results": ""}):
            values = list(event.values())
            if values and "messages" in values[0]:
                new_content = values[0]["messages"].content
                response_text += new_content  # Append streamed tokens
                message_placeholder.markdown(response_text)

           