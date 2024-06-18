from dotenv import load_dotenv
import os
import streamlit as st
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # Load environment variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)



st.title('인공지능 시인')

inputContent = st.text_input("시의 주제를 적어주세요", "시 주제")




if st.button("입력"):
    
    with st.spinner('잠시만기다려주세요'):
    
        systemMessage = SystemMessage(content="주제에 맞는 시를 써줘")
        humanMessage = HumanMessage(content= inputContent)

        messages = [
            systemMessage,humanMessage
        ]

        

        parser = StrOutputParser()

        result = model.invoke(messages)
        message = parser.invoke(result)
        print(message)
        
        st.success('성공')
        st.write(message)







