# 🎉 Pull Request para DOP Foundation

> "Contribuições são as melhores forma de evoluir comunitariamente!"

---

## ✨ O Que Este PR Adiciona

**Breve descrição do que esta mudança faz:**

```text
[Em 1-2 linhas: o que este PR adiciona/altera/corrigiu]
Ex: "Adicionar validação de hash SHA-256 no upload de arquivos FLAC"
```

---

## ✅ Checklist Antes de Submeter

- [ ] Teste localmente (roda sem erro?)
- [ ] Código segue estilo PEP 8
- [ ] Strings em português (ou inglês claro)
- [ ] Docs atualizadas se necessário
- [ ] Testes criados/atuais (`pytest`)
- [ ] Mensagens de erro amigáveis

---

## 🎯 Objetivo do PR

**Por que esta mudança é necessária?**

> "Explique o problema resolvido e benefício"

### Problema Anterior:

```text
[Descrever situação antes deste PR]
Ex: "Arquivos eram aceitos sem verificação de hash, permitindo uploads falsos"
```

### Solução Implementada:

```text
[Como isso foi resolvido]
Ex: "Adicionei verificação de hash SHA-256 no upload e rejeição automática se inválido"
```

---

## 📋 Tipo de PR

**Selecione uma:**

- [ ] ✨ **Feature Nova** — Adiciona funcionalidade (nova, não quebrar existente)
- [ ] 🐛 **Bug Fix** — Corrigir problema existente
- [ ] 🔧 **Refatoração** — Melhorar código sem mudar comportamento
- [ ] 📖 **Docs** — Melhorar documentação
- [ ] 🧪 **Testes** — Adicionar testes unitários/integração
- [ ] ⚙️ **Configuração** — Mudanças de ambiente/Docker/etc

---

## 💻 Código Alterado

| Arquivo | Tipo de Mudança | Descrição |
|---------|-----------------|-----------|
| `arquivo.py` | `[adicionou/removo/mudou]` | `[explicar o que mudou]` |
| `arquivo.md` | `[atualizado]` | `[o que mudou na doc]` |

### Diff Principal:

```diff
@@ -1,5 +1,7 @@
 # Exemplo de diff do arquivo
 def funcao():
+    # Nova validação adicionada
     if condicao:
         return True
-    else:
+    elif condicao2:
+        return False
     return None
```

---

## 🧪 Testes Adicionados

Se aplicável, listar novos testes:

```bash
# Localmente teste com:
pytest tests/test_arquivo.py -v

# Output esperado:
# test_validacao_hash PASSED (0.23s)
# test_upload_falso_rejeitado PASSED (0.18s)
# test_upload_valido ACEITO PASSED (0.21s)
```

---

## 🎨 Design/Visual (se UI/UX)

**Screenshots antes/depois:**

| Antes | Depois |
|-------|--------|
| ![Antes](link.png) | ![Depois](link.png) |

**Alterações visuais:**

- [ ] Novo componente/adicionando elemento
- [ ] Cor/estilo alterado (ex: degradê neon mais intenso)
- [ ] Layout mudado (cards de obra mais legíveis)

---

## 🔒 Segurança

**Revisão de segurança:**

- [ ] Não expõe dados sensíveis em logs
- [ ] Validação de inputs completa
- [ ] Não quebra autenticação/autorização
- [ ] Tratamento correto de exceptions

---

## 📈 Impacto

| Aspecto | Impacto |
|---------|---------|
| **Novas features** | `adiciona X novas funcionalidades` |
| **Performance** | `[melhora/piora/mesmo]` — explicação se mudar |
| **Compatibilidade** | Não quebra (ou lista o que quebra) |
| **Complexidade** | Simplifica ou adiciona complexidade? |

---

## 🎤 Mensagem Final no PR

```markdown
## ✅ Pronto para Revisão

Esta mudança:
- [ ] Resolve problema descrito acima
- [ ] Segue código de contribuição da DOP Foundation
- [ ] Mantém princípios inegociáveis do projeto
- [ ] Não adiciona vulnerabilidades de segurança

**Testado em:**
- Python 3.10.11
- Ganache local rodando
- IPFS Kubo ativo

Agradeço à equipe pela revisão! 🎵
```

---

<div style="background:linear-gradient(180deg, #FF00FF, #FF6B00); color:#fff; padding:24px; border-radius:12px; margin-top:32px;">
  <h3 style="margin:0 0 16px 0;">🤝 Vamos Colaborar!</h3>
  <p style="margin:0; font-size:15px;">Seu PR será revisado em até 48 horas. Contribuições bem escritas são priorizadas, mesmo sem experiência prévia!</p>
</div>

---

## 📜 Ao Mergear

**Após aprovação:**

```bash
git checkout main
git pull origin main
git branch -d feature/seu-branch  # apaga seu branch antigo
git merge feature/seu-branch
# ou rebase para histórico limpo
git push origin main
```

Obrigado pela contribuição! 🎵
