# Import necessary libraries
from langchain.llms import AzureOpenAI
from langchain.agents import AgentType, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.callbacks import StreamlitCallbackHandler
from langchain.sql_database import SQLDatabase
import streamlit as st
import os
import openai

apikey="apikey"
# Set up Azure OpenAI API configuration
openai.api_type = "openai.api_type"
openai.api_version = "openai.api_version"
openai.api_base= "openai.api_base"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Create an instance of Azure OpenAI
llm = AzureOpenAI(
    temperature=0,
    engine="",
    model_name="",
    headers={
      "User-Id": ""
    }
)

# Create a Streamlit app
st.title("Talk to your data")

# Input API key and database connection string
# Example :- postgresql://username:password@localhost:port/yourdatabase
db_string="postgresql://username:password@localhost:port/yourdatabase"
if apikey:
    # Create an SQLDatabase instance
    db = SQLDatabase.from_uri(db_string)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    
    # Create an SQL agent
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
else:
    st.write("Please input your Azure OpenAI API Key")

# Chat input
if prompt := st.text_input("Chat with Assistant"):
    st.write("User: " + prompt)
    
    # Run the assistant and display the response
    with st.empty():
        st_callback = StreamlitCallbackHandler(st)
        response = agent_executor.run(prompt, callbacks=[st_callback])
        st.write("Assistant: " + response)
