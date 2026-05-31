import streamlit as st
from openai import OpenAI

# server_url = st.secrets["backend_url"]

client = OpenAI(
    api_key=st.secrets["api_key"],
    base_url=st.secrets["base_url"]
)
st.title("AI Interview Chat Bot")
with st.form("Details"):
    Lang = st.text_input("Enter the Language")
    Topic = st.text_input("Enter the Topic")
    Level = st.selectbox("Enter the Level",["Easy","Medium","Advance"])
    Type = st.selectbox("Enter the Type",["MCQ's","Theory Questions","Coding Snippets"])

    Submit_Button = st.button("Submit")

    if Submit_Button:

        prompt = f"""
            Give me Questions in {Lang} Language on Topic Name is {Topic} in {Level} level and {Type} type.
            
            Follow:
            Do not give any expalination give only Questions

        """

            

        response = client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages = [
                {
                    "role" : "system",
                    "Content" : prompt
                    
                } 
            ]
        )
        st.write(response.choices[0].message.content)
        




