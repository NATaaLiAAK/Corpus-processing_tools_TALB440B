
import sys
import os
from mastodon import Mastodon
import pandas as pd

# Ajouter le dossier parent au sys.path pour permettre l'importation de config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer le module config
from config import config

# Connect to Mastodon API
mastodon = Mastodon(
    access_token=config.ACCESS_TOKEN,  # Mon jeton d'accès API
    api_base_url=config.BASE_URL  # L'URL de mon instance Mastodon
)

# Fonction pour récupérer des toots contenant des mots-clés spécifiques
def get_toots_with_keywords(keywords, max_toots=1000):
    toots = []
    for keyword in keywords:
        max_id = None
        count = 0
        while count < max_toots:
            results = mastodon.search_v2(q=keyword, max_id=max_id)
            if 'statuses' not in results:
                break  # Sortir de la boucle si aucun résultat trouvé
            for status in results['statuses']:
                toots.append({
                    'id': status['id'],
                    'content': status['content'],
                    'keyword': keyword,
                    'location': status['account']['location'] if 'location' in status['account'] else None,
                    'is_disaster': 1  # Étiqueter manuellement les toots liés aux catastrophes avec 1
                })
                count += 1
                if count >= max_toots:
                    break  # Sortir de la boucle si le nombre maximum de toots récupérés est atteint
            if 'next' not in results.get('links', {}):
                break  # Sortir de la boucle si aucun lien vers la page suivante n'est disponible
            max_id = results['statuses'][-1]['id']  # Récupérer l'ID du dernier toot pour la pagination
    return toots



# Liste de mots-clés liés aux catastrophes
disaster_keywords = ['earthquake', 'flood', 'wildfire', 'accident']

# Collecter les toots
toots = get_toots_with_keywords(disaster_keywords)

# Convertir en DataFrame
df = pd.DataFrame(toots)

# Chemin du dossier parent de scripts
parent_folder = os.path.dirname(os.path.abspath(__file__))

# Chemin du dossier de données
data_folder = os.path.join(parent_folder, "..", "data", "raw")

# Créer le répertoire s'il n'existe pas
os.makedirs(data_folder, exist_ok=True)

# Enregistrer dans un fichier CSV
df.to_csv(os.path.join(data_folder, 'mastodon_disaster_toots.csv'), index=False)

# Exemples d'utilisation des permissions supplémentaires
# Lire les informations de mon propre profil
my_profile = mastodon.account_verify_credentials()
print(f"My profile: {my_profile}")

# Lire mes notifications
notifications = mastodon.notifications()
print(f"Notifications: {notifications}")

# Lire mes followers
followers = mastodon.account_followers(my_profile['id'])
print(f"Followers: {followers}")

# Lire les comptes que je suis
following = mastodon.account_following(my_profile['id'])
print(f"Following: {following}")
