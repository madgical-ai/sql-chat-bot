# LangChain SQL Chat Assistant

> *Ask your database questions in plain English. No SQL knowledge required — just type "Show me last month's sales" and get instant answers.*

A Streamlit-powered chatbot that converts natural language queries into SQL, executes them against your PostgreSQL database, and returns results in a conversational interface. Built with LangChain and Azure OpenAI.

---

## The Problem It Solves

Accessing database insights requires SQL expertise — a blocker for most team members:

- **Marketing teams** can't answer "Which products sold best this week?"
- **Sales leads** can't get "Deals closed by region" without analyst help
- **Operations** wait hours/days for data requests
- **Everyone** relies on a small group of people who know SQL

This chatbot democratizes data access — anyone can ask questions and get answers.

| | Before | After |
|---|---|---|
| **Time to insight** | Hours to days | Instant |
| **SQL knowledge required** | Yes | No |
| **Query accuracy** | Analyst-dependent | AI-verified |
| **Availability** | 9-5 analyst | 24/7 chatbot |

---

## How It Works

```
User Question (Natural Language)
    │
    ▼
[1] Intent Detection     → Classify: query, analysis, action
    │
    ▼
[2] SQL Generation    → LangChain + Azure OpenAI → SQL query
    │
    ▼
[3] Query Validation → Syntax + safety checks
    │
    ▼
[4] Execute Query   → PostgreSQL
    │
    ▼
[5] Result Formatting → Tabular + natural language summary
```

### Key Technical Decisions

1. **LangChain SQLAgent** — Handles multi-step queries with automatic retries
2. **Schema-aware Prompting** — Includes table structures in prompt for accurate SQL generation
3. **Query Validation Layer** — Prevents dangerous operations (DROP, unauthorized accesses)
4. **Result Summarization** — Converts raw SQL results into readable insights

---

## Project Structure

```
sql-chat-bot/
├── app.py                  # Streamlit application
├── prompts.py              # SQL generation prompts
├── database.py           # SQLAlchemy connection
├── validators.py        # Query safety checks
└── requirements.txt
```

---

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_VERSION=2023-03-15-preview
export OPENAI_KEY=your_azure_key
export OPENAI_URL_BASE=https://your-resource.openai.azure.com/

# Run the app
streamlit run app.py
```

---

## Usage

1. Open the Streamlit app at `http://localhost:8501`
2. Type your question in natural language
3. View SQL-generated results and conversational answers

### Example Queries

- "Show me all orders from last month"
- "Which customers have the highest total purchase value?"
- "List products that haven't been ordered in 30 days"

---

## Production Deployment

1. **Authentication**: Add Azure AD or SSO for enterprise use
2. **Rate Limiting**: Prevent excessive API calls
3. **Query Logging**: Track common queries for prompt improvements
4. **Read Replicas**: Route read queries to replicas for performance

---

## License

MIT License