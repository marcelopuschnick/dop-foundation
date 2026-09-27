"""
Compila MusicRegistry.sol e faz deploy no Ganache local.
"""
import json
from pathlib import Path
from web3 import Web3
from solcx import compile_standard, install_solc

RPC_URL = "http://127.0.0.1:8545"
RAIZ = Path(__file__).parent.parent
CONTRATO_SOL = RAIZ / "contracts" / "MusicRegistry.sol"
CONTRATO_JSON = RAIZ / "contracts" / "MusicRegistry.json"

VERSAO_SOLC = "0.8.19"

print("=" * 60)
print("DEPLOY MusicRegistry - FUNDACAO DOP")
print("=" * 60)

try:
    install_solc(VERSAO_SOLC)
    print(f"\n[1/5] Solidity {VERSAO_SOLC} instalado")
except Exception:
    print(f"\n[1/5] Solidity ja instalado")

print(f"\n[2/5] Compilando {CONTRATO_SOL.name}...")
codigo_fonte = CONTRATO_SOL.read_text()

compilado = compile_standard(
    {
        "language": "Solidity",
        "sources": {"MusicRegistry.sol": {"content": codigo_fonte}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode.object"]}
            }
        },
    },
    solc_version=VERSAO_SOLC,
)

abi = compilado["contracts"]["MusicRegistry.sol"]["MusicRegistry"]["abi"]
bytecode = compilado["contracts"]["MusicRegistry.sol"]["MusicRegistry"]["evm"]["bytecode"]["object"]

CONTRATO_JSON.write_text(json.dumps({"abi": abi, "bytecode": bytecode}, indent=2))
print(f"      ABI e bytecode salvos em {CONTRATO_JSON.name}")

print(f"\n[3/5] Conectando em {RPC_URL}...")
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    print("ERRO: Nao conectou no Ganache. Ele esta rodando?")
    exit(1)

print(f"      Conectado. Chain ID: {w3.eth.chain_id}")

print(f"\n[4/5] Fazendo deploy...")
conta = w3.eth.accounts[0]
w3.eth.default_account = conta

MusicRegistry = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = MusicRegistry.constructor().transact({"from": conta})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

endereco = tx_receipt.contractAddress
print(f"      Deploy concluido!")
print(f"      Endereco do contrato: {endereco}")
print(f"      Bloco: {tx_receipt.blockNumber}")

ENDERECO_JSON = RAIZ / "contracts" / "endereco.json"
ENDERECO_JSON.write_text(json.dumps({"endereco": endereco}, indent=2))
print(f"\n[5/5] Endereco salvo em {ENDERECO_JSON.name}")

print("\n" + "=" * 60)
print("DEPLOY CONCLUIDO COM SUCESSO")
print("=" * 60)