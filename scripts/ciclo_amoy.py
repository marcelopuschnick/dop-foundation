"""
Ciclo validado na blockchain local (Ganache).
Le bloco atual, saldo da carteira, e confirma conexao.
"""
from web3 import Web3

# Conecta no Ganache local
RPC_URL = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    print("ERRO: Nao conectou no Ganache. Ele esta rodando?")
    print("Abra o Ganache e clique em QUICKSTART")
    exit(1)

print("=" * 50)
print("CICLO BLOCKCHAIN LOCAL - FUNDACAO DOP")
print("=" * 50)

print(f"\nRede conectada: {w3.is_connected()}")
print(f"Chain ID: {w3.eth.chain_id}")
print(f"Bloco atual: {w3.eth.block_number}")

# Cole aqui o endereco da primeira conta do Ganache
ENDERECO = "0x7C074A6d216b53a78d457857d320764B5a7f0A09"

if ENDERECO != "0xSeuEnderecoAqui":
    saldo_wei = w3.eth.get_balance(ENDERECO)
    saldo_eth = w3.from_wei(saldo_wei, "ether")
    print(f"\nEndereco: {ENDERECO}")
    print(f"Saldo: {saldo_eth} ETH")

    # Lista todas as contas disponiveis
    print(f"\nContas disponiveis no Ganache:")
    for i, conta in enumerate(w3.eth.accounts[:3]):
        saldo = w3.from_wei(w3.eth.get_balance(conta), "ether")
        print(f"  [{i}] {conta} - {saldo} ETH")
else:
    print("\nAVISO: Cole um endereco real do Ganache em ENDERECO")

print("\n" + "=" * 50)