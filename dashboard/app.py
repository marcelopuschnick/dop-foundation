import streamlit as st

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA — DESIGN SYSTEM DOP DARK CYBERPUNK
# =============================================================================
st.set_page_config(
    page_title="DOP FOUNDATION",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'report_my_bug': '#️⃣',
        'get_support': '📧 DOP FOUNDATION'
    },
)

# =============================================================================
# APARÊNCIA VISUAL — CSS CUSTOMIZADO
# =============================================================================
st.markdown("""
<style>
    /* RESET E FUNDO PRETO */
    html, body {
        background-color: #000000 !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif;
    }

    /* TÍTULOS — BLACK + CAIXA ALTA + DEGRADÊ NEON */
    h1, h2, h3, h4, h5, h6 {
        color: #fff !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        font-family: 'Montserrat', sans-serif !important;
        background: linear-gradient(180deg, #FF00FF, #FF6B00) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-shadow: 0 0 20px rgba(255, 0, 255, 0.5), 0 0 30px rgba(255, 107, 0, 0.5) !important;
    }

    /* SUBTÍTULOS — MENOS INTENSOS MAS AINDA NEON */
    .stSubheader {
        color: #ffffff !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* CAIXAS DE CARD — PRETO COM BORDA NEON */
    div[data-testid="stMetric"] {
        background-color: #0a0a0a !important;
        border: 2px solid #FF6B00 !important;
        box-shadow: 0 0 15px rgba(255, 107, 0, 0.3) !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
    }

    /* BOTÕES — GRADIENTE NEON */
    .stButton > button {
        background: linear-gradient(135deg, #FF00FF, #FF6B00) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        font-family: 'Montserrat', sans-serif !important;
        border: none !important;
    }

    /* LINKS — NEON ROSE */
    a {
        color: #FF6B00 !important;
        text-decoration: underline !important;
    }

    a:hover {
        color: #FF00FF !important;
    }

    /* LISTAS E TEXTOS */
    p, span, div {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
    }

    /* MARCADOR DE SEPARAÇÃO — BORDA NEON */
    hr.stDivider {
        border-color: #FF6B00 !important;
        box-shadow: 0 0 10px rgba(255, 107, 0, 0.5) !important;
    }

    /* BADGES E TAGS — NEON */
    span[data-testid="stMetricValueDelta"]::before {
        content: "" !important;
    }

    /* HEADER CARD DO LOGO */
    .logo-container {
        background-color: #0a0a0a !important;
        border: 3px solid #FF00FF !important;
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.4) !important;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    /* ESTILO PARA PRINCÍPIOS */
    .principio-card {
        background-color: #0a0a0a !important;
        border: 1px solid #FF6B00 !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        padding: 24px !important;
        margin-bottom: 16px !important;
        transition: all 0.3s ease !important;
    }

    .principio-card:hover {
        border-color: #FF00FF !important;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.4) !important;
    }

    /* SEÇÃO DE STATUS */
    .status-box {
        background-color: #0a0a0a !important;
        border-left: 4px solid #FF6B00 !important;
        padding: 20px !important;
        margin-bottom: 16px !important;
    }

    /* OBRAS REGISTRADAS */
    .obra-card {
        background-color: #0a0a0a !important;
        border: 2px solid #FF6B00 !important;
        box-shadow: 0 0 15px rgba(255, 107, 0, 0.3) !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        padding: 24px !important;
        margin-bottom: 16px !important;
    }

    .obra-card:hover {
        border-color: #FF00FF !important;
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.4) !important;
        transform: translateY(-4px) !important;
    }

    /* RODAPÉ */
    .footer-box {
        background: linear-gradient(180deg, #FF00FF, #FF6B00) !important;
        color: #000000 !important;
        padding: 40px !important;
        text-align: center !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
    }

    /* STATUS INDICATORS */
    .status-check {
        background-color: #FF6B00 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        padding: 16px 32px !important;
        text-align: center !important;
        border-radius: 8px !important;
        box-shadow: 0 0 20px rgba(255, 107, 0, 0.4) !important;
    }

    .status-check:hover {
        background-color: #FF00FF !important;
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.5) !important;
    }

    /* INFO BOX */
    .info-box {
        border: 2px solid #FF6B00 !important;
        padding: 24px !important;
        text-align: center !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
    }

</style>
""", unsafe_allow_html=True)

# =============================================================================
# HEADER — LOGO E IDENTIDADE VISUAL
# =============================================================================
col1, col2, col3 = st.columns([4, 2, 4])

with col1:
    pass  # Espaço vazio

with col2:
    st.markdown("""
    <div class="logo-container" style="display:flex; align-items:center; justify-content:center; min-height:120px;">
        <span style="font-size:80px; filter:drop-shadow(0 0 20px #FF00FF);">🎵</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    pass  # Espaço vazio

st.markdown("---")

# =============================================================================
# TÍTULO PRINCIPAL — GRANDE E NEON
# =============================================================================
st.title("DOP FOUNDATION")

# Subtítulo com estilo
st.subheader("INFRAESTRUTURA SOBERANA DE DISTRIBUIÇÃO MUSICAL")

# Descrição narrativa em box informativo
st.markdown("""
<div class="info-box" style="border:2px solid #FF00FF; padding:24px; text-align:center;">
    <p style="margin:0; font-size:16px; line-height:2;">
        DEVOLVER AO ARTISTA E À SOCIEDADE O CONTROLE, A TRANSPARÊNCIA<br>
        E O RETORNO ECONÔMICO DA MÚSICA.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# STATUS DOS MÓDULOS — CARDS NEON
# =============================================================================
st.markdown("STATUS DO SISTEMA")

col1, col2, col3 = st.columns(3)

with col1:
    card_0 = """
    <div class="status-check">
        ✅ DNA<br>
        <span style="font-size:14px; margin-top:8px;">MÓDULO 0</span><br>
        <span style="font-size:12px; margin-top:4px;">IDENTIDADE & GOVERNANÇA</span>
    </div>
    """
    st.markdown(card_0, unsafe_allow_html=True)

with col2:
    card_1 = """
    <div class="status-check" style="background:#FF00FF; box-shadow:0 0 25px rgba(255,0,255,0.5);">
        🔧 EM EXECUÇÃO<br>
        <span style="font-size:14px; margin-top:8px;">MÓDULO 1</span><br>
        <span style="font-size:12px; margin-top:4px;">INFRAESTRUTURA LOCAL</span>
    </div>
    """
    st.markdown(card_1, unsafe_allow_html=True)

with col3:
    card_future = """
    <div class="status-check">
        🔮 PRÓXIMOS PASSOS<br>
        <span style="font-size:14px; margin-top:8px;">MÓDULOS 2-8</span><br>
        <span style="font-size:12px; margin-top:4px;">PLANEJADOS</span>
    </div>
    """
    st.markdown(card_future, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# PRINCÍPIOS INEGOCIÁVEIS — LISTA NEON
# =============================================================================
st.markdown("PRINCÍPIOS INEGOCIÁVEIS")

principios = [
    "🎼 ARTISTA É DONO DO MASTER E DEFINE O PREÇO",
    "🚫 NENHUM INTERMEDIÁRIO COM PODER DE VETO",
    "⚡ SPLIT AUTOMÁTICO E AUDITÁVEL EM TEMPO REAL",
    "🤝 FUNDO COMUNITÁRIO OBRIGATÓRIO EM CADA VENDA",
    "👥 GOVERNANÇA COM COLÉGIOS E VETO REAL",
    "🤖 IA CONSELHEIRA, NUNCA SOBERANA",
    "📜 CÓDIGO ABERTO, DADOS PORTÁVEIS",
    "💿 FLAC DE ALTÍSSIMA QUALIDADE",
    "🔄 FALLBACK APENAS COMUNITÁRIO",
    "📈 RETORNO SOCIAL MENSURÁVEL E PUBLICADO",
]

for principio in principios:
    st.markdown(f"""
    <div class="principio-card" style="margin:8px 0; padding:24px; border:1px solid #FF6B00;">
        {principio}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# CICLO TÉCNICO VALIDADO — STATUS NEON
# =============================================================================
st.markdown("CICLO TÉCNICO VALIDADO")

col_a, col_b, col_c = st.columns(3)

with col_a:
    status_api = """
    <div class="status-check" style="background:#00c853; color:#000;">
        ✅ API LOCAL<br>
        <span style="font-size:12px;">RODANDO</span>
    </div>
    """
    st.markdown(status_api, unsafe_allow_html=True)

with col_b:
    status_bc = """
    <div class="status-check" style="background:#FF00FF; color:#000;">
        ⛓️ BLOCKCHAIN<br>
        <span style="font-size:12px;">GANACHE ATIVO</span>
    </div>
    """
    st.markdown(status_bc, unsafe_allow_html=True)

with col_c:
    status_wallet = """
    <div class="status-check" style="background:#FF6B00; color:#000;">
        💰 CARREIRA<br>
        <span style="font-size:12px;">LENDENDO SALDO</span>
    </div>
    """
    st.markdown(status_wallet, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# RODAPÉ — GRADIENTE INTENSO
# =============================================================================
st.markdown("""
<div class="footer-box">
    <h1 style="color:#000; text-shadow:none; margin:0 0 16px 0;">DOP FOUNDATION</h1>
    <p style="margin:0; font-size:18px;">INFRAESTRUTURA SOBERANA DE DISTRIBUIÇÃO MUSICAL</p>
    <p style="margin:16px 0 0 0; font-size:14px;">CÓDIGO ABERTO • DADOS PORTÁVEIS • FLAC DE ALTÍSSIMA QUALIDADE</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# CONEXÃO BLOCKCHAIN E LISTAGEM DE OBRAS (OPCIONAL — SE DESEJADO)
# =============================================================================
if st.checkbox("MOstrar obras registradas na blockchain", value=False):
    st.markdown("---")
    st.markdown("OBRAS REGISTRADAS NA BLOCKCHAIN")

    try:
        from web3 import Web3

        RPC_URL = "http://127.0.0.1:8545"
        w3 = Web3(Web3.HTTPProvider(RPC_URL))

        if w3.is_connected():
            st.success(f"✅ CONECTADO — CHAIN ID: {w3.eth.chain_id}")

            RAIZ = Path(__file__).parent.parent / "contracts"
            ENDERECO_FILE = RAIZ / "endereco.json"

            if ENDERECO_FILE.exists():
                endereco_json = json.loads(ENDERECO_FILE.read_text())
                ENDERECO = endereco_json["endereco"]

                ABI_FILE = RAIZ / "MusicRegistry.json"
                abi = json.loads(ABI_FILE.read_text()["abi"])

                contract = w3.eth.contract(address=ENDERECO, abi=abi)
                total = contract.functions.contar().call()

                if total > 0:
                    st.success(f"✅ TOTAL DE OBRAS REGISTRADAS: {total}")

                    col1, col2, col3 = st.columns(3)

                    for i in range(total):
                        with col1 if i % 3 == 0 else (col2 if i % 3 == 1 else col3):
                            obra = contract.functions.obterObra(i).call()

                            st.markdown(f"""
                            <div class="obra-card">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                                    <span style="font-size:24px;">🎵 Oبرا #{obra[0]}</span>
                                    <span style="background:#FF00FF; color:#000;
                                                        padding:8px 16px; border-radius:4px; font-size:12px;">
                                        {obra[3]}
                                    </span>
                                </div>
                                <div style="margin-bottom:8px;"><strong>Nome:</strong> <span style="color:#FF6B00;">{obra[1]}</span></div>
                                <div style="margin-bottom:8px;"><strong>Artista:</strong> <span style="color:#FF6B00;">{obra[2]}</span></div>
                                <div style="margin-bottom:16px;"><strong>Criado em:</strong>
                                    <span style="font-size:13px; color:#888;">{w3.to_datetime(obra[6]).strftime('%Y-%m-%d %H:%M')} UTC</span>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.info("👉 NENHUMA OTRA REGISTRADA AINDA.")

            else:
                st.warning("⚠️ ARQUIVO DE ENDEREÇO NÃO ENCONTRADO")

        else:
            st.error("❌ NÃO É POSSÍVEL CONECTAR À REDE GANACHE")

    except Exception as e:
        st.error(f"⚠️ ERRO AO CONECTAR NA BLOCKCHAIN: {str(e)[:100]}")
