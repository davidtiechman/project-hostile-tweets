import pymongo
import pandas as pd
def load_data():
    myclient = pymongo.MongoClient(host="mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
    mydb = myclient["IranMalDB"]
    mycol = mydb["tweets"]
    mongo = mycol.find()
    return mongo

def convert_by_df(mongo):
    mongo = list(mongo)
    df = pd.DataFrame(mongo)
    return df