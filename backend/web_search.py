import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Charger la clé API depuis le fichier .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def search_duckduckgo(query):
    if not SERPAPI_KEY:
        return "❌ Clé API SerpAPI non trouvée."

    try:
        # Configuration de la requête
        search = GoogleSearch({
            "q": query,
            "api_key": SERPAPI_KEY,
            "num": 5,  # Nombre de résultats
            "hl": "fr",  # Langue française
        })

        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        # Construire un résumé textuel
        if not organic_results:
            return "❌ Aucun résultat trouvé."

        summary = ""
        for item in organic_results:
            title = item.get("title", "Sans titre")
            link = item.get("link", "Pas de lien")
            snippet = item.get("snippet", "Pas de description.")
            summary += f"- 📌 **{title}**\n  🔗 {link}\n  📝 {snippet}\n\n"

        return summary.strip()

    except Exception as e:
        return f"❌ Erreur SerpAPI : {str(e)}"
