from fastapi import FastAPI
from app import config

app = FastAPI(
    title="Fundação DOP",
    description="Infraestrutura soberana de distribuição musical",
    version="0.1.0",
)

@app.get("/")
def raiz():
    return {
        "fundacao": "DOP",
        "versao": "0.1.0",
        "ambiente": config.AMBIENTE,
        "rede": config.REDE,
        "chain_id": config.CHAIN_ID,
    }

@app.get("/status")
def status():
    return {
        "status": "ok",
        "mensagem": "Sistema DOP operacional",
    }