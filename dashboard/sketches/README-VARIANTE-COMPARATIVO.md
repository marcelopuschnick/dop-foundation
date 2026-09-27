# DOPEFLACK UI MOCKUPS - COMPARATIVO DAS 3 VARIANTES
<!-- Generated with Skill `sketch` from Hermes Agent (persistent, re-usable) -->
<!-- Author: DopeFlack Core Team | Version: 1.0.0-beta -->

## 📋 Contexto

Estas variantes de UI exploram **3 direções de design** para o dashboard DopeFlack, baseadas na referência visual da imagem (Linear/Vercel vibe) mas com cores e identidade do projeto (orange #FF4D00, purple #CC00FF). 

### Objetivo
Gerar mockups lado a lado para comparar antes de commitar produção. Cada variante é **disponível como HTML estático** — clique duas vezes em cada arquivo pra abrir e ver no navegador local.

---

## 📌 Diferenciais Principais

| Variante | Estilo | Densidade | Cultural First | Waveforms Animados | Complexidade Visual |
|----------|--------|-----------|-----------------|--------------------|---------------------|
| **v1-linear-dark** | Minimalista | Low | Medium | Sim (subtil) | Baixo (clean, editorial) |
| **v2-brutalist** | Brutalista Cultural | High | High | Sim (brutos) | Médio (borders explícitos) |
| **v3-synthwave** | Synthwave Cyberpunk | Medium-High | High+ | Sim (retro-futuristas) | Alto (glows, gradientes neons) |

---

## 🎨 Análise de Cada Variante

### v1-linear-dark.html
#### Design stance
Minimalismo agressivo estilo Linear/Vercel — tipografia Helvetica/Inter forte, dark mode profundo com gradientes sutis.

#### Key choices
```css
Layout: Sidebar + Grid + Cultural Fund section (não overlapping)
Typography: Inter (-apple-system, sans-serif), font-weight 400 para headings
Color palette:  
  --bg-dark: #0a0a18 → Dark profundo (#050510 base)
  --primary: #FF4D00 (orange DopeFlack)
  --secondary: #CC00FF (purple neon)
Hover effects: Background rgba(255,77,0,.1), transform translateY(-4px) sutil
Waveforms: SVG animated com height animado (scaleY 0.2→1) + opacity .3→.9
```

#### Weak at
- Menos feedback visual pra cultural-first users (badges sociais menos visíveis)
- Grid explícito menos pronunciado que em v2/v3

#### Best for
Power users, power user experience, clean interface com foco no playback musical + fund tracking

---

### v2-brutalist.html
#### Design stance
Cultural-first explícito — grid explicita com borders visíveis (rgba(255,77,0,.2)) que enfatizam a função de cada seção. Typography Courier New para dados financeiros (monospace auditável).

#### Key choices
```css
Layout: Single-column (não sidebar) pra foco cultural
Typography: Courier New / monospace pra dados do fund
Borders: 1px solid rgba(255,77,0,.2) → bordas transparentes mas visíveis
Cursor: pointer nas cards pra indicar interatividade
Hover effects: Transform translateY(-4px), background rgba(255,77,0,.3)
Badges sociais: Gold/Silver/Bronze com gradientes brilhantes
```

#### Weak at
- Pode ser visualmente pesado pra mobile (borders + grid explícito)
- Cultural Fund dados podem parecer muito densos pra power users

#### Best for  
Cultural-first vibes, community-facing dashboard, badges sociais como elementos de design explícitos

---

### v3-synthwave.html
#### Design stance  
Estilo synthwave cyberpunk baseado na referência imagem original — dark cinematográfico com waveforms retro-futuristas + gradientes neons (purple/orange). Typography sem serifa mas com glow effects. Cultural Fund como elemento central destacado.

#### Key choices
```css
Layout: Sidebar + Main + Cultural Fund section (grid 3 colunas)
Typography: Inter, font-weight 400/700 pra headings
Effects: Radial-gradient ellipse pra profundity cinematográfica
Waveforms: SVG conic-gradient animated de forma retro-futurista  
Cultural Fund badge: "LIVE · VERIFIED" com glow verde (#00FF9D)
```

#### Weak at
- Waveforms podem ser complexos visualmente em mobile viewport pequeno
- Gradientes neons podem reduzir contraste em alguns contextos de uso noturno

#### Best for
Visual storytelling, cultural-first + power user hybrid, badges sociais como elementos narrativos (gloss brilhantes)

---

## 🚀 Próximos Passos

### Opção A: Commitar uma variante v1/v2/v3 selecionada
```bash
cd "/c/Users/marce/dop-foundation"
git add dashboard/sketches/{VARIANT chosen}.html README-*.md
git commit -m "Add V{num} UI variant as production baseline" 
git push origin main          # ou branch alvo

# Opcional: criar branch feature pra refinamento posterior  
git checkout -b feat/v{n}-refinement
```

### Opção B: Combinar elementos (hybrid approach)
Criar variante X = híbrido v2 (brutalist cultural) + v3 (synthwave vibes):
- Layout grid de v2, mas com waveforms e gradientes de v3
- Cultural Fund live updates de v1 + hover effects de v3

### Opção C: Iteração baseada em feedback visual
Abrir variantes no navegador, ver qual bate melhor com referência imagem. Ajustar:
- Cores (mantém orange #FF4D00 como primary, mas ajustam secondary)  
- Waveforms (substitute SVG static por HTML5 canvas ou p5js se quiser mais performance)
- Cultural Fund live updates (WebSocket vs polling simulação JavaScript)

---

## 📌 Como Abrir Cada Variante

```bash
# PowerShell (Windows): abre cada arquivo em nova aba navegador local
start "v1-linear-dark.html"         # Minimalista agresivo
start "v2-brutalist.html"           # Cultural explícito  
start "v3-synthwave.html"           # Synthwave cyberpunk

# Ou via Python:
python -m http.server 8000 --ignore-absolute-imports   # roda servidor simples
# Abra em browser: http://localhost:8000/dashboard/sketches/
```

---

## 📋 Checklist de Decisão (antes de commitar)

| Critério | v1-linear-dark | v2-brutalist | v3-synthwave |
|----------|-----------------|--------------|---------------|
| **Bate com referência imagem?** | Sim (mais clean) | Parcial (menos decoration) | Sim (vibe original mais próxima) |
| **Minimalista agressivo?** | ✅ Sim | ⚠️ Partial (borders explícitos) | ❌ Não (complexidade visual alta) |
| **Cultural-first explícita?** | Parcial | ✅ Sim | ✅ Sim + extras |
| **Waveforms animados funcionais?** | ✅ Sim | ✅ Sim | ✅ Sim |
| **Performance em mobile viewport?** | ✅ Bom | ⚠️ Médio (borders grid) | ⚠️ Baixo (gradientes neons) |
| **Complexidade CSS mantenha simples?** | ✅ Sim (<50 lines style) | ⚠️ Médio (~80 lines) | ❌ Alto (~120+ lines) |

---

## 🎯 Recomendação do Team:
V3-synthwave bate melhor com referência imagem original, mas v1-linear-dark é mais minimalista agressivo. 

**Sugestão:** Comece com `v1-linear-dark` (clean, tipografia forte) pra version 1, depois refina com waveforms e live updates. Quando quiser mais cultural-first vibe, migre pra v2 ou híbrido entre v1+v3.

---

## 💝 Contribuintes:
- Hermes Agent skills: `sketch` (persistent, re-writable)  
- DopeFlack Core Team | 2026
