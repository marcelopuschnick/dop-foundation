# 🎭 MOCKUP PARA DEMONSTRAÇÃO DA DOP FOUNDATION

## Objetivo

Criar um **mockup visual impactante** para apresentação pública, showcase em eventos, pitch decks ou vídeo demonstrativo.

---

## 📋 Cenário da Demonstração

### Contexto Narrativo

> **"Imagine que você é um artista independente. Você gravou seu primeiro álbum em casa, mas quer distribuí-lo sem perder controle e ter transparência total. Conheça a DOP Foundation."**

---

## 🎬 Roteiro de Demonstração (5-7 minutos)

### Parte 1: O Problema (1 min)

```
🎤 NARRATIVA:
"Você trabalha meses na sua música. Grava, produz, mixa... 
Mas quando vai distribuir? Grandes distribuidoras pegam 30%,
cobram de você e escondem seus splits com managers, selos, etc."

❌ SITUATION ATUAL:
- Perde até 80% do valor da sua música
- Sem transparência nos splits
- Não é dono completo do seu trabalho
```

### Parte 2: Solução DOP (1 min)

```
🎤 NARRATIVA:
"A DOP Foundation inverte essa lógica. Você:
✅ É dono do master sempre
✅ Define o preço final
✅ Splits automáticos em tempo real
✅ Blockchain auditável por qualquer pessoa"
```

### Parte 3: Demo Visual (2-3 min)

#### Passo a passo na interface Streamlit:

1. **Abrir dashboard** — https://dop-foundation.streamlit.app/
   - Mostrar identidade visual DOP DARK CYBERPUNK
   - Títulos neon laranja/rosa saturados
   - Fundo preto, texto Montserrat white

2. **Ver status do sistema**
   - Cards de módulos (DNA, Infraestrutura, Próximos)
   - Princípios inegociáveis em cards com hover
   - Status do ciclo técnico (API, Blockchain, Carteira)

3. **Obras registradas** (MOCKUP!)
   ```python
   # Adicionar obras mockadas para mostrar impacto visual
   - "Nebulosa Violeta" - ArtistaNova
   - "Ritmos da Aurora" - ElétricaMúsica
   - "Sinfonia Digital" - OrquestraVirtual
   ```

4. **Princípios visuais**
   - Degradês neon intensos (rosa→laranja)
   - Fontes em caixa alta
   - Bordes brilhantes

5. **Status dos módulos**
   - Módulo 0: ✅ DNA completo
   - Módulo 1: 🔧 Em execução com ganache rodando
   - Módulos 2-8: 🔮 Próximos passos

---

## 🎨 Elementos Visuais para Mockup

### Cards de Obras (MOCKUP)

Criar cards visuais com dados fictícios para demonstração:

| Campo | Exemplo |
|-------|---------|
| **Obra** | Nebulosa Violeta |
| **Artista** | ArtistaNova |
| **Hash** | `QmXyZ...abc123` (CID v0) |
| **Preço** | 5,00 tokens (~$8,75 USD) |
| **Criado em** | 26/09/2026 |

### Dados Mockados para Demonstração

```python
OBRAS_MOCKADAS = [
    {
        "id": 0,
        "nome": "Nebulosa Violeta",
        "artista": "ArtistaNova",
        "hashArquivo": "QmXyZ...abc123456789",
        "preco": "500000000000000000",  # 0.5 tokens
        "criadoEm": "2026-09-20"
    },
    {
        "id": 1,
        "nome": "Ritmos da Aurora",
        "artista": "ElétricaMúsica",
        "hashArquivo": "QmDef...xyz987654321",
        "preco": "300000000000000000",  # 0.3 tokens
        "criadoEm": "2026-09-22"
    },
    {
        "id": 2,
        "nome": "Sinfonia Digital",
        "artista": "OrquestraVirtual",
        "hashArquivo": "QmGhi...uvw111222333",
        "preco": "800000000000000000",  # 0.8 tokens
        "criadoEm": "2026-09-24"
    }
]
```

### Screenhots para Apresentação

Fazer capturas:
1. Logo + título com degradê neon
2. Cards dos princípios em grid
3. Status do ciclo técnico verde/neon
4. Lista de obras registradas
5. Rodapé com gradient intenso

---

## 🚀 Deploy e Compartilhamento

### Opções para Publicar Demo:

#### A) Streamlit Cloud (Recomendado!)
```bash
# 1. Pushar repo para GitHub
git add .
git commit -m "feat: mockup demonstração com obras fictícias"
git push origin main

# 2. Conectar ao Streamlit Cloud
# https://streamlit.io/cloud
# Upload do repo + credenciais Python (se necessário)

# 3. Subir demo
# Dashboard já está rodando em dop-foundation.streamlit.app
```

#### B) GitHub Pages com embed
Embutir streamlit app numa página GitHub Pages para maior alcance.

#### C) Vídeo de tela
Gravar demo usando OBS Studio:
- Capturar janela do navegador
- Mostrar 2x velocidade para vídeo compacto
- Inserir voiceover com o roteiro acima

---

## 📊 Métricas que Impactam

Na demo, mostrar (mesmo que mockadas):

- **Artistas registrados**: 3 (fictícias)
- **Obras distribuídas**: 3
- **Valor retido por artistas**: ~$26 USD em royalties diretos
- **Fundo comunitário acumulado**: [X]% de cada venda
- **Auditabilidades públicas**: Todas as transações verificáveis

---

## 🎯 Call-to-Action Final

```
🎤 NARRATIVA:
"A DOP Foundation não é só código. É um movimento para que
artistas mantenham o controle da sua música.

Junte-se a nós! Faça seu fork, contribua, distribua suas obras."
```

**Links**:
- 🌐 https://dop-foundation.streamlit.app/
- 📖 Ver README.md completo
- 🤝 Contribua no GitHub

---

## 🎬 Dicas para Apresentação ao Vivo

### Engajamento:
1. **Perguntar ao público**: "Quantos aqui são artistas independentes?"
2. **Mostrar blockchain ao vivo**: Abrir Ganache e mostrar saldo
3. **Explicar conceitos simples**: Blockchain = caderno de registro público imutável

### Visual Impactante:
- Tiro rápido do logo neon
- Zoom nos cards com hover effects
- Mostrar gradientes e brilhos
- Manter ritmo dinâmico (50 slides max se for slide deck)

### Roteiro Curto (2 min):
```
1. Logo DOP + problema (30s)
2. Solução + princípios (45s)
3. Demo visual interface (60s)
4. Conclusão + CTA (30s)
```

---

<div style="background: linear-gradient(180deg, #FF00FF, #FF6B00); padding:24px; text-align:center;">
  <h3 style="color:#fff; margin:0;">🎭 PRONTO PARA DEMONSTRAÇÃO!</h3>
  <p style="color:#fff; margin-top:16px;">Rodar dashboard + mockups = impacto visual garantido</p>
</div>
