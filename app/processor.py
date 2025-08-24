from nltk.sentiment import vader
import os
from app.retcher import load_data, convert_by_df
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Analyzer():
    def __init__(self):
        self.mongo = load_data()
        self.df = convert_by_df(self.mongo)
        self.df = self.df.head(100)

    def rarest_word(self):
        self.df['array_text'] = self.df['Text'].str.split(" ")
        self.df['rarest_word'] = self.df['array_text'].apply(lambda words: Counter(words).most_common()[-1][0])
        return self.df

    def emotion_text(self):
        nltk.download('vader_lexicon')  # Compute sentiment labels
        # tweet = self.df['Text'].loc[0]
        self.df['score'] = self.df['Text'].apply(lambda text: vader.SentimentIntensityAnalyzer().polarity_scores(str(text))['compound'])
        self.df['type_text'] = self.df['score'].apply(lambda s: 'positive' if s >= 0.5 else ('negative' if s <= -0.5 else 'neutral'))
        self.df.drop(columns=['score'], inplace=True)
        return self.df

    def find_weapon_name(self):
        self.df['weapons_detected'] = self.df.apply(self.lop_of_array_weapons, axis=1)
        return self.df
    def lop_of_array_weapons(self,row):
        arr_weapon = []
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, 'data', 'weapon_list.txt')

        with open(file_path, 'r') as file:
            arr_weapon = file.read().split('\n')
        for w in arr_weapon:
            if w in row['array_text']:
                return w
        return ""




analyzer = Analyzer()
analyzer.rarest_word()
print(analyzer.find_weapon_name())