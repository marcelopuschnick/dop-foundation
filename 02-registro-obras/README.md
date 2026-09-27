# 📜 Módulo 2 — Registro de Obras

## Onde as obras ganham vida immutável na blockchain

---

## O Que Aqui

É aqui que **cada obra musical** é registrada de forma soberana e auditável:

- ✅ Hash do arquivo FLAC registrado on-chain
- ✅ Metadados completos (nome, artista, preço)
- ✅ Link para IPFS (armazenamento descentralizado)
- ✅ Timestamp de criação imutável
- ✅ Propriedade intransferível até venda

---

## 🎯 Fluxo de Registro

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Arquivo FLAC   │───>│  Hash IPFS      │───>│ Smart Contract   │
│  (Master)       │    │  (CID v0)       │    │  MusicRegistry   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 📋 Estrutura de Dados

Cada obra registrada contém:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | uint256 | Identificador único autoincremental |
| `nome` | string | Título da obra musical |
| `artista` | string | Nome do artista criador |
| `hashArquivo` | string | CID/IPFS ou hash SHA-256 |
| `preco` | uint256 | Preço de venda em tokens |
| `dono` | address | Endereço da carteira |
| `criadoEm` | timestamp | Data e hora de registro |

---

## 🚀 Exemplo de Registro

```bash
# 1. Preparar arquivo FLAC
flac -8 master_da_obra.wav -o master_da_obra.flac

# 2. Hash do arquivo
sha256sum master_da_obra.flac

# 3. Upload para IPFS
ipfs add master_da_obra.flac
CID: QmXyZ...abc123

# 4. Registrar na blockchain
python scripts/register_obra.py \
  --nome "Canção do Vale" \
  --artista "NomeArtista" \
  --hashArquivo "QmXyZ...abc123" \
  --preco "500000000000000000"  # 0.5 tokens
```

---

## 📝 Contrato Solidity

O contrato `MusicRegistry.sol` gerencia:

- ✅ Registro de obras (`registrar()`)
- ✅ Consulta de obra por ID (`obterObra(uint256)`)
- ✅ Contagem total (`contar()`)
- ✅ Eventos para auditoria (`ObraRegistrada`)

---

## 🔍 Auditoria em Tempo Real

Todo registro é auditável:

```solidity
event ObraRegistrada(
    uint256 indexed id,
    string nome,
    string artista,
    address indexed dono
);
```

Qualquer pessoa pode verificar:

1. Ir ao explorador de blocos (Ganache/Amoy)
2. Buscar no evento `ObraRegistrada`
3. Confirmar hash IPFS e dados da obra

---

## 🌟 Próximo Passo

Após registro na blockchain, a obra vai para:

- **Módulo 3 — Marketplace** → Compra/venda FLAC direto no navegador
- **Módulo 4 — Splits** → Distribuição automática de comissões
- **Dashboard DOP** → Visualização pública da obra

---

<div style="background: linear-gradient(180deg, #FF00FF, #FF6B00); padding:24px; text-align:center; margin-top:32px;">
  <h3 style="color:#fff; margin:0 0 16px 0;">🎵 Pronto para registrar sua primeira obra?</h3>
  <p style="color:#fff; margin:0; font-size:14px;">Acesse o dashboard e faça seu upload!</p>
</div>
