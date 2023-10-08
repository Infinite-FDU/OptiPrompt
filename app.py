# app.py
import streamlit as st
from handlers import create_chatbox_handler
from bigdl.llm.langchain.llms import TransformersLLM
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import SystemMessage  


import re
import time

st.set_page_config(
    page_title="Infinit FDU Chatbot",
    page_icon="👋",
)

st.title("Infinit FDU Chatbot")

# TODO:
#  1. Let user input a custom instruction
#  2. Store this instruction in a local txt file
#  3. 

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
    max_new_tokens = st.number_input("Set max new tokens", value=512)
    st.write("Max new tokens:", max_new_tokens)
    user_input_type = st.radio("Select input type", ["fact", "code", "entertainment", "utility", "personal", "default"], index=None)


# load llm
llm = load_transformers_llm(MODEL_NAME, max_new_tokens)
# set handler
# handler = create_chatbox_handler(user_input_type, llm)


if "first_deployment" not in st.session_state:
    st.session_state.first_deployment = True

if "custom_instruction" not in st.session_state:
    st.session_state.custom_instruction = ""


with st.form("IST_FORM"):
    st.info("User instructions can only apply to new chats!", icon="🚨")
    INSTRUCTION = st.text_area("Customize instructions :sunglasses:", max_chars=500,
                               )
    st.session_state.custom_instruction = INSTRUCTION
    submitted = st.form_submit_button("Submit")
if submitted:
    st.toast('Your instruction was saved!', icon='😍')
st.session_state.first_deployment = False

# chatbox memory
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = ChatPromptTemplate.from_template(
   """
    {type_instruction}

    用户输入：
    {user_input}

    修改的输入如下：
    你好，AI助手，我想向你咨询一下问题：
   """
)

system_message = SystemMessage(content=st.session_state.custom_instruction)
overall_prompt = (system_message + prompt)
chain = LLMChain(llm=llm, prompt=overall_prompt)

code_instruction = """您是一个代码优化AI助手。
        请修改并优化以下代码问题，以使其更明确和清晰。请确保提供足够的上下文信息和详细描述，以便更好地回答问题。如果你的答案包括代码，用markdown格式展示代码部分。
"""
default_instruction = """您是一个语言模型提示词撰写专家，你的工作是为用户优化他们的问题，输出更好的问题，而非回答问题，你修改后的答案将提供给更强大的语言模型，由他们来给出问题的答案。
        接下来，用户会向你提供一个问题，你需要将问题修改为更好的问题输出，请注意输出的问题不针对用户，不是对于用户需求的再度确认，而站在用户视角可以用于向更强大的语言模型提问。
        换句话说，你要替用户问出更好的问题，在此过程中，你需要让问题更加明确、最好能提供例子说明、改正问题中的语法错误以及事实性错误。

        你的回答将以$你好，AI助手，我想向你咨询一下问题：$开头。请以问号作为你输出的结尾。\n

        例子：\n问题输入$复旦 哲学系$\n问题输出$你好，AI助手！我想向你咨询一下问题：复旦哲学系专业实力怎么样？请为我介绍其概括。$\n问题输入$长城再哪里$\n问题输出$你好，AI助手！我想向你咨询一下问题：长城在哪里$\n问题输入$container复数$\n问题输出$你好，AI助手！我想向你咨询一下问题：英语单词container的复数形式是什么$"""

if user_input := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Wait for it..."):
            # response = handler.handle_input(user_input)
            response = chain.predict(type_instruction = default_instruction, user_input=user_input)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})