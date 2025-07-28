import os
import shutil
import subprocess
from web_search import search_duckduckgo

def ask_llm(user_query):
    # Vérifie si Ollama est installé
    if not shutil.which("ollama"):
        return " Erreur : le programme 'ollama' n'est pas trouvé sur le système."

    # Fait une recherche sur le Web avec SerpAPI
    web_info = search_duckduckgo(user_query)

    # Construit le prompt à envoyer au modèle
    prompt = f"""
Tu es un assistant IA local. Voici des informations trouvées en ligne :

{web_info}

Ta tâche : répondre de manière claire à cette question :
{user_query}

Réponse :
""".strip()

    try:
        print(" Prompt envoyé à Ollama :")
        print(prompt)

        # Lance le modèle avec subprocess + encodage UTF-8
        result = subprocess.run(
            ['ollama', 'run', 'mistral'],
            input=prompt.encode('utf-8'),         # encode en UTF-8
            capture_output=True                   # récupère la réponse
        )

        # Vérifie s’il y a eu une erreur
        if result.returncode != 0:
            return f" Erreur Ollama : {result.stderr.decode('utf-8', errors='ignore')}"

        # Renvoie la réponse correctement décodée
        return result.stdout.decode('utf-8', errors='ignore').strip()

    except Exception as e:
        return f" Erreur exécution via subprocess : {str(e)}"
