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
def load_transformers_llm(model_name):
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
    model_name = st.selectbox('Choose local model',
        ("Baichuan-13B-Chat", ""),
        placeholder="Select...",)
    st.write("Model name:", model_name)
    user_input_type = st.radio("Select input type", ["multi-step", "code", "default"], index=None)

    with st.form("Customize instruction"):
        custom_instruction = st.text_area("Customize instructions :sunglasses:", max_chars=500,
                                   )
        st.session_state.custom_instruction = custom_instruction
        submitted = st.form_submit_button("Submit")
    if submitted:
        with open("system_message.txt", "w") as file:
            # Write the system message to the file
            file.write(custom_instruction)
        st.toast('Your instruction was saved!')


# load llm
llm = load_transformers_llm(model_name)
# set handler
# handler = create_chatbox_handler(user_input_type, llm)
st.success("Model " + model_name + " loaded, enjoy your journey")

if "first_deployment" not in st.session_state:
    st.session_state.first_deployment = True

if "custom_instruction" not in st.session_state:
    st.session_state.custom_instruction = ""


# chatbox memory
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

init_prompt = ChatPromptTemplate.from_template(
   """
    {type_instruction}

    用户输入：
    {user_input}

    修改的输入如下：
    你好，AI助手，我想向你咨询一下问题：
   """
)

system_message = SystemMessage(content=st.session_state.custom_instruction)
final_prompt = (system_message + init_prompt)
chain = LLMChain(llm=llm, prompt=final_prompt)

# ======================================================== #
# ================= Generate Instruction ================= #
# ======================================================== #

multi_step_instruction = ""

code_instruction = """您是一个代码优化AI助手。
        请修改并优化以下代码问题，以使其更明确和清晰。请确保提供足够的上下文信息和详细描述，以便更好地回答问题。如果你的答案包括代码，用markdown格式展示代码部分。
"""

judge_instruction = """你是一个语言模型提示词评分大师，用户将输入一个提示词，你针对该问题给出你的评分以及你的建议，评分为0-10。

    评分依据一下几点：
    1. 该问题是否有逻辑谬误、或者是歧义。
    2. 该问题是否有语法错误、错别字。
    3. 该问题是否足够具体，能帮助语言模型理解他所表达的意思，太简短或者宽泛的问题是糟糕的。
    4. 该问题是否被拆分为了多个小问题，激发语言模型分步骤思考的能力，以便语言模型一步步解决它。
    5. 该问题是否提供了例子，便于语言模型理解具体情景。

    评分的尺度是：
    10分-足够完美，可以向大语言模型提问。
    8分-基本完美，但没有提供例子或是没有拆分为多个小问题。
    6分-没有明显的逻辑、语法错误，但是还有改进的空间。
    4分-问题较大。
    2分-需要重写。

    请赖你的专业知识，给出你的评分，请不要给出过高的评分，你需要严格一些，将评分放在方括号中，之后你可以加上建议。例如：[8.5]，评分范围为0-10分，小数点后保留一位小数。"""

default_instruction = """您是一个语言模型提示词撰写专家，你的工作是为用户优化他们的问题，输出更好的问题，而非回答问题，你修改后的答案将提供给更强大的语言模型，由他们来给出问题的答案。
        接下来，用户会向你提供一个问题，你需要将问题修改为更好的问题输出，请注意输出的问题不针对用户，不是对于用户需求的再度确认，而站在用户视角可以用于向更强大的语言模型提问。
        换句话说，你要替用户问出更好的问题，在此过程中，你需要让问题更加明确、最好能提供例子说明、改正问题中的语法错误以及事实性错误。

        你的回答将以$你好，AI助手，我想向你咨询一下问题：$开头。请以问号作为你输出的结尾。\n

        例子：\n问题输入$复旦 哲学系$\n问题输出$你好，AI助手！我想向你咨询一下问题：复旦哲学系专业实力怎么样？请为我介绍其概括。$\n问题输入$长城再哪里$\n问题输出$你好，AI助手！我想向你咨询一下问题：长城在哪里$\n问题输入$container复数$\n问题输出$你好，AI助手！我想向你咨询一下问题：英语单词container的复数形式是什么$"""

# ======================================================== #
# ======================================================== #
# ======================================================== #
def extract_transformed_text(response):
    # Use regex to extract text after "修改的输入如下："
    match = re.search(r'修改的输入如下：(.*)', response, re.DOTALL)
    if match:
        transformed_text = match.group(1).strip()
        return transformed_text
    else:
        return "No modified question found"

if user_input := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Wait for it..."):
            # response = handler.handle_input(user_input)
            if (user_input_type == "default"):
                _ = default_instruction
            elif (user_input_type == "multi-step"):
                _ = multi_step_instruction
            elif (user_input_type == "code"):
                _ = code_instruction
            elif (user_input_type == "judge"):
                _ = judge_instruction
            st.write("Final Prompt: ")
            # st.write(final_prompt.format(type_instruction = _, user_input=user_input))
            response = chain.predict(type_instruction = _, user_input=user_input)
        st.markdown(extract_transformed_text(response))
    st.session_state.messages.append({"role": "assistant", "content": response})