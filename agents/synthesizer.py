from langchain.schema import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = google_api_key

llm= ChatGoogleGenerativeAI(model= "gemini-2.0-flash")

SYSTEM_PROMPT = """You are an answer drafting assistant. Your role is to:
1. Synthesize information from provided search results
2. Draft clear, well-structured responses
3. Maintain factual accuracy based on the given context
4. Organize information in a logical flow
5. Highlight key points and conclusions

Please draft your answers accordingly."""

def synthesis_agent(state):
    # Combine search results with conversation
    context = f"Based on this information: {state['search_results']}, please provide a response."
    # Create a proper message list
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"] + [SystemMessage(content=context)]
    response = llm.invoke(messages)
    return {"messages": response}