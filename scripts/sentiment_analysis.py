import pandas as pd
from textblob import TextBlob

# Charger les données nettoyées depuis le fichier CSV
df = pd.read_csv('../data/processed/cleaned_mastodon_disaster_toots.csv')

# Fonction pour effectuer l'analyse des sentiments sur un texte
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Appliquer l'analyse des sentiments à chaque texte dans le DataFrame
df['sentiment'] = df['cleaned_text'].apply(analyze_sentiment)

# Enregistrer les données avec les résultats de l'analyse des sentiments dans un nouveau fichier CSV
output_path = '../data/processed/sentiment_data.csv'
df.to_csv(output_path, index=False)

print(f"Les résultats de l'analyse des sentiments ont été enregistrés dans {output_path}")
