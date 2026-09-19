
from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# ques="How are you?"
# res=llm.invoke(ques)
# print(res.content)

## If we want to let it run in loops like someone exits from chatbot
# while True:
#     query=input("user:")
#     if(query in ["exit","stop","ok","quit"]):
#         print("GoodBye!")
#         break
#     res=llm.invoke(query)
#     print("AI:",res.content[0]["text"]) #to print text only

##with streamlit
st.title("QnA Chatbot")
st.markdown("This is a chatbot built using Google Gemini 3.5 model." )

if "messages" not in st.session_state:
    st.session_state.messages=[]
for messages in st.session_state.messages:
    role=messages["role"]
    content=messages["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask anything")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    ai_text = res.content[0]["text"]
    st.session_state.messages.append({"role":"ai","content":ai_text})
    st.chat_message("ai").markdown(ai_text)

  





