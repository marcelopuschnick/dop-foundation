# 🤝 Contribuindo para a DOP Foundation

## Bem-vindo!

Agradecemos seu interesse em contribuir para a **Fundação DOP**! Estamos construindo algo incrível juntos.

---

## 🎯 Como Ajudar

### ✅ Tipos de Contribuição

| Área | O Que Você Pode Fazer |
|------|------------------------|
| 💻 **Código** | Novas funcionalidades, refatoração, testes |
| 🎨 **Design** | Melhorias de UI/UX, temas alternativos |
| 📖 **Documentação** | Tutoriais, traduções, exemplos práticos |
| 🐛 **Issues** | Reportar bugs, pedir melhorias |
| 💭 **Discussão** | Sugestões no GitHub Discussions |

### ✅ Código de Conduta

Nossa comunidade é baseada em:

- 🤝 **Respeito**: Tratar sempre com consideração
- 🔒 **Transparência**: Decisões abertas e claras
- ⚖️ **Meritocracia**: Contribuições avaliadas por mérito técnico

---

## 🚀 Primeiros Passos

### 1. Fork do Repositório

```bash
git clone https://github.com/SEU_USUARIO/dop-foundation.git
cd dop-foundation
```

### 2. Criar Branch Pessoal

```bash
git checkout -b feature/nova-funcionalidade
# ou
git checkout -b bug/relatar-problema-XYZ
```

**Nomeação de branches:**

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| Feature | `feature/titulo-minusculos` | `feature/marketplace-flac` |
| Bug fix | `bug/corrigir-issue-N` | `bug/fatal-calc-splits` |
| Docs | `docs/nova-guia-XYZ` | `docs/tutorial-ipfs-upload` |
| Testes | `test/cobertura-api` | `test/integration-blockchain` |

---

## 📝 Desenvolvimento

### 1. Configurar Ambiente

```bash
python -m venv .venv
source .venv/Scripts/Activate.ps1  # Windows
pip install -r requirements.txt
streamlit run dashboard/app.py
```

### 2. Estilo de Código Python

Seguir [PEP 8](https://pep8.org/) com:

- 4 espaços por tabulação
- `import` em linhas separadas
- Strings com aspas duplas
- Tipo hints onde aplicável

```python
def registrar_obra(nome: str, artista: str) -> bool:
    """Registra obra na blockchain.

    Args:
        nome: Título da obra musical
        artista: Nome do criador

    Returns:
        True se registro bem-sucedido
    """
    ...
```

### 3. Testes

Criar testes em `tests/`:

```python
# tests/test_registry.py
import unittest
from contracts.MusicRegistry import registrar_obra


class TestRegistroObras(unittest.TestCase):
    
    def test_registrar_obra_valida(self):
        resultado = registrar_obra(
            nome="Exemplo",
            artista="TestArtist"
        )
        self.assertTrue(resultado)
```

Roda: `pytest`

---

## 🎨 Melhores Práticas de Contribuição

### Review do Código

Seu PR será revisado por mantenedores com foco em:

- ✅ **Correção**: Respeita os princípios da DOP
- ✅ **Performance**: Code review para eficiência
- ✅ **Clean code**: Sem duplicação excessiva
- ✅ **Documentação**: Strings explicativas claras

**Não se preocupe:** feedback é construtivo, não pessoal.

### Pull Requests Ideais

PRs bem feitos:

1. Descrevem o problema em 2-3 linhas
2. Explicam a solução (com diff do código)
3. Adicionam testes se aplicável
4. Atualizam documentação
5. Mantêm tamanho enxuto (<400 linhas ideais)

### Revisão por Pares

Todos podem revisar! Dê feedback útil:

- ✅ "Funciona perfeitamente" + sugestões de melhoria
- ❌ Evite "Isso está ruim, mude aqui"
- 💡 Sugira alternativas em vez de impor

---

## 🐛 Reportar Bugs

Use issue template quando reportar bug:

```markdown
## Descreva o Bug

**O que aconteceu:** [Sintoma observado]

**Passos para reproduzir:**
1. Fazer X na interface
2. Clicar em Y no dashboard
3. Ver erro Z no console

**Comportamento esperado:** [O que deveria acontecer]

**Captura de tela:** [Link se necessário]

## Contexto Técnico (opcional)

- Versão Python: 3.10.x
- Ganache rodando? Sim/Não
- Mensagem de erro completa: ...
```

---

## 📚 Melhorias à Documentação

Tutoriais são a melhor forma de crescer juntos!

### Criar Tutorial

Template ideal:

```markdown
# Tutorial: Registrar Sua Primeira Obra

## Pré-requisitos

- Python 3.10+ instalado
- Docker Desktop rodando
- Ganache com QUICKSTART

## Passo a Passo

### 1. Preparar Arquivo FLAC

```bash
flac -8 master.flac -o master.flac.8
```

### 2. Upload para IPFS

```bash
ipfs add master.flac.8
CID: QmABC...xyz
```

### 3. Registrar na Blockchain

Edite `.env`:

```ini
IPFS_API=http://127.0.0.1:5001
DATABASE_URL=sqlite:///dados/dop.db
```

Rode registro via CLI ou dashboard!

## Resultado

Sua obra agora está registrada na blockchain da DOP Foundation.
```

---

## 📋 Checklist do PR

Antes de submeter seu PR:

- [ ] Branch nomeada corretamente
- [ ] Testes passando (`pytest -v`)
- [ ] Código formatado (`black .` se usar)
- [ ] Strings de erro em português (ou inglês claro)
- [ ] README atualizado (se nova funcionalidade)
- [ ] `.env` não versionado (.env.example sim!)

---

## 🙏 Agradecimento Final

```
Seu tempo e contribuição contam!

Cada pull request, issue reportado ou tutorial escrito torna a DOP melhor.

Vamos fazer isso juntos. 🎵
```

---

## 📬 Duvidas?

- 💬 Discord: `https://discord.gg/DOPFOUNDATION` *(em breve)*
- 🐦 Twitter/X: `@DOPFoundation` *(em breve)*
- 📧 Email: `contato@dop-foundation.com` *(em breve)*

**Abra uma issue se precisar de ajuda!**

---

<div style="text-align:center; margin-top:32px;">
  <p>Feito com ❤️ por artistas, devs e entusiastas</p>
  <small>&copy; 2026 DOP Foundation | Código Aberto | MIT License</small>
</div>
