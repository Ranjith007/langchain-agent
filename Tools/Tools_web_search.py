# tools/web_search.py
import os
from dotenv import load_dotenv
load_dotenv()
import requests

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def web_search_tool_fn(query: str) -> str:
    """
    Simple SerpAPI wrapper using 'serpapi' HTTP interface.
    Returns short concatenation of top organic results' snippets.
    """
    if not SERPAPI_KEY:
        return "Error: SERPAPI_API_KEY not set."

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }
    try:
        r = requests.get("https://serpapi.com/search", params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        organic = data.get("organic_results", [])[:5]
        snippets = []
        for o in organic:
            txt = o.get("snippet") or o.get("title") or ""
            if txt:
                snippets.append(txt.strip())
        return "\n\n".join(snippets) if snippets else "No direct results."
    except Exception as e:
        return f"Search error: {e}"
