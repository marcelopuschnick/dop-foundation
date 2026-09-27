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
# IMAGENS DOS ÁLBUNS — COVERS DO UNSPLASH
# =============================================================================
COVERS = {
    1: "https://images.unsplash.com/photo-1614726395744-dc36ecd20a1b?w=400&h=400&fit=crop",
    2: "https://images.unsplash.com/photo-1493225255756-d9584486029e?w=400&h=400&fit=crop",
    3: "https://images.unsplash.com/photo-1514320297829-725c6ab7f8e5?w=400&h=400&fit=crop",
    4: "https://images.unsplash.com/photo-1470225620780-dc8f911b6a73?w=400&h=400&fit=crop",
    5: "https://images.unsplash.com/photo-1493225255756-d9584486029e?w=400&h=400&fit=crop",
    6: "https://images.unsplash.com/photo-1459749411177-287ce324648d?w=400&h=400&fit=crop"
}

# =============================================================================
# HEADER
# =============================================================================
col1, col2, col3 = st.columns([4, 2, 4])

with col2:
    st.markdown("""
    <div style="display:flex; align-items:center; justify-content:center; min-height:80px; background:linear-gradient(135deg,#0a0a0a,#1a1a2e); border:3px solid #FF00FF; box-shadow:0 0 30px rgba(255,0,255,0.3);">
        <span style="font-size:70px; filter:drop-shadow(0 0 20px #FF00FF) drop-shadow(0 0 30px #FF6B00);">🎵</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# HERO SECTION — CARTÃO PRINCIPAL COM DEGRADÊ ANIMADO
# =============================================================================
st.markdown("""
<div style="background:linear-gradient(135deg,rgba(26,26,46,0.95),rgba(10,10,10,0.98));
                padding:48px; border-radius:16px; border:2px solid #FF6B00;
                box-shadow:0 10px 40px rgba(255,107,0,0.2); margin-bottom:32px;">
    <h1 style="color:#fff; font-size:42px; text-align:center; margin:0 0 16px 0;
               background:linear-gradient(180deg,#FF00FF,#FF6B00);
               -webkit-background-clip:text; -webkit-text-fill-color:transparent;
               font-weight:900;">DOP FOUNDATION</h1>
    <p style="color:#FF6B00; font-size:20px; text-align:center; margin:0 0 24px 0;">
        LOJA PREMIUM DE FLAC MASTER — ALTISSIMA QUALIDADE
    </p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;
                background:linear-gradient(180deg,#FF00FF,#FF6B00); padding:20px; border-radius:12px;">
        <span style="background:rgba(255,255,255,0.2); padding:12px 24px; border-radius:8px; color:#fff; font-size:14px; font-weight:700;">
            🎼 QUALIDADE FLAC 16-bit/44.1kHz
        </span>
        <span style="background:rgba(255,255,255,0.2); padding:12px 24px; border-radius:8px; color:#fff; font-size:14px; font-weight:700;">
            📦 DOWNLOADS DECENTRALIZADOS
        </span>
        <span style="background:rgba(255,255,255,0.2); padding:12px 24px; border-radius:8px; color:#fff; font-size:14px; font-weight:700;">
            🔒 DADOS PORTÁVEIS
        </span>
    </div>
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
                    padding:16px; margin-bottom:16px; text-align:center;
                    transition:all 0.3s ease; cursor:pointer;"
             onmouseover="this.style.borderColor='#FF00FF'; this.style.boxShadow='0 0 25px rgba(255,0,255,0.3)'"
             onmouseout="this.style.borderColor='#FF6B00'; this.style.boxShadow='0 0 15px rgba(255,107,0,0.2)'">
            <!-- Imagem cover do álbum -->
            <img src="{COVERS.get(obra['id'], 'https://images.unsplash.com/photo-1614726395744-dc36ecd20a1b?w=400&h=400&fit=crop')}" style="width:100%; height:240px; object-fit:cover; border-radius:8px; margin-bottom:12px; box-shadow:0 4px 16px rgba(0,0,0,0.3);">

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
