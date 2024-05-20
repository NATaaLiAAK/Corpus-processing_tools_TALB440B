import sys
import os
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Charger les données brutes depuis le fichier CSV
df = pd.read_csv('../data/raw/mastodon_disaster_toots.csv')

# Supprimer les doublons
df.drop_duplicates(inplace=True)

# Nettoyage du texte
def clean_text(text):
    # Convertir le texte en minuscules
    text = text.lower()
    # Supprimer les mentions d'utilisateur (@username)
    text = re.sub(r'@[^\s]+', '', text)
    # Supprimer les liens URL
    text = re.sub(r'http\S+', '', text)
    # Supprimer les caractères spéciaux et la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text

df['cleaned_text'] = df['content'].apply(clean_text)

# Tokenization
stop_words = set(stopwords.words('english'))
def tokenize_text(text):
    tokens = word_tokenize(text)
    # Supprimer les mots vides
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

df['tokens'] = df['cleaned_text'].apply(tokenize_text)

# Stemming
stemmer = PorterStemmer()
def stem_text(tokens):
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

df['stemmed_tokens'] = df['tokens'].apply(stem_text)

# Définir le répertoire de sortie
output_dir = '../data/processed/'

# Enregistrer les données nettoyées dans un nouveau fichier CSV
df.to_csv(output_dir + 'cleaned_mastodon_disaster_toots.csv', index=False)

