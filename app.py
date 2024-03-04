import streamlit as st 
from functions import conRAG


st.title("Araf ChatBot")

# set initial messages
if "messages" not in st.session_state.keys():
    st.session_state["messages"] = [
        {"role": "assistant", "content":"Hello, How can i help you!"}
    ]


# display the messages 
if "messages" in st.session_state.keys():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    

user_prompt = st.chat_input()


if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content":user_prompt})

    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"]!="assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response=conRAG(user_prompt)
            st.write(ai_response)
    newAI_message = {"role": "assistant", "content": ai_response} 
    st.session_state.messages.append(newAI_message)


