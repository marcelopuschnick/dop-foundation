# 🚨 [CRITICAL] Bug que Exige Ação Imediata

> ⚠️ Este template é para bugs **bloqueantes** ou **de segurança**.  
> Para bugs menores, use [bug.md](./bug.md)

---

## Alerta de Segurança

**Selecione o tipo:**

- [ ] 🐛 Bug funcional (o app quebra/sobra)
- [ ] 💸 Perda financeira (perca tokens/recursos)
- [ ] 🔒 Vulnerabilidade de segurança
- [ ] ⚠️ Falha crítica de dados (vazamento/pérdida)

---

## Impacto Crítico

**Por que isso exige ação imediata?**

```text
[Explain why this requires immediate attention]
Example: "O app não conecta no Ganache, impedindo todas as operações"
```

**Dados em risco?**

- [ ] Sim — [descrever dados expostos/perdidos]
- [ ] Não — apenas funcionalidade quebrada

---

## Reprodução Imediata

### Minimizar para reproduzir:

1. [ ] Rodar `ganache` (se aplicável)
2. [ ] Navegar até `/status` no dashboard
3. [ ] Verificar console do navegador (F12)
4. [ ] Tentar registrar nova obra
5. [ ] Erro ocorre: `[colar erro completo]`

### Stack Trace Completo:

```text
[Colar stack trace ou logs do terminal aqui]
```

---

## Diagnóstico Inicial

**Testes realizados:**

- [ ] Python versão correta (`python --version`)
- [ ] `pip freeze > requirements.txt` sincronizado
- [ ] Ambiente virtual ativado (`.venv/Scripts/Activate.ps1`)
- [ ] Ganache rodando (acessar http://localhost:8545/)
- [ ] IPFS Kubo rodando (verificar `/ipfs` endpoint)

**Resultado:**

- [ ] Todos OK — bug é no código, não configuração
- [ ] Falha de instalação — seguir [01-infraestrutura/01-instalacao.md](../01-infraestrutura/01-instalacao.md)

---

## Comportamento Observado vs. Esperado

| Campo | Observado | Esperado |
|-------|-----------|----------|
| **Funcionalidade** | `[ex: upload arquivo FLAC]` | `[ex: arquivo aparece na blockchain]` |
| **Erro** | `[mensagem de erro completa]` | `[sem erro, sucesso]` |

---

## Ambiente Técnico (Obrigatório)

```bash
# Rodar no terminal e colar output
python --version  # Ex: Python 3.10.11
pip --version     # Ex: pip 23.0.1
streamlit --version  # Ex: Streamlit/Elementary 1.28.0
ganache --version   # Se usar localmente

# Output:
# Python 3.10.11 (pyenv-win)
# pip 23.0.1
# Streamlit CLI 1.28.0
```

---

## Logs Completos (se houver)

**Terminal do Python:**

```text
[Colar output completo de python scripts/*.py]
```

**Console do Navegador (F12 → Console):**

```text
[Colar mensagens JS se aplicável]
```

---

<div style="background:#8b0000; color:#fff; padding:16px; border-radius:8px; margin-top:32px;">
  <h3 style="margin:0 0 8px 0;">🔥 Ação Imediata Requerida</h3>
  <p style="margin:0;">Nossos mantenedores priorizarão este bug nas próximas horas. Contribuidores experientes podem aplicar hotfix diretamente!</p>
</div>

---

## 📝 Ao Aplicar Hotfix

Se você for corrigir o bug, siga:

1. Branch: `hotfix/[descrever-problema-breve]`
2. Teste localmente primeiro (`pytest`)
3. Commit message: `[hotfix] corrigir [problema] — ver #ISSUE-NUMBER`
4. Pull Request com referenciando a issue crítica

---

## 🙏 Agradecimento por Reportar

```
Obrigado por ajudar a manter a DOP Foundation estável!

Cada bug reportado faz o projeto melhor e mais seguro para artistas.
```
