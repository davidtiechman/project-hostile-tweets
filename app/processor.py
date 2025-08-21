from nltk.sentiment import vader
from app.retcher import load_data, convert_by_df
from collections import Counter
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
        self.df['score'] = self.df['Text'].apply(lambda text: vader.SentimentIntensityAnalyzer().polarity_scores(str(text))['compound'])
        self.df['type_text'] = self.df['score'].apply(lambda s: 'positive' if s >= 0.5 else ('negative' if s <= -0.5 else 'neutral'))
        self.df.drop(columns=['score'], inplace=True)
        return self.df
    def find_weapon_name(self):
        arr_weapon = []
        with open('../data/weapon_list.txt', 'r') as file:
            for name_weapon in file.readlines():
                nwe_name = name_weapon.strip('\n')
                arr_weapon.append(nwe_name)
            for name in arr_weapon:
                if name not in self.df.index:
                    self.df['weapons_detected'] = ''
                elif name in self.df.index:
                    self.df['weapons_detected'] += name + ' '
        print(arr_weapon)
        print(self.df['weapons_detected'])
        print(self.df.columns)
         # self.df['Text']
        # pass
analyzer = Analyzer()
# analyzer.rarest_word()
# analyzer.emotion_text()
analyzer.find_weapon_name()