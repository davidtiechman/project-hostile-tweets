import fastapi

from app.manager import Wires_to_json
from app.processor import Analyzer

app = fastapi.FastAPI()
@app.get("/")
def read_root():
    try:
        analyzer = Analyzer()
        analyzer.rarest_word()
        analyzer.emotion_text()
        df = analyzer.find_weapon_name()
        wired = Wires_to_json()
        wired.write_to_json(df)
    except Exception as e:
        raise e
