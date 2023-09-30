# LangChain Streamlit Chat Assistant

This is a Streamlit application that allows you to interact with a chat assistant powered by LangChain and Azure OpenAI. You can use this assistant to perform various tasks, including querying a SQL database and getting responses to your queries.

## Prerequisites

Before you can use this application, make sure you have the following prerequisites:

1. **Azure OpenAI API Key**: You'll need an Azure OpenAI API key. If you don't have one, you can obtain it from Azure OpenAI.

2. **Database Connection String**: You should have the connection string for your PostgreSQL database. The format of the connection string should be like this: `postgresql://username:password@localhost:port/yourdatabase`.

3. **Streamlit**: Ensure you have Streamlit installed. You can install it using `pip install streamlit`.

## Getting Started
**[Demo Video Link](https://drive.google.com/file/d/13osa0RrF8uMb3mxeWlo9mc-QU8PpG82K/view)**

1. Clone the repository and navigate to the project directory.

2. Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Set the following environment variables:

    - `LANGCHAIN_TRACING_V2`: Set this to `"LANGCHAIN_TRACING_V2"`.
    - `LANGCHAIN_ENDPOINT`: Set this to your LangChain endpoint.
    - `LANGCHAIN_API_KEY`: Set this to your LangChain API key.
    - `OPENAI_API_KEY`: Set this to your Azure OpenAI API key.

4. Modify the Streamlit application code:

    - Replace `"openai.api_type"`, `"openai.api_version"`, and `"openai.api_base"` with your Azure OpenAI API configuration values.
    - Update `"model_name"` with your desired language model name.
    - Modify the `headers` dictionary with your Helicone authentication and user ID values.
    - Adjust the database connection string in `db_string` with your PostgreSQL database details.

5. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Launch the Streamlit app, and you will see a chat input box.

2. Enter your queries or instructions in the chat input box.

3. The assistant will process your input and provide responses. The conversation will be displayed in the Streamlit app.

## Example Database Query

To query your PostgreSQL database, you can use SQL commands. For example:

```sql
SELECT * FROM your_table WHERE column_name = 'value';
```

The assistant will execute the SQL query and provide the results.

Please make sure to handle sensitive data and database credentials securely.

**Note:** If you encounter any issues or have questions, feel free to contact us for support.

---

**Important:** This application is designed for demonstration purposes. Ensure that you follow best practices for security and API key management in production environments.
