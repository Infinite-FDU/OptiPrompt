<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- PROJECT LOGO -->
<br />
<!-- <div align="center">
  <a href="https://github.com/Infinite-FDU/BigDL">
    <img src="images/logo.jpg" alt="Logo" width="80" height="80">
  </a> -->

<h1 align="center">OptiPrompt</h1>
<h4 align="center">version 602</h4>
  <p align="center">
    A conversational AI chatbot for enhancing user queries and assisting in generating improved questions.
    <br />
    <a href="https://github.com/Infinite-FDU/BigDL"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Infinite-FDU/BigDL">View Demo</a>
    ·
    <a href="https://github.com/Infinite-FDU/BigDL/issues">Report Bug</a>
    ·
    <a href="https://github.com/Infinite-FDU/BigDL/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


Welcome to the **OptiPrompt** project, your gateway to a world of intelligent conversation and assistance! 🤖✨

The **OptiPrompt** is an innovative chatbot powered by state-of-the-art natural language processing models. Whether you're seeking answers, code optimization suggestions, or even help with refining your questions, our chatbot is here to assist you effectively. Designed for a variety of use cases, from code optimization to language model guidance, it's your go-to AI assistant.

Our project leverages the latest advancements in language modeling technology and provides you with a seamless conversational experience. Engage in productive discussions, refine your queries, and harness the power of AI to enhance your workflow.

Get ready to embark on an exciting journey with the **OptiPrompt**. Explore its capabilities, improve your communication, and boost your productivity. It's more than just a chatbot; it's your AI companion in the world of natural language understanding and generation.

Start your conversation with the **OptiPrompt** today and elevate your interactions to the next level! 🚀🤖

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

* Streamlit
* Langchain
* Baichuan-13b 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Getting Started

Before getting started with the project, ensure that you have the following prerequisites installed:

## Prerequisites

- **Python 3.9**: You'll need Python 3.10 to run this project. We recommend using Anaconda to manage your Python environments. You can create a Python 3.10 environment with the following command:

```bash
conda create -n infinite-fdu python=3.9
```

Activate the environment using:

```bash
conda activate infinite-fdu
```

## Installation

1. Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/Infinite-FDU/OptiPrompt
   ```
2. Navigate to the project directory
3. Install the project dependencies from the `requirements.txt` file:
   ```bash
   pip install --pre --upgrade bigdl-llm[all]
   pip install -r requirements.txt
   ```

### Check for CUDA Compatibility

Before running the project, it's essential to check whether your computer satisfies the requirements for CUDA support. CUDA is a parallel computing platform and application programming interface (API) model created by NVIDIA.

Some of the deep learning libraries used in this project, such as PyTorch, can leverage CUDA for GPU acceleration. If you have an NVIDIA GPU and wish to enable GPU support, you should ensure that your GPU is compatible with CUDA and that you have the appropriate NVIDIA drivers installed.


If your GPU is not CUDA-compatible or you encounter issues with CUDA, **remove the torch based packages in the `requirements.txt` and install on your own.**


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

## Prompt Engineering Overview

Welcome to the OptiPrompt, your intelligent assistant for prompt engineering. As a prompt engineer, your role is to craft and refine prompts to elicit precise and meaningful responses from language models. This chatbot offers a range of optimization options to assist you in your task.

### 1. Default Optimization

- **User Input:** _Enter your original prompt here._
- **Optimized Output:** _The chatbot will refine your prompt to make it more explicit and effective for language models._

### 2. Code Optimization

- **User Input:** _Share your code snippet or programming-related query._
- **Optimized Output:** _The chatbot will review and enhance your code for better readability and functionality._

### 3. Judge Prompt Word

- **User Input:** _Submit a prompt word or phrase for evaluation._
- **Evaluation Output:** _The chatbot will assess the quality of your prompt and provide a score along with feedback._

### 4. Multi-Step Question

- **User Input:** _Pose a complex question that can be divided into smaller steps._
- **Optimized Output:** _The chatbot will break down your question into manageable parts, perfect for step-by-step exploration._


**Note:** This project has been tested using artificial intelligence, Claude, for prompt optimization. It compares user inputs to optimized inputs and achieves a perfect score in **39 out of 39 tests.** For detailed information, please refer to the "test_default.ipynb" and "output.json" files.

## Custom Instructions for Persistent Memory

The OptiPrompt empowers you with the ability to provide custom instructions, allowing you to whisper specific guidance to the language model. These custom instructions serve as a form of persistent memory, influencing the behavior of the chatbot across different sessions.

### How Custom Instructions Work

1. **Customize Your Guidance**: Craft personalized instructions in plain text to guide the language model in a particular direction. You can provide context, preferences, or specific expectations.

2. **Save to Local File**: Your custom instructions are saved to a local file, ensuring they persist even after closing the chatbot session. This file acts as a repository of your guidance.

3. **Influence Model Behavior**: During subsequent interactions, the chatbot will refer to your saved custom instructions, effectively remembering your preferences and following your guidance.

4. **Adapt and Refine**: You can update and refine your custom instructions over time, enabling the language model to adapt to your evolving needs and preferences.

### Enhance Your Conversations

Custom instructions provide a powerful way to tailor your interactions with the OptiPrompt. Whether you want to fine-tune responses, shape the conversation, or achieve specific outcomes, your instructions serve as a valuable resource for persistent memory and guidance.

Harness the potential of custom instructions to create more meaningful and personalized conversations with the chatbot, making it a truly adaptable assistant that understands your unique requirements.

_For more examples, please refer to the [Documentation](https://python.langchain.com/docs/get_started/introduction)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
# Roadmap

## Version 1.0.0 (Initial Release)
- [x] Streamlit app setup with customizable settings and styling.
- [x] Integration of Transformers LLM with support for model selection.
- [x] Four distinct input types: multi-step, judge, code, and default.
- [x] User-friendly interface for prompt engineering with real-time previews.
- [x] System message functionality for context-aware interactions.
- [x] Chat history display for tracking conversations.
- [x] Save customized instructions to a local file for future sessions.
- [x] Documentation and GitHub repository setup.

## Future Versions
- [ ] Continued language support expansion.
- [ ] Integration with other local models.
- [ ] Collaboration with domain-specific experts for specialized knowledge.
- [ ] Exploration of educational and research applications.
- [ ] User feedback sessions for continuous improvement.






