# handlers.py
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from prompt_templates import fact_prompt, code_prompt, utility_prompt, personal_prompt, entertainment_prompt, default_prompt
import re  


def extract_transformed_text(response):
    # Use regex to extract text after "修改的输入如下："
    match = re.search(r'修改的输入如下：(.*)', response, re.DOTALL)
    if match:
        transformed_text = match.group(1).strip()
        return transformed_text
    else:
        return "No modified question found"

class ChatboxHandler:
    def __init__(self, llm) -> None:
        self.llm = llm

    def handle_input(self, user_input):
        pass

class FactQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.fact_prompt = ChatPromptTemplate.from_template(
        fact_prompt()
    )
    def handle_input(self, user_input):
        # Logic to handle fact-based questions
        chain = LLMChain(llm=self.llm, prompt=self.fact_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return extract_transformed_text(response)

class CodeQuestionHandler(ChatboxHandler):
    def __init__(self, llm) -> None:
        super().__init__(llm)
        self.code_prompt = ChatPromptTemplate.from_template(
       code_prompt()
        )

    def handle_input(self, user_input):
        # Logic to handle fact-based questions
        chain = LLMChain(llm=self.llm, prompt=self.code_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        # Use regex to extract text after "修改的输入如下："
        return extract_transformed_text(response)

class EntertainmentQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.entertainment_prompt = ChatPromptTemplate.from_template(
            entertainment_prompt()
        )

    def handle_input(self, user_input):
        # Logic to handle entertainment-related questions
        chain = LLMChain(llm=self.llm, prompt=self.entertainment_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return extract_transformed_text(response)

class UtilityQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.utility_prompt = ChatPromptTemplate.from_template(
            utility_prompt()
        )

    def handle_input(self, user_input):
        # Logic to handle utility-related questions
        chain = LLMChain(llm=self.llm, prompt=self.utility_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return extract_transformed_text(response)

class PersonalQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.personal_prompt = ChatPromptTemplate.from_template(
            personal_prompt()
        )

    def handle_input(self, user_input):
        # Logic to handle personal-related questions
        chain = LLMChain(llm=self.llm, prompt=self.personal_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return extract_transformed_text(response)



class DefaultQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.personal_prompt = ChatPromptTemplate.from_template(
            default_prompt()
        )

    def handle_input(self, user_input):
        # Logic to handle personal-related questions
        chain = LLMChain(llm=self.llm, prompt=self.personal_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return extract_transformed_text(response)


def create_chatbox_handler(input_type, llm):
    if input_type == "fact":
        return FactQuestionHandler(llm)
    elif input_type == "code":
        return CodeQuestionHandler(llm)
    elif input_type == "entertainment":
        return EntertainmentQuestionHandler(llm)
    elif input_type == "utility":
        return UtilityQuestionHandler(llm)
    elif input_type == "personal":
        return PersonalQuestionHandler(llm)
    else:
        # Default handler for unknown input types
        return DefaultQuestionHandler(llm)

