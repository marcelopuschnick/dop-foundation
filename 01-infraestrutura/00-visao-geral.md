# Módulo 1 — Infraestrutura Local

Este módulo monta o chão onde tudo vai rodar. Sem ele, nenhum
contrato funciona, nenhum FLAC é armazenado, nenhuma venda é
simulada. É o alicerce técnico da fundação.

O objetivo é ter um ambiente reproduzível na máquina local,
usando apenas ferramentas gratuitas e auditáveis.

---

## 1. Componentes

### Hardhat
Framework de desenvolvimento Ethereum que roda uma rede
blockchain local. Permite escrever, testar e fazer deploy de
contratos Solidity sem gastar dinheiro real.

- **Papel:** rede local, compilação, testes, deploy
- **Custo:** gratuito, código aberto
- **Substituto em produção:** Polygon Amoy (testnet pública)

### IPFS Kubo
Sistema de armazenamento distribuído. Guarda os arquivos FLAC
fora da blockchain (que é cara para arquivos grandes) e
registra apenas o hash on-chain.

- **Papel:** armazenamento dos FLAC, entrega ao comprador
- **Custo:** gratuito, código aberto
- **Vantagem:** arquivo não fica preso a nenhum servidor central

### Docker
Container que amarra tudo em um ambiente isolado e
reproduzível. Garante que o sistema rode igual em qualquer
máquina, sem depender de configuração manual.

- **Papel:** orquestração dos serviços
- **Custo:** gratuito para uso pessoal
- **Vantagem:** um comando sobe tudo

### Polygon Amoy (Testnet)
Rede pública de teste compatível com Ethereum. Serve para
simular o comportamento real em uma blockchain pública,
sem custo financeiro.

- **Papel:** testnet de validação
- **Custo:** gratuito (tokens de teste via faucet)
- **Chain ID:** 80002

---

## 2. Estrutura de pastas do módulo
01-infraestrutura/
├── 00-visao-geral.md <- este arquivo
├── 01-instalacao.md <- instalar Docker, Node, Hardhat
├── 02-docker-compose.md <- subir os serviços
├── 03-hardhat-config.md <- configurar rede local
├── 04-ipfs-config.md <- subir nó IPFS
├── 05-verificacao.md <- testar se tudo funciona
└── 06-troubleshooting.md <- problemas comuns

text

Cada arquivo é curto, direto e cumpre uma etapa. Nada de
"pular para o final". Cada um prepara o próximo.

---

## 3. O que NÃO entra neste módulo

- Contratos de música (Módulo 2)
- Marketplace (Módulo 3)
- Splits (Módulo 4)
- Governança (Módulo 5)
- IA conselheira (Módulo 6)

Este módulo é só chão. Depois a gente constrói em cima.

---

## 4. Pré-requisitos

- Windows 10/11 com PowerShell 7
- Docker Desktop instalado
- Node.js 20 LTS ou superior
- Git instalado
- Ollama rodando (já temos)
- Sublime para editar arquivos (já temos)

O próximo arquivo (`01-instalacao.md`) verifica o que já está
instalado e instala o que falta.

---

## 5. Princípios que este módulo respeita

- **Código aberto:** todas as ferramentas são open source
- **Soberania local:** nada depende de serviço pago
- **Reprodutibilidade:** qualquer pessoa monta igual
- **Auditabilidade:** tudo é inspecionável
- **Sem lock-in:** se uma ferramenta falhar, outra substitui

---

## 6. Próximo passo

Depois de salvar este arquivo, o próximo é `01-instalacao.md`,
que verifica Docker, Node, Git e prepara o terreno para o
`docker-compose.yml`.