# Instalação e Verificação — Stack Python

Este arquivo verifica o que já está instalado na máquina e
instala apenas o que falta. O stack é 100% Python: uma
linguagem só, pastas limpas, zero labirinto.

---

## 1. Verificação rápida

Abra o PowerShell e rode os comandos abaixo, um por vez.

### Python

    python --version

Esperado: Python 3.10.x ou superior

### pip (gerenciador de pacotes)

    pip --version

Esperado: pip 23.x ou superior

### Git

    git --version

Esperado: git version 2.XX.X

### Docker (opcional por enquanto)

    docker --version

Esperado: Docker version XX.X.X (só se já tiver instalado)

---

## 2. Resultado na máquina atual

Verificado em 26/09/2026:

| Ferramenta | Versão | Status |
|---|---|---|
| Docker | 29.5.2 | OK |
| Docker Compose | v5.1.4 | OK |
| Git | 2.51.0 | OK |
| Python | 3.10.11 (pyenv-win) | OK |
| pip | 23.0.1 | OK |

Tudo instalado. Nada a fazer nesta seção.

Node.js e npm também estão instalados, mas não serão usados
neste projeto. O stack é Python puro.

---

## 3. Configuração do Git

Depois de confirmar que o Git está instalado, configure
sua identidade:

    git config --global user.name "Seu Nome"
    git config --global user.email "seu@email.com"

E a branch padrão:

    git config --global init.defaultBranch main

---

## 4. Criar o ambiente virtual do projeto

Ambiente virtual é uma pasta isolada onde as bibliotecas do
projeto ficam. Não mistura com o Python do sistema. É limpo.

Na raiz do projeto:

    cd C:\Users\marce\dop-foundation
    python -m venv .venv

Isso cria uma pasta `.venv` dentro do projeto. É lá que as
bibliotecas vão morar.

### Ativar o ambiente virtual

    .\.venv\Scripts\Activate.ps1

Se aparecer `(.venv)` no começo da linha do PowerShell,
funcionou.

### Se der erro de permissão

Rode uma vez:

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Confirme com "S" e tente ativar de novo.

---

## 5. Instalar as bibliotecas do projeto

Com o ambiente virtual ativado (tem que ter o `(.venv)` no
prompt), instale tudo de uma vez:

    pip install fastapi uvicorn streamlit web3 ipfshttpclient eth-ape python-dotenv

Isso pode demorar alguns minutos. É normal.

### O que cada uma faz

| Biblioteca | Função |
|---|---|
| fastapi | Backend / API do sistema |
| uvicorn | Servidor que roda o FastAPI |
| streamlit | Dashboard visual (a interface bonita) |
| web3 | Conversa com a blockchain |
| ipfshttpclient | Conversa com o IPFS (FLAC) |
| eth-ape | Compila e faz deploy de contratos Solidity |
| python-dotenv | Lê configurações de arquivo .env |

---

## 6. Congelar as dependências

Para que qualquer pessoa reproduza o ambiente:

    pip freeze > requirements.txt

Isso cria um arquivo `requirements.txt` com a lista exata
das bibliotecas instaladas. Quem quiser montar o projeto
roda `pip install -r requirements.txt` e tem tudo igual.

---

## 7. Verificação final

Com o ambiente virtual ativado, rode:

    python --version
    pip --version
    streamlit --version
    python -c "import web3; print(web3.__version__)"

Se os quatro retornarem versão sem erro, o ambiente está
pronto.

---

## 8. Como desativar e reativar o ambiente virtual

Quando terminar de trabalhar:

    deactivate

Para entrar de novo:

    cd C:\Users\marce\dop-foundation
    .\.venv\Scripts\Activate.ps1

---

## 9. Próximo passo

Com o ambiente Python montado, o próximo arquivo é
`02-estrutura-projeto.md`, onde organizamos as pastas
internas em Python puro: `app/`, `contratos/`, `dados/`,
`dashboard/`, `config/`.

Antes de seguir, garanta que:
- `(.venv)` aparece no prompt
- `pip freeze` gerou o `requirements.txt`
- Os quatro comandos da seção 7 retornaram versão