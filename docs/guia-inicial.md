# 🎵 Guia Inicial — Começando com DOP Foundation

## Olá, Artista! 👋

Você vai distribuir sua primeira música na **DOP Foundation**? Vamos te guiar em 5 passos simples.

---

## 📋 Pré-requisitos

### O Que Você Precisa Ter:

- ✅ **Computador** — Windows 10/11, Mac OS ou Linux
- ✅ **Python 3.10+** — Roda `python --version`
- ✅ **git** (opcional) — Para baixar código
- ✅ **Docker Desktop** (se usar containerização)

### Se Já Tem Tudo:

```bash
# Verificar Python
python --version      # Esperado: Python 3.10.11 ou superior

# Verificar pip (gerenciador Python)
pip --version         # Ex: pip 23.0.1

# Instalar se precisar:
https://www.python.org/downloads/
```

---

## 🚀 Instalação em 3 Passos

### Passo 1: Clonar ou Baixar o Projeto

**Opção A — Clone do GitHub:**

```bash
git clone https://github.com/SEU_USUARIO/dop-foundation.git
cd dop-foundation
```

**Opção B — ZIP:**

1. Vá no repo no GitHub → Green button "Code" → Download ZIP
2. Extrair em pasta local
3. Continuar neste guia

---

### Passo 2: Configurar Ambiente Virtual

```bash
# Criar ambiente isolado
python -m venv .venv

# Ativar (Windows PowerShell)
.venv\Scripts\Activate.ps1  # Se der erro, rode: Set-ExecutionPolicy RemoteSigned

# Verificar se ativou — Deve ver (.venv) no prompt
```

### Passo 3: Instalar Dependências

```bash
# Instalar bibliotecas Python
pip install -r requirements.txt

# Output esperado:
# Collecting fastapi...done
# Installing build dependencies...done
# ...
Successfully installed web3 ipfshttpclient...
```

✅ **Pronto!** Agora você pode rodar o dashboard.

---

## 🎨 Rodando o Dashboard

```bash
streamlit run dashboard/app.py
```

O app abre em https://localhost:8501 (ou porta disponível).

### Primeiro Acesso ao Dashboard:

1. **Ver status do sistema** — API, Blockchain, Carteira
2. **Princípios inegociáveis** — Conheça a filosofia DOP
3. **Módulos ativos** — Veja o que está rodando

---

## ⛓️ Configurar Blockchain Local

### Ganache (Blockchain de Teste):

```bash
# 1. Instalar Ganache:
choco install ganache       # Windows
brew install ganache        # Mac OS

# 2. Iniciar
ganache

# 3. Clique em "QUICKSTART" na interface
# 4. Abra https://localhost:8545/ e clique "Start Private Network"
```

### IPFS Kubo (Armazenamento):

```bash
# Opção A — Usar serviço cloud (simples)
export IPFS_API=https://ipfs.cloudflare.com

# Opção B — Instalar Kubo localmente (recomendado)
ipfs-kubo install
ipfs daemon

# Verificar:
ipfs version   # Ex: 0.19.0
ipfs cat /
```

---

## 🎵 Upload e Registro de Sua Primeira Obra

### Passo a Passo Visual:

#### 1. Preparar Arquivo FLAC

```bash
# Converter WAV para FLAC (alta qualidade)
flac -8 master_da_obra.wav -o master_da_obra.flac

# Verificar qualidade:
metaflac master_da_obra.flac --show-tag
# Ou usar ferramenta visual como MediaInfo
```

#### 2. Upload para IPFS

```bash
ipfs add master_da_obra.flac

# Output:
# Added QmXyZ...abc123456789 /home/artist/master_da_obra.flac

# COPIAR CID (Content Identifier): QmXyZ...abc123456789
```

#### 3. Registrar na Blockchain

Abra o dashboard em https://localhost:8501 e use a aba **"OBRAS REGISTRADAS"** para registrar:

- **Nome da obra:** "Canção do Vale"
- **Artista:** "Seu Nome Aqui"  
- **CID/IPFS:** `QmXyZ...abc123456789`
- **Preço:** 0.5 tokens (ajustável)

Clique em **"REGISTRAR NA BLOCKCHAIN"**!

---

## ✅ Verificação de Registro

Após registro:

1. Ir ao [Ganache Explorer](https://localhost:8547)
2. Buscar no evento `ObraRegistrada`
3. Confirmar hash IPFS do arquivo

```text
✅ Obra registrada!
- CID/IPFS: QmXyZ...
- Hash blockchain: 0x1a2b3c...
- Dono: Sua carteira Ethereum
```

---

## 🎯 Próximo Passo: Marketplace

Agora que sua obra está registrada, você pode:

- 🔗 **Configurar página de venda**
- 💰 **Definir preço em tokens/USD**
- 👥 **Compartilhar link com fãclub**

---

## 🆘 Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| `python: command not found` | Instalar https://www.python.org/downloads/ |
| Ambiente virtual não ativa | Rode `.venv\Scripts\Activate.ps1` de novo |
| Ganache não conecta | Abra http://localhost:8545 e clique "Start Private Network" |
| IPFS upload falha | Verifique `export IPFS_API=http://127.0.0.1:5001` no .env |
| Error: Contract not deployed | Rode `python scripts/deploy_registry.py` |

### Logs para Debugging:

```bash
# Ver logs do Python
tail -f app/logs/*.log

# Ver logs do Ganache (no explorer)
http://localhost:8547

# Ver logs do IPFS
ipfs daemon --enable-gc
```

---

## 🎉 Parabéns!

Você acaba de distribuir sua primeira obra na DOP Foundation!

**O que você conquistou:**

- ✅ Obra registrada na blockchain (imutável e auditável)
- ✅ Arquivo FLAC em IPFS (descentralizado e persistente)
- ✅ Controle total sobre seu preço e distribuição

---

## 🌐 Compartilhamento Público

Agora compartilhe:

1. **Dashboard online**: https://dop-foundation.streamlit.app/
2. **Página da obra**: Link único por CID/IPFS
3. **Redes sociais**: "Minha música está na DOP Foundation!"

---

## 🤝 Contribua!

Gostou? Quer fazer o próximo passo com sua obra?

- Fork este repo → https://github.com/SEU_USUARIO/dop-foundation
- Crie issue ou PR → https://github.com/SEU_USUARIO/dop-foundation/issues
- Discuta na comunidade — [Discord em breve]

---

<div style="background: linear-gradient(180deg, #FF00FF, #FF6B00); padding:24px; text-align:center; margin-top:32px;">
  <h3 style="color:#fff; margin:0 0 16px 0;">🎵 Você está no movimento!</h3>
  <p style="color:#fff; font-size:14px;">DOP Foundation — Código aberto • Dados portáveis • FLAC de altíssima qualidade</p>
</div>

---

<div style="text-align:center; color:#666; margin-top:24px;">
  <small>&copy; 2026 DOP Foundation | MIT License | Documentação em constante evolução</small>
</div>
