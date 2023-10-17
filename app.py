# app.py
import streamlit as st
from bigdl.llm.langchain.llms import TransformersLLM
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import SystemMessage

import re
import os

import logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Configure the Streamlit page with custom settings
st.set_page_config(
    page_title="OptiPrompt",
    page_icon=":ringed_planet:",
    menu_items={
        'Get help': 'https://github.com/Infinite-FDU/BigDL',
        'Report a bug': "https://github.com/Infinite-FDU/BigDL/issues",
        'About': "# Something about this app"
    }
)

# Handle download
output_file_name = "chat_history.md"
user_prefix = "Human:"
ai_prefix = "AI:"
delimiter = "***"

if not os.path.exists(output_file_name):
    with open(output_file_name, "w") as file:
        file.write("# Chat History\n")

st.title(":bird: OptiPrompt")
logging.info("Streamlit page configured")


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


if "custom_instruction" not in st.session_state:
    st.session_state.custom_instruction = ""

# Create a sidebar section in the Streamlit app for user configuration
with st.sidebar:
    # Create a selectbox to choose a local model with default options
    model_name = st.selectbox(
        'Choose local model', ("Baichuan-13B-Chat", ""), placeholder="Select...")
    st.write("Model name:", model_name)

    # Create a radio button group for selecting input types
    user_input_type = st.radio("Select input type", [
                               "multi-step", "judge", "default"], index=2)


    file_path = "system_message.txt"
    # Check if the system message text file exists
    if os.path.exists(file_path):
        # If the file exists, read its contents and store it in a string
        with open(file_path, "r") as file:
            local_system_message = file.read()
    else:
        local_system_message = ""
    st.session_state.custom_instruction = local_system_message

    # Create a form for customizing instructions
    with st.form("Customize instruction"):
        custom_instruction = st.text_area(
            "Customize instructions :sunglasses:", value=local_system_message, max_chars=500)
        submitted = st.form_submit_button("Submit")

    # If the form is submitted, save the customized instruction to the system message text file
    if submitted:
        # Store the customized instruction in the session state
        st.session_state.custom_instruction = custom_instruction
        with open("system_message.txt", "w") as file:
            file.write(custom_instruction)
        st.toast('Your instruction was saved!')


logging.info("Exit side bar")

# Load the selected Transformers LLM (Language Model) based on the chosen model name
llm = load_transformers_llm(model_name)
st.success(model_name + " loaded, enjoy your journey!")

logging.info("Transformers LLM loaded")


# Display chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


logging.info("Chat history displayed")

# ======================================================== #
# ================ Generate initial prompt =============== #
# ======================================================== #

simple_prompt = ChatPromptTemplate.from_template(
    """
{type_instruction}

用户输入：
{user_input}
"""
)

init_prompt = ChatPromptTemplate.from_template(
    """
{type_instruction}

用户输入：
{user_input}

修改的输入如下：
你好，AI助手，我想向你咨询一下问题：
"""
)

multi_step_init_prompt = ChatPromptTemplate.from_template(
    """
{type_instruction}

用户输入：
{user_input}

修改的输入如下：
你好，AI助手，基于已有问题：{user_input}，我将问题拆分为几步，所以想向你咨询下列问题:
"""
)


# ======================================================== #
# ================= Generate Instructions ================ #
# ======================================================== #

multi_step_instruction = """
您是一个语言模型提示词撰写专家，你的工作是为用户优化他们的问题，输出更好的问题，而非回答问题，你修改后的答案将提供给更强大的语言模型，由他们来给出问题的答案。
用户的输入可能涉及一个复杂的问题，如果直接让语言模型回答这个问题效果并不好。所以请你思考：如果解决这个问题可以分为哪些子问题？并且将每个小问题作为优化过的问题输出。
优化过的问题将以“你好，AI助手，基于已有问题%原有问题%，我将问题拆分为几个小问题，所以想向你咨询下列问题：”，以“请逐个回答上述问题，一步步思考。”结尾。

例子1：
输入：如何使用语言模型？
修改后的输入：
你好，AI助手，基于已有问题“如何使用语言模型？”，我将问题拆分为几步，所以想向你咨询下列问题：

1.如何获取语言模型的使用资格？
2.如何学习语言模型的使用方法？
3.如何熟练掌握语言模型的使用

请逐个回答上述问题，一步步思考。

例子2：
输入：如何赚到100万？
修改后的输入：
你好，AI助手，基于已有问题“如何赚到100万？”，我将问题拆分为几步，所以想向你咨询下列问题：
1.如何找到一份高薪的工作？
2. 如何提高自己的技能和知识水平以获得更高薪资？
3. 如何合理规划财务以实现财富增值？
4. 在什么行业或领域中更容易赚取百万以上的收入？
5. 如何在职场上建立良好的人际关系从而提升个人价值？
"""

code_instruction = """
您是一个代码优化AI助手。
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

请依赖你的专业知识，给出你的评分，请不要给出过高的评分，你需要严格一些，将评分放在方括号中，之后你可以加上评分理由和建议。例如：[8.5]，评分范围为0-10分，小数点后保留一位小数。

"""

default_instruction = """您是一个语言模型提示词撰写专家，你的工作是为用户优化他们的问题，输出更好的问题，而非回答问题，你修改后的答案将提供给更强大的语言模型，由他们来给出问题的答案。
接下来，用户会向你提供一个问题，你需要将问题修改为更好的问题输出，请注意输出的问题不针对用户，不是对于用户需求的再度确认，而站在用户视角可以用于向更强大的语言模型提问。
换句话说，你要替用户问出更好的问题，在此过程中，你需要让问题更加明确、最好能提供例子说明、改正问题中的语法错误以及事实性错误。

你的回答将以”你好，AI助手，我想向你咨询一下问题：“开头。请以问号作为你输出的结尾。

例子1：
问题输入：复旦 哲学系
问题输出：你好，AI助手！我想向你咨询一下问题：复旦哲学系专业实力怎么样？请为我介绍其概括。

例子2：
问题输入：长城再哪里
问题输出：你好，AI助手！我想向你咨询一下问题：长城在哪里

例子3：
问题输入：container复数
问题输出你好，AI助手！我想向你咨询一下问题：英语单词container的复数形式是什么
"""

# ======================================================== #
# ==================== Generate Chains =================== #
# ======================================================== #

system_message = SystemMessage(content=st.session_state.custom_instruction)

final_prompt = (system_message + init_prompt)
chain = LLMChain(llm=llm, prompt=final_prompt)

multi_step_final_prompt = (system_message + multi_step_init_prompt)
multi_step_chain = LLMChain(llm=llm, prompt=multi_step_final_prompt)

judge_final_prompt = (system_message + simple_prompt)
judge_chain = LLMChain(llm=llm, prompt=judge_final_prompt)

logging.info("Chains are ready")

def extract_transformed_text(response: str, to_extract: str) -> str:
    """
    Extracts the transformed text from the response based on a specified string.

    Args:
        response (str): The response from the language model.
        to_extract (str): The string to look for in the response.

    Returns:
        str: The extracted transformed text.
    """
    # Use regex to extract text after the specified string
    match = re.search(f'{to_extract}(.*)', response, re.DOTALL)
    if match:
        transformed_text = match.group(1).strip()
        return transformed_text
    else:
        return "No modified question found"



logging.info("User input begins")
if user_input := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Wait for it..."):
            logging.info("Calling chains")
            if (user_input_type == "default"):
                response = chain.predict(
                    type_instruction=default_instruction, user_input=user_input)
                extracted_response = extract_transformed_text(response, "修改的输入如下：")
            elif (user_input_type == "judge"):
                response = judge_chain.predict(
                    type_instruction=judge_instruction, user_input=user_input)
                extracted_response = extract_transformed_text(response, "小数点后保留一位小数。")
            elif (user_input_type == "multi-step"):
                response = multi_step_chain.predict(
                    type_instruction=multi_step_instruction, user_input=user_input)
                extracted_response = extract_transformed_text(response, "修改的输入如下：")
            else:
                st.warning("Please select an input type", icon="🚨")
                st.stop()
        
        logging.info("extracted_response: " + extracted_response)
        response_newlines = extracted_response.replace('\n', '\n\n')
        st.markdown(response_newlines)

        # Manage outputfile
        with open(output_file_name, "a") as file:
            file.write("**" + user_input_type + "|** ")
            file.write(user_prefix + " " + user_input + "\n")
            file.write(ai_prefix + " " + response_newlines + "\n")
            file.write(delimiter + "\n")
    st.session_state.messages.append(
        {"role": "assistant", "content": response_newlines})

with st.sidebar:
# Create a button for downloading the image
    with open(output_file_name, "r") as file:
        btn = st.download_button(
            label=":file_folder:",
            data=file,
            file_name=output_file_name,
            use_container_width=True
        )
