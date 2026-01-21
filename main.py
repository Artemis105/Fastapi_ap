from fastapi import FastAPI
import plots

app = FastAPI(title="Function Plot API")

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(plots.router)


