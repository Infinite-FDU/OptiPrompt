# prompt_template.py

def fact_prompt_ycy_1():
    return """这是一个寻求事实的问题。为了获得更准确和有用的答案，请执行以下操作：

        1. 请简化问题，使其尽可能清晰和精炼。
        2. 请检查问题中的语法和拼写错误，确保问题表达准确。

        原来的输入如下：
        {user_input}

        修改的输入如下：
    """


def fact_prompt_ycy_2():
    return """Assist the user in improving the clarity and precision of their input. Ensure that their message is conveyed accurately and comprehensively. Suggest any necessary additions or modifications to enhance the quality of their communication.
    
    User input: {user_input}.

    Refined input:
    """


def utility_prompt_ycy_1():
    return """您是一个能够提升用户输入质量的AI助手。
        根据用户提供的问题或请求，对其输入进行编辑和修正，以确保表达更加精确、清晰。
        例如，如果用户需要修复电脑声音问题，请对其输入进行编辑，使其准确描述问题并排除不必要的信息。如果用户寻找Python编程教程，请编辑输入以反映清晰的需求，例如特定主题或技能水平。
        请确保编辑后的输入保持简洁明了，有助于提供更准确的回应。

        原来的输入如下：
        {user_input}

        修改的输入如下：
    """


def code_prompt_ycy_1():
    return """您是一个代码优化AI助手。
        请修改并优化以下代码问题，以使其更明确和清晰。请确保提供足够的上下文信息和详细描述，以便更好地回答问题。如果你的答案包括代码，用markdown格式展示代码部分。

        原来的输入如下：
        {user_input}

        修改的输入如下：
    """


def entertainment_prompt_ycy_1():
    return """您是一个娱乐问题优化AI助手。
请帮助用户优化以下娱乐性问题，使其更加明确、精确和简洁。删除不必要的信息，确保问题的核心内容清晰可见。
        原来的输入如下：
        {user_input}

        修改的输入如下：
        """


def personal_prompt_ycy_1(user_input):
    return f"""您是一个个人问题优化AI助手。
        请帮助用户优化以下个人问题，使其更加明确、精确和简洁。删除不必要的信息，确保问题的核心内容清晰可见。

        原来的输入如下：
        {user_input}

        修改的输入如下：
        """

def fact_prompt():
    return fact_prompt_ycy_2()

def code_prompt():
    return code_prompt_ycy_1()

def utility_prompt():
    return utility_prompt_ycy_1()

def entertainment_prompt():
    return entertainment_prompt_ycy_1()

def personal_prompt():
    return personal_prompt_ycy_1()

def default_prompt():
    return fact_prompt_ycy_1()