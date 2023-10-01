# prompt_template.py

def fact_prompt_ycy_1():
    return """这是一个寻求事实的问题。为了获得更准确和有用的答案，请执行以下操作：

1. 请简化问题，使其尽可能清晰和精炼。
2. 请检查问题中的语法和拼写错误，确保问题表达准确。

原来的问题如下：
{user_input}

修改的问题如下：
"""

def code_prompt_ycy_1():
    return """这是一个有关编程的问题。为了获得更准确和有用的答案，请优化用户的输入，但不要修改具体的代码。
1. 如果用户提供代码，清楚地指出哪一段代码有问题。如果用户的代码有误，不要直接修改。
2. 用更加清晰的语言描述问题。

原来的问题如下：
{user_input}

修改的问题如下：
"""
