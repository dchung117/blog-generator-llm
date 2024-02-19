import os
import streamlit as st
from dotenv import load_dotenv

from blog_gen.blog_gen import BlogLLAMAHandler

if __name__ == "__main__":
    load_dotenv()
    blog_llama = BlogLLAMAHandler(os.environ.get("LLAMA_PATH"))
    st.set_page_config(page_title="Blog generator",
                       page_icon="🤖",
                       layout="centered",
                       initial_sidebar_state="collapsed"
    )

    st.header("Generate a blog w/ LLaMa 2")
    topic = st.text_input("What is the blog topic?")
    col_1, col_2 = st.columns([5, 5])
    with col_1:
        n_words = st.text_input("How many words to generate?")
    with col_2:
        style = st.selectbox("Select an audience for the blog", [
            "Researchers", "Students", "Children"
        ])
    done = st.button("Generate")

    if done:
        blog = blog_llama.get_llm_response(topic, num_words=n_words, blog_style=style)
        st.write(blog)