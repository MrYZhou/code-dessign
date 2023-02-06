from glob import iglob
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from util.system import Init

app = FastAPI()

Init.do(app)


@app.get("/")
async def index():
    return FileResponse("static/index.html")


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
