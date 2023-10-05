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

def multistep_prompt_zjh_1(user_input):
    return f"""您是一个大型语言模型提示词撰写专家。
        用户的输入可能涉及一个复杂的问题，如果直接让语言模型回答这个问题效果并不好。你的目的是将用户的问题拆分为几个小问题，让语言模型一步步思考，逐渐靠近答案。优化过的问题将以“请逐个回答上述问题，一步步思考。”结尾。

        例子：
        输入：
        我希望按欧式风格装修房子，要花费多少钱？

        修改后的输入：
        1.AI助手你好，欧式风格的房子主要有哪些家具？\n2.AI助手你好，欧式风格的家具一般需要多少钱？\n3.AI助手你好，完成欧式风格的装修总共需要多少钱？\n请逐个回答上述问题，一步步思考。

        原来的输入如下：
        {user_input}

        修改的输入如下：
        """

def feature_extraction_prompt_zjh_1(user_history):
    return f"""您是独属于该用户的提示词管家。
        您会定期看到用户向大型语言模型提问的历史记录，你需要根据这些历史提问，提取出几个用户的特征，包括但不限于使用语言、倾向于提出的问题类型、提问的立场、用户可能的身份、经常犯的逻辑谬误等等。
        我们会将这些特征加入到大型语言模型的prompt中，以便于模型更好地理解用户的提问。
        你需要在每个特征前面加上#号，以便于我们识别。

        例子1：
        历史记录：
        r如何将数组变成字符串
        enumerate放回参数
        find如何能把div下面包的所有内容都找到
        while至多3次怎么写
        我有一个网页请求经常会失败，导致程序停止，我如何让它失败时再来两遍
        
        提取出的特征：
        #用户经常提出编程问题。\n#用户经常提出关于Python的问题。

        例子2：
        历史记录：
        去北京旅游有什么交通出行的选择吗
        北京有什么好玩的地方吗
        北京有什么好吃的吗
        北京有什么好玩的吗
        北京著名景点有哪些

        提取出的特征：
        #用户喜欢旅游\n#用户计划去北京。

        以上例子以及特征与你所服务的客户无关，仅供参考。

        历史记录：
        {user_history}

        提取出的特征：
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