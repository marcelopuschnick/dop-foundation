# Governança da Fundação DOP

A governança é o que impede a fundação de virar uma nova major.
É descentralizada, com colégios temáticos e poder de veto real.
Nenhuma maioria simples atropela um colégio afetado.

---

## 1. Colégios

A comunidade é dividida em quatro colégios. Cada um tem voz
e veto sobre decisões que afetem diretamente sua área.

### Colégio dos Artistas
- **Composição:** artistas verificados com obra registrada na fundação.
- **Poder de veto sobre:** royalty mínimo, direitos autorais,
  precificação, uso de samples, licenciamento.
- **Justificativa:** quem cria a obra tem soberania sobre ela.

### Colégio dos Ouvintes
- **Composição:** compradores ativos com histórico de aquisição.
- **Poder de veto sobre:** taxa de plataforma, teto de preço,
  percentual do fundo comunitário, políticas de reembolso.
- **Justificativa:** quem sustenta a economia tem voz nas regras.

### Colégio Técnico
- **Composição:** engenheiros, devs, mantenedores de nó, curadoria técnica.
- **Poder de veto sobre:** infraestrutura, soberania, segurança,
  padrões de qualidade de FLAC, arquitetura de contratos.
- **Justificativa:** quem mantém o sistema vivo sabe o que o quebra.

### Colégio Jurídico
- **Composição:** advogados, contadores, especialistas tributários.
- **Poder de veto sobre:** risco legal, tributário, regulatório,
  conformidade com LGPD e legislação autoral.
- **Justificativa:** ninguém quer a fundação exposta a sanções.

---

## 2. Mecanismo de decisão

Todo processo de decisão segue cinco etapas obrigatórias:

### Etapa 1 — Proposta
Qualquer membro com reputação mínima pode submeter uma proposta.
A proposta é pública, versionada e imutável após submissão.

### Etapa 2 — Análise da IA conselheira
A IA local analisa a proposta e emite parecer **não vinculante**
com:
- Impacto econômico estimado
- Riscos técnicos identificados
- Precedentes históricos relevantes
- Simulações de cenário

### Etapa 3 — Deliberação por colégio
Cada colégio delibera separadamente. O voto é registrado on-chain
via Snapshot local. O peso do voto é definido por reputação
(não por capital).

### Etapa 4 — Verificação de veto
Se qualquer colégio afetado vetar, a proposta é bloqueada ou
devolvida para reformulação. O veto é registrado e justificado
publicamente.

### Etapa 5 — Execução via multisig
Propostas aprovadas são executadas por multisig comunitário
(Safe local). Nenhuma execução é automática sem ratificação
humana.

---

## 3. Quórum e aprovação

| Tipo de proposta | Aprovação mínima | Veto de colégio |
|---|---|---|
| Ordinária (operacional) | 50% + 1 dos votantes | Não se aplica |
| Afeta direitos | 2/3 dos votantes | Obrigatório do colégio afetado |
| Constitucional (muda princípios) | 3/4 dos votantes | Obrigatório de todos os colégios |
| Emergencial (segurança) | Conselho técnico + multisig | Ratificação em 72h |

---

## 4. Reputação

O peso do voto não é proporcional a capital. É proporcional a
reputação, que se constrói por:
- Contribuição técnica verificada
- Obras publicadas e auditadas
- Participação consistente em deliberações
- Curadoria reconhecida pela comunidade

Reputação é **não transferível**. Não se compra, não se vende,
não se herda.

---

## 5. Transparência

- Todas as propostas são públicas
- Todos os votos são registrados on-chain
- Todos os vetos são justificados publicamente
- Todas as execuções são auditáveis
- Relatório mensal automatizado de governança

---

## 6. O que a governança NÃO pode fazer

- Alterar os 10 princípios inegociáveis sem quórum constitucional
- Extinguir colégios ou retirar poder de veto
- Permitir intermediário com poder soberano
- Delegar decisão executiva à IA
- Ocultar votos, vetos ou execuções