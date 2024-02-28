# Import necessary libraries
from langchain.llms import AzureOpenAI
from langchain.agents import AgentType, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.callbacks import StreamlitCallbackHandler
from langchain.sql_database import SQLDatabase
import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()

apikey = "yes"

# Set up Azure OpenAI API configuration
openai.api_type = "azure"
openai.api_version = os.getenv("OPENAI_VERSION")
openai.api_base= os.getenv("OPENAI_URL_BASE")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")


# Create an instance of Azure OpenAI
llm = AzureOpenAI(
    temperature=0, 
    engine="gpt-3-5",
    model_name="gpt-3.5-turbo",
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
