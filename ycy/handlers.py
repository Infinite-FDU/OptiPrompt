# handlers.py
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import re


class ChatboxHandler:
    def __init__(self, llm) -> None:
        self.llm = llm

    def handle_input(self, user_input):
        pass

class FactQuestionHandler(ChatboxHandler):
    def __init__(self, llm):
        super().__init__(llm)
        self.fact_prompt = ChatPromptTemplate.from_template(
        """这是一个寻求事实的问题。为了获得更准确和有用的答案，请执行以下操作：

        1. 请简化问题，使其尽可能清晰和精炼。
        2. 请检查问题中的语法和拼写错误，确保问题表达准确。
        
        原来的问题如下：
        {user_input}
        
        修改的问题如下：
        """
    )
    def handle_input(self, user_input):
        # Logic to handle fact-based questions
        chain = LLMChain(llm=self.llm, prompt=self.fact_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        # Use regex to extract text after "修改的问题如下："
        match = re.search(r'修改的问题如下：(.*)', response, re.DOTALL)
        if match:
            transformed_text = match.group(1).strip()
            return transformed_text
        else:
            return "No modified question found"

class CodeQuestionHandler(ChatboxHandler):
    def __init__(self, llm) -> None:
        super().__init__(llm)
        self.code_prompt = ChatPromptTemplate.from_template(
        """这是一个有关编程的问题。为了获得更准确和有用的答案，请优化用户的输入，但不要修改具体的代码。
        1. 如果用户提供代码，清楚地指出哪一段代码有问题。如果用户的代码有误，不要直接修改。
        2. 用更加清晰的语言描述问题。

        原来的问题如下：
        {user_input}
        
        修改的问题如下：
        """
        )

    def handle_input(self, user_input):
        # Logic to handle fact-based questions
        chain = LLMChain(llm=self.llm, prompt=self.code_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        # Use regex to extract text after "修改的问题如下："
        match = re.search(r'修改的问题如下：(.*)', response, re.DOTALL)
        if match:
            transformed_text = match.group(1).strip()
            return transformed_text
        else:
            return "No modified question found"

class DefaultQuestionHandler(ChatboxHandler):
    def __init__(self, llm) -> None:
        super().__init__(llm)
        self.default_prompt = ChatPromptTemplate.from_template(
        """这是一个通用问题。请提出您的问题，我们将尽力提供解答。

        示例问题：
        "告诉我有趣的历史事件。"
        """
        )

    def handle_input(self, user_input):
        chain = LLMChain(llm=self.llm, prompt=self.default_prompt, llm_kwargs={"max_new_tokens": 512})
        response = chain.run(user_input)
        return response


def create_chatbox_handler(input_type, llm):
    if input_type == "fact":
        return FactQuestionHandler(llm)
    elif input_type == "code":
        return CodeQuestionHandler(llm)
    elif input_type == "default":
        return DefaultQuestionHandler(llm)
