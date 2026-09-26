import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
RAIZ = Path(__file__).parent.parent
load_dotenv(RAIZ / "config" / ".env")

# Ambiente
AMBIENTE = os.getenv("AMBIENTE", "desenvolvimento")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Blockchain
REDE = os.getenv("REDE", "polygon-amoy")
RPC_URL = os.getenv("RPC_URL", "https://rpc-amoy.polygon.technology/")
CHAIN_ID = int(os.getenv("CHAIN_ID", "80002"))

# IPFS
IPFS_API = os.getenv("IPFS_API", "http://127.0.0.1:5001")

# Banco
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dados/dop.db")

# IA
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")