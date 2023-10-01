# app.py
import streamlit as st
from handlers import create_chatbox_handler
from bigdl.llm.langchain.llms import TransformersLLM

import re
import time

st.set_page_config(
    page_title="Infinit FDU Chatbot",
    page_icon="👋",
)

st.title("Infinit FDU Chatbot")

# Use cache to load model, no need to reload after web rerun
@st.cache_resource
def load_transformers_llm(model_name, max_new_tokens):
    # Define the base folder path
    base_folder_path = "F:/Study/Code/llm-models"

    # Append MODEL_NAME to the folder path
    model_path = base_folder_path + "/" + model_name

    if (model_name == "Baichuan-13B-Chat"):
        llm = TransformersLLM.from_model_id_low_bit(
            model_id=model_path,
            model_kwargs={"temperature": 0.2, "trust_remote_code": True},
            
        )

    return llm


# config sidebar
with st.sidebar:
    MODEL_NAME = st.selectbox('Choose local model',
        ("Baichuan-13B-Chat", ""),
        placeholder="Select...",)
    st.write("Model name:", MODEL_NAME)
    max_new_tokens = st.number_input("Set max new tokens", value=1024)
    st.write("Max new tokens:", max_new_tokens)
    user_input_type = st.radio("Select input type", ["fact", "code", "default"], index=None)

# load llm
llm = load_transformers_llm(MODEL_NAME, max_new_tokens)
# set handler
handler = create_chatbox_handler(user_input_type, llm)
st.success("Model " + MODEL_NAME + " loaded, enjoy your journey")



# chatbox memory
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_input := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Wait for it..."):
            response = handler.handle_input(user_input)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})