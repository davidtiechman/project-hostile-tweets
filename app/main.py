import fastapi
import os

from starlette.responses import FileResponse

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
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.csv')
        df.to_csv(file_path, index=False, encoding='utf-8')
        return FileResponse(file_path, media_type='text/csv', filename="data.csv")
    except Exception as e:
        raise e
