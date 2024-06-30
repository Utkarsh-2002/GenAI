## Conversation Q&A

import streamlit as st

from langhain.schema import HumanMessage, SystemMessage, AIMessage      # we give a question it acutally a humanmessage then by deafault  chatbout domain messge like act as a comedy chat bot then it is System messageand llm provide response that is AI message
from lanchain.chat_models import ChatOpenAI


## streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's chat")


from dotenv import load_dotenv    #open ai API
load_dotenv()

import os

chat = ChatOpenAI(tempertaure = 0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a comedian AI assitant")
    ]


#function to load OPen AI model and get responses

def get_chatmodel_response(question):
    
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])    #get the anser 
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("InputL ",key="input")
response = get_chatmodel_response(input)

submit=st.button("Ask the Question")

## if ask button clicked

if submit:
    st.subheader("The response is")
    st.write(response)

