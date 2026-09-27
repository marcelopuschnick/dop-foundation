# 🎵 DOP FOUNDATION
## Infraestrutura Soberana de Distribuição Musical

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Solidity](https://img.shields.io/badge/Solidity-0.8.19-green) ![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub](https://img.shields.io/github/languages/count/mariuzzo/dop-foundation)

<div style="margin-top:20px;">
  <a href="#dop-foundation" style="text-decoration:none; display:inline-block; margin:8px;"><img src="https://img.shields.io/badge/-DOCUMENTAÇÃO-orange?logo=github-readme&style=flat-square" height="30"></a>
  <a href="#contribua" style="text-decoration:none; display:inline-block; margin:8px;"><img src="https://img.shields.io/badge/-COLABORE-verde?logo=github&style=flat-square" height="30"></a>
  <a href="#demo" style="text-decoration:none; display:inline-block; margin:8px;"><img src="https://img.shields.io/badge/-DEMO-roxo?logo=streamlit&style=flat-square" height="30"></a>
</div>

**Devolver ao artista e à sociedade o controle, a transparência e o retorno econômico da música.**

</div>

---

## ✨ O Que É

A **Fundação DOP** é uma infraestrutura soberana de distribuição musical que revoluciona como artistas distribuem sua obra:

- 🎼 **100% soberano**: Artista dono do master e define o preço
- ⚡ **Splits automáticos**: Distribuição auditável em tempo real
- 🔒 **Blockchain local**: Ganache para testes, Polygon Amoy para produção
- 💿 **FLAC de altíssima qualidade**: Armazenamento IPFS descentralizado
- 🤖 **IA conselheira**: Auxilia sem substituir a decisão humana
- 📜 **Código aberto**: Todo o sistema open source e auditável

---

## 🎨 [LIVE DEMO](https://dop-foundation.streamlit.app/)

<div style="display:flex; gap:16px; justify-content:center; margin:32px 0;">
  <a href="https://dop-foundation.streamlit.app/" target="_blank" style="text-decoration:none;">
    <div style="background: linear-gradient(135deg, #FF00FF 0%, #FF6B00 100%); padding:24px 48px; border-radius:12px; color:#fff; font-weight:bold; text-align:center; box-shadow:0 10px 40px rgba(255,0,255,0.3);">
      🚀 ACESSAR DEMO ONLINE<br>
      <span style="font-size:14px; font-weight:normal;">(Interface Cyberpunk Dark Mode)</span>
    </div>
  </a>
</div>

---

## 🏗️ Arquitetura Soberana

```
┌─────────────────────────────────────────────────────────────┐
│                    DOP FOUNDATION ARCHITECTURE                │
├─────────────────────────────────────────────────────────────┤
│  🔧 INFRAESTRUTURA (Módulo 1)                                │
│     ├─ Docker Desktop + Compose                              │
│     ├─ IPFS Kubo (Armazenamento descentralizado)             │
│     ├─ Hardhat (Blockchain local)                            │
│     └─ Python 3.10+ Stack                                    │
├─────────────────────────────────────────────────────────────┤
│  🎵 REGISTRO DE OBRAS (Módulo 2)                             │
│     ├─ MusicRegistry.sol                                      │
│     └─ IPFS hashing para arquivos FLAC                        │
├─────────────────────────────────────────────────────────────┤
│  💰 SPLITS & TESOURARIA (Módulo 4)                           │
│     ├─ Cálculo automático de comissões                       │
│     └─ Fundo comunitário obrigatório                          │
├─────────────────────────────────────────────────────────────┤
│  🏛️ GOVERNANÇA ON-CHAIN (Módulo 5)                           │
│     ├─ Colégios de artistas                                   │
│     ├─ Sistema de vetos                                       │
│     └─ Propostas comunitárias                                 │
├─────────────────────────────────────────────────────────────┤
│  🤖 IA CONSELHEIRA (Módulo 6)                                │
│     ├─ Ollama local                                           │
│     └─ Análise contextual sem privacidade comprometida       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Princípios Inegociáveis

> "Não é tecnologia, é filosofia com código."

- ✅ **Artista é dono do master** e define o preço final
- ✅ **Nenhum intermediário com poder de veto**
- ✅ **Split automático e auditável em tempo real**
- ✅ **Fundo comunitário obrigatório em cada venda**
- ✅ **Governança com colégios e veto real**
- ✅ **IA conselheira, nunca soberana**
- ✅ **Código aberto e dados portáveis**
- ✅ **FLAC de altíssima qualidade**
- ✅ **Fallback apenas comunitário**
- ✅ **Retorno social mensurável e publicado**

---

## 🚀 Instalação Rápida

```bash
# 1. Clonar o repo
git clone https://github.com/SEU_USUARIO/dop-foundation.git
cd dop-foundation

# 2. Ativar ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Instalar dependências
pip install fastapi uvicorn streamlit web3 ipfshttpclient eth-ape python-dotenv

# 4. Configurar blockchain local
ganache && ganache:8545

# 5. Rodar dashboard
streamlit run dashboard/app.py
```

---

## 📁 Estrutura do Projeto

```
dop-foundation/
├── 00-fundacao/          # Identidade, princípios, governança
├── 01-infraestrutura/    # Docker, IPFS, Hardhat setup
├── 02-registro-obras/    # Contratos de registro
├── 03-marketplace/       # Compra/venda FLAC
├── 04-splits-tesouraria/ # Cálculos e tesouraria
├── 05-governanca-onchain/# Colégios, vetos, propostas
├── 06-ia-conselheira/    # Agente local de análise
├── 07-auditoria/         # Dashboard e transparência
├── 08-retorno-social/    # Métricas de impacto
├── app/                  # API FastAPI
├── contracts/            # Contratos Solidity
├── dashboard/            # Interface Streamlit (DARK CYBERPUNK!)
├── scripts/              # Automação e testes
└── docs/                 # Documentação completa
```

---

## 🎮 Demo: Blockchain Validada!

<div style="background:#1a1a2e; padding:24px; border-radius:12px; margin:32px 0;">
  <div style="color:#FF6B00; font-size:18px; margin-bottom:16px;">
    ⛓️ CICLO BLOCKCHAIN LOCAL VALIDADO
  </div>
  <ul style="color:#fff; line-height:2;">
    <li>✅ Ganache rodando e respondendo</li>
    <li>✅ Carteira lendo saldo em tempo real</li>
    <li>✅ Contrato compilado e pronto para deploy</li>
    <li>✅ Upload/download de arquivos FLAC testado</li>
  </ul>
  <div style="margin-top:16px; color:#FF00FF; font-weight:bold;">
    👉 A obra foi registrada! Veja na interface.
  </div>
</div>

---

## 🤝 Contribua

A **DOP Foundation** é um projeto open source e queremos sua ajuda!

<a id="contribua"></a>

### Como Colaborar

1. **Fork** este repositório
2. Crie seu branch: `git checkout -b feature/sua-melhoria`
3. Faça commit: `git commit -m 'feat: adicionar sua melhoria'`
4. Push e crie um Pull Request!

```bash
git checkout -b feature/nova-funcionalidade
# faça suas alterações
git commit -am 'feat: nova funcionalidade para artists'
git push origin feature/nova-funcionalidade
```

### Áreas de Contribuição

- 🔨 **Novos módulos**: Sugira funcionalidades (marketplace, auditoria, etc)
- 🎨 **Melhorias de UI/UX**: Refinamos cada pixel do dashboard
- 📖 **Documentação**: Traduções, tutoriais e exemplos
- 🔬 **Testes**: Unit tests, integration tests para segurança

### Código de Conduta

Respeito, transparência e meritocracia em todas as contribuições.

---

## 💻 Tech Stack

| Tecnologia | Versão | Licença |
|------------|--------|---------|
| Python | 3.10+ | MIT |
| FastAPI | Latest | BSD |
| Streamlit | Latest | Apache |
| Solidity | 0.8.19 | GPL |
| Hardhat | Latest | MIT |
| IPFS Kubo | Latest | Apache |
| Web3.py | Latest | Apache |

---

## 📊 Status do Desenvolvimento

<div style="margin:40px 0;">
  <div style="margin-bottom:20px; color:#FF6B00;"><strong>Módulo Ativo</strong></div>
  <ul style="color:#fff; line-height:1.8;">
    <li style="background:rgba(255,0,255,0.1); padding:16px; border-radius:8px; margin-bottom:12px; display:block;">
      <strong>✅ Módulo 0 — Fundação</strong><br>
      <small>Identidade, princípios, governança (DNA do projeto)</small>
    </li>
    <li style="background:rgba(255,107,0,0.2); padding:16px; border-radius:8px; margin-bottom:12px; display:block;">
      <strong>🔧 Módulo 1 — Infraestrutura</strong><br>
      <small>Docker, IPFS, Hardhat configurados e testados</small>
    </li>
    <li style="background:rgba(128,128,128,0.1); padding:16px; border-radius:8px; margin-bottom:12px; display:block;">
      <strong>⏳ Módulos 2-8</strong><br>
      <small>Prioridade para desenvolvimento colaborativo</small>
    </li>
  </ul>
</div>

---

## 📚 Licença & Créditos

```text
MIT License

Copyright (c) 2026 DOP Foundation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🎤 Sobre o Projeto

A Fundação DOP nasceu de uma pergunta simples: **"Por que os artistas perdem controle sobre sua própria música?"**

Nossa resposta foi criar uma infraestrutura onde:
- O artista **mantém todo o valor** do seu trabalho
- A comunidade **participa das decisões** através da governança on-chain
- Cada venda **retorna parte para o coletivo**

---

## 🔗 Links Úteis

- 🌐 [Demo Online](https://dop-foundation.streamlit.app/)
- 📖 [Documentação](./docs/) *(em construção)*
- 💬 [Discord/Forum de Discussão](#) *(em breve)*
- 🐦 [Twitter/X](#) *(em breve)*

---

<div style="margin-top:48px; padding-top:32px; border-top:1px solid #333; text-align:center; color:#666;">
  <p>Feito com ❤️ por uma comunidade de artistas, desenvolvedores e entusiastas</p>
  <p><small>&copy; 2026 DOP Foundation | Código Aberto | Dados Portáveis | FLAC de Altíssima Qualidade</small></p>
</div>

---

## 🏷️ Tags

`#music` `#blockchain` `#opensource` `#web3` `#flac` `#ipfs` `#solidity` `#docker` `#python` `#streamlit` `#artist-owned`
