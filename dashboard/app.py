import streamlit as st
import json

# =============================================================================
# DOP FOUNDATION — LOJA PREMIUM FLAC MASTER (VERSÃO STREAMLIT CLOUD FRIENDLY)
# Simples e funcional!
# =============================================================================

st.set_page_config(
    page_title="DOP FOUNDATION — FLAC MASTER STORE",
    page_icon="🎵",
    layout="wide",
)

# =============================================================================
# CATÁLOGO MOCKUP DE FLAC MASTER
# =============================================================================
CATALOGO_MOCKUP = [
    {
        "id": 1,
        "nome": "NEBULOSA VIOLETA",
        "artista": "ARTISTA NOVA",
        "ano": "2026",
        "preco": "0.5 tokens (~R$ 8,75)",
        "genero": "Electronic / Ambient"
    },
    {
        "id": 2,
        "nome": "RITMOS DA AURORA",
        "artista": "ELÉTRICA MÚSICA",
        "ano": "2026",
        "preco": "0.3 tokens (~R$ 5,25)",
        "genero": "Synthwave / Retro"
    },
    {
        "id": 3,
        "nome": "SINFONIA DIGITAL",
        "artista": "ORQUESTRA VIRTUAL",
        "ano": "2026",
        "preco": "0.8 tokens (~R$ 14,00)",
        "genero": "Classical / Electronic"
    },
    {
        "id": 4,
        "nome": "URBAN LEGENDS",
        "artista": "FUNK COLABORATIVO BR",
        "ano": "2026",
        "preco": "0.4 tokens (~R$ 7,00)",
        "genero": "Funk / Eletrônico"
    },
    {
        "id": 5,
        "nome": "INDIE NIGHTS",
        "artista": "GUITARRISTA INDEPENDENTE",
        "ano": "2026",
        "preco": "0.6 tokens (~R$ 10,50)",
        "genero": "Indie Rock / Alternative"
    },
    {
        "id": 6,
        "nome": "HORIZONTES SONOROS",
        "artista": "PODCASTER ELETRÔNICO",
        "ano": "2026",
        "preco": "0.35 tokens (~R$ 6,00)",
        "genero": "Lo-fi / Chillout"
    }
]

# =============================================================================
# HEADER
# =============================================================================
col1, col2, col3 = st.columns([4, 2, 4])

with col2:
    st.markdown("""
    <div style="display:flex; align-items:center; justify-content:center; min-height:80px; background:#0a0a0a; border:3px solid #FF00FF;">
        <span style="font-size:60px; filter:drop-shadow(0 0 15px #FF00FF);">🎵</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# TÍTULO E DESCRIÇÃO
# =============================================================================
st.title("DOP FOUNDATION")
st.subheader("LOJA PREMIUM DE FLAC MASTER — ALTISSIMA QUALIDADE")

st.markdown("""
<div style="background:linear-gradient(180deg,#FF00FF,#FF6B00); padding:24px; text-align:center; margin-top:16px;">
    <p style="margin:0; font-size:16px; color:#fff; line-height:1.6;">
        <strong>CATÁLOGO DE FLAC MASTER</strong><br>
        Qualidade de referência • Downloads descentralizados • FLAC 16-bit/44.1kHz
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# FILTROS
# =============================================================================
st.markdown("### 🔍 Encontrar Sua Música")

col_filter1, col_filter2 = st.columns(2)

with col_filter1:
    genero_filtro = st.selectbox(
        "Filtrar por Gênero",
        ["Todos", "Electronic", "Funk", "Indie Rock", "Lo-fi"]
    )

with col_filter2:
    artista_filtro = st.text_input(
        "Buscar por artista...",
        placeholder="Digite o nome do artista..."
    )

# =============================================================================
# APLICAR FILTROS
# =============================================================================
obras_filtradas = CATALOGO_MOCKUP.copy()

if genero_filtro != "Todos":
    obras_filtradas = [obra for obra in obras_filtradas if genero_filtro.lower() in obra["genero"].lower()]

if artista_filtro:
    termo = artista_filtro.lower()
    obras_filtradas = [obra for obra in obras_filtradas
                       if termo in obra["nome"].lower() or termo in obra["artista"].lower()]

st.info(f"📊 <strong>{len(obras_filtradas)}</strong> obras encontradas")

# =============================================================================
# LISTAGEM DE OBRAS
# =============================================================================
if st.button("🔄 Atualizar Catálogo", type="primary", use_container_width=True):
    st.success("Catálogo atualizado!")

st.markdown("---")

col1, col2, col3 = st.columns(3)

for obra in obras_filtradas:
    with col1 if (obras_filtradas.index(obra) % 3 == 0) else \
        (col2 if (obras_filtradas.index(obra) % 3 == 1) else col3):

        st.markdown(f"""
        <div style="background:#0a0a0a; border:2px solid #FF6B00;
                    padding:16px; margin-bottom:16px; text-align:center;">
            <!-- Usando placeholder de imagem -->
            <div style="width:100%; height:180px; background:linear-gradient(135deg,#1a1a2e,#2a2a4e);
                        display:flex; align-items:center; justify-content:center; margin-bottom:12px; border-radius:8px;">
                <span style="font-size:60px; opacity:0.5;">🎵</span>
            </div>

            <h3 style="color:#fff; font-size:18px; margin:0 0 4px 0; font-weight:700;">{obra['nome']}</h3>
            <p style="color:#FF6B00; font-size:14px; margin:4px 0;"><strong>{obra['artista']}</strong></p>

            <div style="background:#1a1a2e; padding:10px; border-radius:6px; text-align:left;">
                <small style="color:#888;">🎼 {obra.get('genero', 'Electronic')}</small><br>
                <small style="color:#FF6B00;">💰 {obra['preco']}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# RODAPÉ
# =============================================================================
st.markdown("""
<div style="background:linear-gradient(180deg,#FF00FF,#FF6B00); padding:32px; text-align:center; margin-top:48px;">
    <h1 style="color:#fff; text-shadow:none; margin:0 0 16px 0;">DOP FOUNDATION</h1>
    <p style="color:#fff; font-size:18px;">INFRAESTRUTURA SOBERANA DE DISTRIBUIÇÃO MUSICAL</p>
    <p style="color:#fff; font-size:14px; margin-top:16px;">CÓDIGO ABERTO • DADOS PORTÁVEIS • FLAC DE ALTÍSSIMA QUALIDADE</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# INFORMAÇÕES ADICIONAIS
# =============================================================================
st.markdown("""
<div style="background:rgba(10,10,10,0.9); padding:24px; margin-top:32px; border-radius:12px;">
    <h3 style="color:#FF6B00; font-size:16px; margin-top:0;">ℹ️ SOBRE ESTA LOJA MOCKUP</h3>
    <p style="color:#fff; font-size:14px; line-height:1.8;">
        Esta é uma demonstração visual da loja DOP Foundation.<br>
        O catálogo mostra como funcionará o marketplace completo.<br><br>
        <strong>Próximo passo:</strong> Integrar com IPFS Kubo para streaming real de FLAC!
    </p>
</div>
""", unsafe_allow_html=True)
