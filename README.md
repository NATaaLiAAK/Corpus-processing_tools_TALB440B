# Corpus-processing_tools_TALB440B
A course in corpus building.
_________________________________________________________
# Outils_de_Traitement_de_corpus_TALB440B
Un cours sur la construction de corpus.


## The "Disaster Tweets" dataset on HuggingFace
_________________________________________________________
## Le dataset "Disaster Tweets" sur HuggingFace

` https://huggingface.co/datasets/venetis/disaster_tweets` 

### Description du corpus

Le dataset "Disaster Tweets" sur HuggingFace, créé et partagé par l'utilisateur "venetis", est une collection de 7 613 tweets provenant de Twitter, étiquetés comme liés à des catastrophes (1) ou non (0) - étiquettes binaires. Il inclut des tweets mentionnant divers types de catastrophes, comme des tremblements de terre, des inondations, des incendies de forêt et des accidents. Le dataset a été créé de manière participative (crowdsourced dataset). Les tweets sont en anglais, identifiés par un ID (1ère colonne) et accompagnés de mots-clés (keywords) (2ème colonne) et d'informations de localisation (location) facultatives (3ème colonne).


### Type de prédiction

#### TÂCHE : Text Classification | Classification de texte

Le dataset est destiné à la tâche de classification de texte (Text Classification). L'objectif de cette tâche est de déterminer la catégorie d'un tweet, en particulier pour entraîner des modèles à distinguer les tweets liés aux catastrophes de ceux qui ne le sont pas (classification binaire).

#### SOUS-TÂCHE : Sentiment Analysis | Analyse de sentiments

Le dataset est également adapté à la sous-tâche d'analyse de sentiments, qui fait partie de la tâche de classification de texte. Il contient des tweets étiquetés pour permettre la classification, déterminant si le ton d'un tweet est positif, négatif ou neutre.


### Modèles utilisés

Le dataset peut servir à entraîner des modèles de classification de texte, comme les modèles de type BERT, RoBERTa ou d'autres modèles de traitement du langage naturel (NLP) utilisés pour la classification de texte et l'analyse de sentiments.


_____________________________________________________________________________________________________________________________________


## WEB SCRAPING | SCRAPING

J'essaie de créer moi-même un dataset similaire à "Disaster Tweets" à partir de **Mastodon**, qui répond à la même tâche et sous-tâche et que j'appelle "Mastodon Disaster Toots". Pour faire cela, je dois faire du scraping. Le *scraping* (ou scrapping) est le processus d'extraction de données de sites web en utilisant des scripts ou des outils automatisés. 


### Voici les étapes à suivre :

> 1. **Accéder à l'API de Mastodon** pour collecter les messages (appelés "*toots*").
> 
> 2. **Filtrer ces toots** pour identifier ceux qui sont liés à des catastrophes.
> 
> 3. **Stocker les données** dans un format structuré, tel qu'un fichier CSV, avec les étiquettes appropriées.


### Étapes préliminaires :

> 1. **Créer un compte sur *Mastodon*** et obtenir <span style="text-decoration: underline;">un jeton d'accès API</span>.
> 
> - Utiliser le *jeton d'accès* et l'*URL de base* de mon instance *Mastodon* pour me connecter à l'*API Mastodon*.
>   
> 2. **Installer les bibliothèques Python nécessaires** :
> 
> ` pip install Mastodon.py pandas `
>
> 3. **Recherche de *toots* avec des *mots-clés* spécifiques** :
>
> - La fonction ` get_toots_with_keywords ` utilise des *mots-clés* liés aux catastrophes pour rechercher des *toots*.
>
> 4. **Création et stockage des données** :
>
> - Les toots sont stockés dans une *liste de dictionnaires* puis convertis en *DataFrame pandas*.
> - Les données sont ensuite sauvegardées dans un *fichier CSV* nommé **Mastodon Disaster Toots**.


## Collecter des toots publics de Mastodon pour constituer mon dataset de données lié aux catastrophes.


Pour **l'étape préliminaire numéro 1**, j'ai dû :

> 1. Créer un compte sur *un serveur Mastodon* de mon choix.
> 
> - *Mastodon* est une fédération de serveurs (instances) indépendants. Je devais choisir un serveur en fonction de mes préférences.
> 
> Parmi les 3 types de serveurs Mastodon :
> - *mastodon.social*
> - *mastodon.xyz*
> - *mastodon.technology*
> 
> j'ai choisi *mastodon.social*. Je suis allée sur la page d'inscription du serveur *mastodon.social* et j'ai créé un compte
> ([le lien vers mon profil](https://mastodon.social/@_naTALia_IA)).
>
> 
> 2. Accéder aux *paramètres* de mon compte et créer une *nouvelle application* pour obtenir un *jeton d'accès API*.
>
> ### Les étapes pour *la création de mon application* dans Mastodon :
>
> Dans les *paramètres* de mon compte Mastodon :
>
> Preferences -> Development -> **New application**
> Préférences -> Développement -> **Nouvelle application**
> 
> - Application name | Nom de l'application : **Disaster Tweets Scraper**
> 
> - Redirect URI | Redirection URL : ` urn:ietf:wg:oauth:2.0:oob ` (utilisé pour les tests locaux) -> Je ne dispose pas d'un serveur de redirection.
>   
> - Scopes (API auxquelles l'application aura accès, les permissions dont j'ai besoin) :
> 
>   - ` read ` : read all your account's data | lire toutes les données de mon compte
>     Essentielle pour lire les *toots* (posts) et accéder aux informations publiques des utilisateurs. C'est la permission principale pour extraire des données. Avec le scope *read* je peux :
>                             1. lire les toots que j'ai publié,
>                             2. accéder aux informations publiques de mon profil et des profils des autres utilisateurs,
>                             3. visualiser mes abonnements et abonnés.
>     
>   - ` read:statuses ` : see all posts | voir tous les posts
>     Permet de lire les toots, ce qui est crucial pour collecter les messages liés aux catastrophes.
>     
>   - ` read:accounts ` : see accounts information | voir les informations des comptes
>     Permet de lire les informations de profil des utilisateurs, telles que le nom d'utilisateur, la localisation (si disponible), etc. Utile pour obtenir des informations contextuelles sur les toots.
>     
> - Additional permissions | Permissions additionnelles :
> 
>   - ` read:notifications ` : see your notifications | voir mes notifications
>     Si j'ai besoin de lire les notifications, bien que ce ne soit généralement pas nécessaire pour constituer un dataset de toots.
> 
>   - ` read:search ` : search on your behalf | rechercher en mon nom
>     Permet de rechercher dans les toots publics. Cette permission est utile pour effectuer des recherches par *mots-clés*.
> 
>   - ` read:follows ` : see your follows | voir mes abonnements
>     Permet de lire les listes de *followers/following*. Cela peut être pertinent si j'ai besoin d'analyser les réseaux de relations entre utilisateurs.
>
>   - ` read:me ` : read only your account's basic information | seulement lire les informations basiques de mon compte
>     Permet d'accéder aux informations de mon propre profil.
>     
>     -> Mon objectif est de scraper des toots publics liés à des catastrophes, je n'ai pas spécifiquement besoin de ce scope.
>     -> Cependant, voici quand le scope "read:me" pourrait être utile :
>     - Si je souhaite obtenir des informations sur mon propre compte Mastodon.
>     - Si mon script nécessite des vérifications ou des actions spécifiques liées à l'utilisateur authentifié.
>     -> Le scope **read:me** n'est pas obligatoire pour ma tâche actuelle, mais je souhaite l'ajouter par précaution ou pour de futurs besoins.
>
> 
> 3. Utiliser ce *jeton d'accès* dans mon **script Python** pour authentifier mes *requêtes API*.
>    
> Après avoir créé l'application, j'ai vu apparaître mon jeton d'accès généré.
>
> Après avoir créé mon application sur Mastodon, j'ai obtenu trois informations importantes :
>
> - **Client Key (Clé client)** : Il s'agit d'un identifiant unique pour mon application. Il est > utilisé pour *identifier* mon application lors de l'interaction avec l'API Mastodon.
> 
> - **Client Secret (Secret client)** : C'est une clé secrète associée à mon application. Elle  > est utilisée pour *authentifier* mon application lors de l'interaction avec l'API Mastodon.
> 
> - **Your Access Token (Votre jeton d'accès)** : C'est le jeton d'accès API qui me permet
> d'authentifier mon application auprès de Mastodon et d'accéder à certaines fonctionnalités de > l'API, en fonction des permissions que j'ai demandées lors de la création de l'application.


## Lire et rechercher des toots publics liés aux catastrophes.

### Utilisation des scopes dans mon script Python *scraper.py* :

```


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

```

#### Explications supplémentaires :

1. **my_profile** : Utilise "read:me" pour obtenir des informations sur mon propre compte.
2. **notifications** : Utilise "read:notifications" pour lire mes notifications.
3. **followers** et **following** : Utilise "read:follows" pour obtenir les listes de mes followers et des comptes que je suis.

Ces ajouts peuvent enrichir mon analyse et fournir des données supplémentaires intéressantes.


- J'exécute le script : `python scraper.py` que je stocke dans **scripts**



## Étapes pour traiter les données et les stocker dans data/processed/

- J'ai créé le répertoire `data/processed/` :

`mkdir -p data/processed/`


- Ensuite, j'ai traité les données.


Les **3 fichiers CSV** du dossiers **data** ne sont pas visibles, puisqu'ils sont dans le fichier *.gitignore*.


### Dans le script Python *process_data.py*, les opérations suivantes sont effectuées :

  1. **Suppression des doublons** : Les doublons sont supprimés à l'aide de la méthode `drop_duplicates()` de pandas.

  2. **Nettoyage du texte** :
     
   - Conversion du texte en minuscules.
   - Suppression des mentions d'utilisateur (@username) à l'aide d'expressions régulières.
   - Suppression des liens URL à l'aide d'expressions régulières.
   - Suppression des caractères spéciaux et de la ponctuation à l'aide d'expressions régulières.
     
  3. **Tokenization** :
    - Utilisation de la bibliothèque *NLTK* pour diviser le texte en mots ou tokens.
    - Suppression des mots vides de la liste de tokens à l'aide d'une liste prédéfinie de mots vides en anglais.

  4. **Stemming** :
     - Réduction des mots à leur forme de base (racine) à l'aide de l'algorithme de stemming de Porter.
       
  5. **Sauvegarde des données nettoyées** :
     - Les données nettoyées sont enregistrées dans un nouveau fichier CSV dans le répertoire de sortie spécifié.



- J'exécute le script Python *process_data.py*, lequel je stocke également dans **scripts** :
  
  `python process_data.py`



### Le script Python *sentiment_analysis.py* effectue les opérations suivantes :

1. **Chargement des données nettoyées** : Les données nettoyées sont chargées à partir d'un fichier CSV spécifié.

2. **Analyse des sentiments** : Une fonction *analyze_sentiment* est définie pour analyser le sentiment de chaque texte à l'aide de la bibliothèque *TextBlob*. Le score de polarité est calculé pour chaque texte, et le sentiment est déterminé comme *positif*, *négatif* ou *neutre* en fonction du score.

3. **Application de l'analyse des sentiments** : L'analyse des sentiments est appliquée à chaque texte dans le *DataFrame* à l'aide de la fonction définie précédemment.
   
4. **Enregistrement des résultats** : Les données, y compris les résultats de l'analyse des sentiments, sont enregistrées dans un nouveau fichier CSV.

5. Affichage du chemin du fichier de sortie : Un message est affiché pour indiquer où les résultats de l'analyse des sentiments ont été enregistrés.
   

- J'exécute le script Python *sentiment_analysis.py*, lequel je stocke toujours dans **scripts** :

  `python sentiment_analysis.py`




## Configuration du projet

#### J'ai mis dans le fichier `config.py` mon _URL de base Mastodon_ et mon _jeton d'accès API_.

En isolant les informations sensibles dans un fichier de configuration séparé, je maintiens une séparation claire entre le code de mon application et les données sensibles. Cela facilite la gestion des informations sensibles et réduit les risques de divulgation accidentelle.



## requirements.txt

#### Le fichier `requirements.txt` est utilisé pour répertorier toutes les dépendances requises pour exécuter correctement mon application ou projet Python. Voici ce que font les trois packages listés dans mon fichier _requirements.txt_ :

1. **Mastodon.py** : Il s'agit d'une bibliothèque Python pour interagir avec l'API Mastodon, qui est utilisée dans mon script pour collecter des toots à partir de l'instance Mastodon.
   
2. **pandas** : Pandas est une bibliothèque Python populaire pour la manipulation et l'analyse des données. Elle est utilisée dans mon script pour convertir les données récupérées en un DataFrame, une structure de données tabulaire puissante.
   
3. **textblob** : TextBlob est une bibliothèque Python pour le traitement du langage naturel (NLP). Elle fournit des outils pour la classification de texte, l'analyse de sentiments, la tokenisation, la lemmatisation, et d'autres tâches NLP. Dans mon cas, je l'utilise pour l'analyse de sentiments des toots récupérés à partir de Mastodon.


- Ensuite, j'ai lancé la commande ` pip install -r requirements.txt ` pour installer les dépendances.



## .gitignore

#### Dans le fichier `.gitignore` j'ai mis les informations suivantes :

`# Ignore les fichiers de configuration contenant des informations sensibles`

`config.py`


`# Ignore les fichiers de données brutes`

`data/raw/*`


`# Ignore les fichiers de données traitées`

`data/processed/*`


`# Ignore le fichier .DS_Store généré par macOS`
`# Ce fichier est spécifique à macOS et stocke les métadonnées du dossier, telles que la position des icônes et des vignettes.`
`# Il n'est pas nécessaire dans le cadre de mon projet et peut être ignoré.`

`.DS_Store`


- Avant de pousser des dossiers vers le dépôt distant, il faut bien vérifier que les choses à ignorer sont à ignorer. Sinon, des fichiers indésirables seront visibles partout dans les dossiers.

