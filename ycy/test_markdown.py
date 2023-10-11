import streamlit as st
from IPython.display import display, Markdown, Latex, HTML, JSON
import markdown


output = """
1.faklsdjkl;fgadsf
2.fjaklsdfasd
3.fasdlfkadsf'asd"""

print(markdown.markdown(output))

st.markdown(output)