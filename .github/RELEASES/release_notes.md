# 📝 Release Notes para DOP Foundation

---

## Template de Release

```markdown
# v[NOME]-v[NÚMERO] — [DATA/ANO-MS]

**Data de Lançamento:** `[DD/MM/YYYY]`  
**Versão anterior:** `vNOME-vNUMBER`  
**Chain ID:** `80002 (Polygon Amoy)`  
**Status:** ✅ Estável | ⚠️ Beta | 🔨 RC

---

## 🎉 Destaques desta Versão

### ✨ Novidades

- [ ] `[Feature] Nova funcionalidade: descrição em 1 linha`
  - Benefício do usuário
  - Detalhes técnicos se necessário
  
- [ ] `[Docs] Tutorial novo/Tradução adicionada`
  - Link para tutorial
  - Idiomas disponíveis

- [ ] `[Design] Melhoria de UI: `[descrição breve]`  
    - Ex: "Cards de obra com hover neon mais intenso"
    - Ex: "Degradés rosa→laranja ajustados"

### 🐛 Correções

- [ ] Corrigido erro de upload no IPFS Kubo local
- [ ] Fixed bug de hash invalido rejeitando uploads válidos
- [ ] Melhorado performance na listagem de obras

### 🔒 Segurança

- [ ] Atualizado `web3.py` para versão mais segura
- [ ] Sanitização de inputs melhorada contra XSS
- [ ] Removido debug logging exposto em produção

---

## 📊 Métricas (se aplicável)

```text
Artistas registrados: X → Y (+Z%)
Obras distribuídas: A → B (+C obras)
Valor retido por artistas: R$ X → R$ Y
```

---

## 🔧 Mudanças Técnicas

### Código

- `app/main.py`: `[descrever alteração]`
- `dashboard/app.py`: `[melhoria visual/UI]`
- `contracts/MusicRegistry.sol`: `[otimização ou nova função]`

### Dependências

| Pacote | Versão Antiga | Nova | Motivo |
|--------|--------------|------|--------|
| `web3.py` | `6.0.0` | `6.1.0` | Correção segurança |
| `streamlit` | `1.28.0` | `1.29.0` | Melhorias de UI |

### Banco de Dados

- `[Novas colunas/tabelas adicionadas]`
- `[Migrações: X → Y]`

---

## ⚠️ Notas para Usuários

**Quebras de Compatibilidade:**

> "Nenhuma mudança nesta versão. Tudo funciona igual."  
> Ou listar quebra se houver:  
> - Removida função `obter_obra_antiga()` — migre para `obterObra(uint256)`

**Novos Requisitos:**

- Python 3.10+ (mantido)
- Docker Desktop v28+ (atualizado de v27)

**Migração Necessária:**

```bash
# Se adicionou nova coluna no banco:
python scripts/migrate_nova_coluna.py

# Atualizar dashboard para usar novas classes CSS
streamlit run dashboard/app.py
```

---

## 🔗 Links Relacionados

- Issue resolvida: `#ISSUE-123`
- Pull Request mergeado: `#PR-456`
- Tutorial correspondente: `[docs/NOVA-GUIA.md]`

---

## 🙏 Agradecimentos a Contribuidores desta Versão

Obrigado para:

- @[usuario1]: por implementar feature X
- @[usuario2]: por reportar bug Y
- @[usuario3]: por revisar código Z

---

## 📜 Licença

MIT — Código aberto e gratuito.

**Agradecemos sua contribuição para a DOP Foundation!**
