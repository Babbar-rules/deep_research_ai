from tavily import TavilyClient
from config import TAVILY_API_KEY
from langchain.schema import HumanMessage

def research_agent(state):
    client = TavilyClient(api_key=TAVILY_API_KEY)
    # Extract the last user message content
    last_message = state["messages"][-1].content if isinstance(state["messages"][-1], HumanMessage) else ""
    
    
    search_results = client.search(
        query=last_message,
        search_depth="advanced"
        )
    structured_results=[]
    if "results" in search_results:
        for result in search_results["results"][:5]:  # Limit to top 5 results
            structured_results.append({ 
                "title": result.get("title", "No Title"),
                "url": result.get("url", "No URL"),
                "snippet": result.get("snippet", "No Summary")
             })
     
    return {"search_results": search_results}