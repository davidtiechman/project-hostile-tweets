import json
import os
from app.processor import Analyzer

class Wires_to_json:
    def __init__(self):
        self.analyzer = Analyzer()

    def write_to_json(self,df):
        results = []
        for index, row in df.iterrows():
            result = {'id' : str(row['_id']),
            'original_text':  row['Text'],
            'rarest_word' : row['rarest_word'],
            'sentiment' : row['type_text'],
            'weapons_detected ' : row['weapons_detected']
                  }
            results.append(result)
        with open('data.json', 'w') as js:
            json.dump(results, js, ensure_ascii=False, indent=4)



