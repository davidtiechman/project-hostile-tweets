from app.retcher import load_data, convert_by_df
from collections import Counter
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Analyzer():
    def __init__(self):
        self.mongo = load_data()
        self.df = convert_by_df(self.mongo)

    def rarest_word(self):
        self.df['array_text'] = self.df['Text'].str.split(" ")
        self.df['rarest_word'] = self.df['array_text'].apply(lambda words: Counter(words).most_common()[-1][0])
        return self.df
    def emotion_text(self):
        nltk.download('vader_lexicon')  # Compute sentiment labels
        # tweet = self.df['Text'].loc[0]
        tweet = 'i wolking to israel '
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        pass
    def find_weapon_name(self):
        pass
analyzer = Analyzer()
print(analyzer.rarest_word())
analyzer.emotion_text()