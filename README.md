# Corpus-processing_tools_TALB440B
A course in corpus building.
________________________________________________________
# Outils_de_Traitement_de_corpus_TALB440B
Un cours sur la construction de corpus.


## The "Disaster Tweets" dataset on HuggingFace
________________________________________________________
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


