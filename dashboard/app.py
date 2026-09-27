import streamlit as st
import json
from pathlib import Path
import base64

# =============================================================================
# DOP FOUNDATION — LOJA PREMIUM DE FLAC MASTER + PLAYER INTEGRADO
# Design: Apple Music x Spotify — Preto puro + Montserrat white + neon
# =============================================================================

st.set_page_config(
    page_title="DOP FOUNDATION — FLAC MASTER STORE",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# CATÁLOGO MOCKUP DE FLAC MASTER (GRANDES NOMES) — FAKE DATA PARA SHOWCASE
# =============================================================================
CATALOGO_MOCKUP = [
    {
        "id": 1,
        "nome": "NEBULOSA VIOLETA",
        "artista": "ARTISTA NOVA",
        "ano": "2026",
        "preco": "0.5 tokens (~R$ 8,75)",
        "genero": "Electronic / Ambient",
        "faixa_destaque": "Stardust Dreams (4:32)",
        "cover_url": "https://images.unsplash.com/photo-1614726395744-dc36ecd20a1b?w=400&h=400&fit=crop",
        "cid_ipfs": "QmXyZ...abc123456789"
    },
    {
        "id": 2,
        "nome": "RITMOS DA AURORA",
        "artista": "ELÉTRICA MÚSICA",
        "ano": "2026",
        "preco": "0.3 tokens (~R$ 5,25)",
        "genero": "Synthwave / Retro",
        "faixa_destaque": "Golden Hour (5:18)",
        "cover_url": "https://images.unsplash.com/photo-1493225255756-d9584486029e?w=400&h=400&fit=crop",
        "cid_ipfs": "QmDef...xyz987654321"
    },
    {
        "id": 3,
        "nome": "SINFONIA DIGITAL",
        "artista": "ORQUESTRA VIRTUAL",
        "ano": "2026",
        "preco": "0.8 tokens (~R$ 14,00)",
        "genero": "Classical / Electronic",
        "faixa_destaque": "Cantata AI (7:45)",
        "cover_url": "https://images.unsplash.com/photo-1514320297829-725c6ab7f8e5?w=400&h=400&fit=crop",
        "cid_ipfs": "QmGhi...uvw111222333"
    },
    {
        "id": 4,
        "nome": "URBAN LEGENDS",
        "artista": "FUNK COLABORATIVO BR",
        "ano": "2026",
        "preco": "0.4 tokens (~R$ 7,00)",
        "genero": "Funk / Eletrônico",
        "faixa_destaque": "Batida da Favela (3:56)",
        "cover_url": "https://images.unsplash.com/photo-1470225620780-dc8f911b6a73?w=400&h=400&fit=crop",
        "cid_ipfs": "QmJkl...rst456789012"
    },
    {
        "id": 5,
        "nome": "INDIE NIGHTS",
        "artista": "GUITARRISTA INDEPENDENTE",
        "ano": "2026",
        "preco": "0.6 tokens (~R$ 10,50)",
        "genero": "Indie Rock / Alternative",
        "faixa_destaque": "Midnight Drive (4:12)",
        "cover_url": "https://images.unsplash.com/photo-1493225255756-d9584486029e?w=400&h=400&fit=crop",
        "cid_ipfs": "QmMno...pqr345678901"
    },
    {
        "id": 6,
        "nome": "HORIZONTES SONOROS",
        "artista": "PODCASTER ELETRÔNICO",
        "ano": "2026",
        "preco": "0.35 tokens (~R$ 6,00)",
        "genero": "Lo-fi / Chillout",
        "faixa_destaque": "Study Beats Vol.1 (8:30)",
        "cover_url": "https://images.unsplash.com/photo-1459749411177-287ce324648d?w=400&h=400&fit=crop",
        "cid_ipfs": "QmPqr...stu234567890"
    }
]

# =============================================================================
# PLAYER DE ÁUDIO INTEGRADO — ESTILO APP STORE MUSIC
# =============================================================================
def render_player(audio_url, track_name, artist):
    """Renderiza player estilo Apple Music com controles de áudio."""

    if not audio_url:
        return None

    # Ícones SVG inline para controle de áudio
    play_pause_svg = """
        <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
            <path d="M8 5v14l11-7z"/>
        </svg>
    """

    prev_svg = """
        <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
            <path d="M6 6h2v12H6zm3.5 6l8-5-8-5v10z"/>
        </svg>
    """

    next_svg = """
        <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
            <path d="M6 18l8.5-6L6 12v6zm10.5-13l-8.5 6 8.5 6V5z"/>
        </svg>
    """

    volume_svg = """
        <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
        </svg>
    """

    # Renderizar player com controles
    st.markdown(f"""
    <div style="background:rgba(10,10,10,0.95); border:1px solid #FF6B00;
                padding:24px; margin:32px 0; border-radius:12px; box-shadow:0 10px 40px rgba(255,107,0,0.2);">
        <div style="display:flex; align-items:center; justify-content:space-between;">
            <div style="flex:1;">
                <div style="background:linear-gradient(180deg,#FF00FF,#FF6B00);
                             padding:12px 24px; border-radius:8px; font-size:13px; margin-bottom:16px; display:inline-block;">
                    🎵 <strong>{track_name}</strong> — {artist}
                </div>
                <p style="color:#FF6B00; font-size:14px; margin:0 0 8px 0;"><strong>Gênero:</strong> {genero if 'genero' in locals() else 'Electronic'}</p>
            </div>
            <div style="text-align:right;">
                <button onclick="togglePlay()" style="background:none; border:none; cursor:pointer; margin:4px;">
                    {play_pause_svg}
                </button>
                <button onclick="prevTrack()" style="background:none; border:none; cursor:pointer; margin:4px;">
                    {prev_svg}
                </button>
                <button onclick="nextTrack()" style="background:none; border:none; cursor:pointer; margin:4px;">
                    {next_svg}
                </button>
            </div>
        </div>

        <!-- Audio Element com volume control -->
        <audio id="audio-player" src="{audio_url}" controls style="width:100%; margin-top:16px; height:56px;">
            Seu navegador não suporta o elemento de áudio.
        </audio>

        <div style="margin-top:12px; text-align:right;">
            <label style="color:#FF6B00; font-size:13px;">🔊 Volume:</label>
            <input type="range" min="0" max="1" step="0.1" value="0.8" id="volume-slider"
                   oninput="setVolume(this.value)" style="width:120px; accent-color:#FF6B00;">
        </div>

        <!-- Progress bar -->
        <div style="background:#333; height:4px; border-radius:4px; margin-top:12px; overflow:hidden;">
            <div id="progress-bar" style="background:linear-gradient(90deg,#FF00FF,#FF6B00);
                                        width:0%; height:100%; transition:width 0.1s linear;"></div>
        </div>

        <!-- Playlist de reprodução automática -->
        <script>
            const player = document.getElementById('audio-player');
            const progress = document.getElementById('progress-bar');
            const tracks = {track_name}; // será preenchido dinamicamente
            let currentIndex = 0;

            player.addEventListener('play', () => {
                togglePlayIcon();
                updateProgressBar();
            });

            player.addEventListener('ended', () => {
                if ({enable_auto_next}) nextTrack();
            });

            function nextTrack() {
                currentIndex = (currentIndex + 1) % Object.keys(tracks).length;
                playTrack(Object.keys(tracks)[currentIndex]);
            }

            function prevTrack() {
                currentIndex = (currentIndex - 1 + Object.keys(tracks).length) % Object.keys(tracks).length;
                playTrack(Object.keys(tracks)[currentIndex]);
            }

            function playTrack(trackId) {
                const keys = Object.keys(tracks);
                player.src = tracks[keys[currentIndex]];
                player.play();
            }

            function updateProgressBar() {
                const currentTime = player.currentTime;
                const duration = player.duration || 100; // evitar NaN
                progress.style.width = (currentTime / duration * 100) + '%';
            }

            player.addEventListener('timeupdate', updateProgressBar);

            function setVolume(val) {
                player.volume = val;
            }

            function togglePlayIcon() {
                // lógica de play/pause icon se necessário
            }
        </script>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# HEADER — LOGO E NARRATIVA LOJA PREMIUM
# =============================================================================
col1, col2, col3 = st.columns([4, 2, 4])

with col1:
    pass

with col2:
    st.markdown("""
    <div class="logo-container" style="display:flex; align-items:center; justify-content:center; min-height:100px;">
        <span style="font-size:64px; filter:drop-shadow(0 0 15px #FF00FF);">🎵</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    pass

st.markdown("---")

# =============================================================================
# TÍTULO PRINCIPAL — LOJA DE FLAC MASTER PREMIUM
# =============================================================================
st.title("DOP FOUNDATION")
st.subheader("LOJA PREMIUM DE FLAC MASTER — ALTISSIMA QUALIDADE")

# Box de descrição com narrativa impactante
st.markdown("""
<div class="info-box" style="border:2px solid #FF00FF; padding:24px; text-align:center;">
    <p style="margin:0; font-size:16px; line-height:2;">
        <strong>CATÁLOGO DE FLAC MASTER DE GRANDES ARTISTAS</strong><br>
        Qualidade de referência • Downloads descentralizados • Reproduce em qualquer player
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# FILTROS E BUSCA — UI MODERNA
# =============================================================================
st.markdown("### 🔍 Encontrar Sua Música")

col_filter1, col_filter2 = st.columns(2)

with col_filter1:
    genero_filtro = st.selectbox(
        "Gênero",
        ["Todos", "Electronic", "Funk", "Indie Rock", "Lo-fi"]
    )

with col_filter2:
    artista_filtro = st.text_input(
        "Buscar por artista ou título...",
        placeholder="Digite para filtrar..."
    )

# Aplicar filtros
obras_filtradas = CATALOGO_MOCKUP.copy()

if genero_filtro != "Todos":
    obras_filtradas = [obra for obra in obras_filtradas if genero_filtro.lower() in obra.get("genero", "").lower()]

if artista_filtro:
    termo = artista_filtro.lower()
    obras_filtradas = [obra for obra in obras_filtradas
                       if termo in obra["nome"].lower() or termo in obra["artista"].lower()]

# Mostrar contador de resultados
st.info(f"📊 <strong>{len(obras_filtradas)} obras encontradas</strong> no catálogo FLAC Master")

# =============================================================================
# LISTAGEM DE OBRAS — CARDS PREMIUM ESTILO APPLE MUSIC
# =============================================================================
if st.button("🔄 Atualizar Catálogo", type="primary", use_container_width=True):
    st.success("Catálogo atualizado!")


st.markdown("---")

col1, col2, col3 = st.columns(3)

for obra in obras_filtradas:
    with col1 if (obras_filtradas.index(obra) % 3 == 0) else (
        col2 if (obras_filtradas.index(obra) % 3 == 1) else col3
    ):

        # Renderizar card com imagem cover do Unsplash
        st.markdown(f"""
        <div style="background:rgba(10,10,10,0.98); border:2px solid #FF6B00;
                    padding:16px; margin-bottom:16px; text-align:center;
                    transition:all 0.3s ease; cursor:pointer;"
             onmouseover="this.style.borderColor='#FF00FF'; this.style.boxShadow='0 0 25px rgba(255,0,255,0.3)'"
             onmouseout="this.style.borderColor='#FF6B00'; this.style.boxShadow='0 0 15px rgba(255,107,0,0.2)'">
            <!-- Imagem cover do álbum -->
            <img src="{obra['cover_url']}" style="width:100%; height:240px; object-fit:cover;
                                                  border-radius:8px; margin-bottom:12px;">

            <div style="height:56px;"></div> <!-- Espaçamento para imagem -->

            <h3 style="color:#fff; font-size:18px; margin:0 0 4px 0; font-weight:700;">{obra['nome']}</h3>
            <p style="color:#FF6B00; font-size:14px; margin:4px 0;"><strong>{obra['artista']}</strong></p>

            <div style="background:#1a1a2e; padding:10px; border-radius:6px; text-align:left;">
                <small style="color:#888;">🎼 {obra.get('genero', 'Electronic')}</small><br>
                <small style="color:#FF6B00;">💰 {obra['preco']}</small>
            </div>

            <div style="margin-top:12px; height:40px;"></div> <!-- Espaço para player -->
        </div>
        """, unsafe_allow_html=True)


# =============================================================================
# PLAYER INTEGRADO — MOSTRAR SE ALGUÉM TOCAR UMA FAIXA
# =============================================================================
# Criar URL de áudio simulado (streaming via IPFS ou link externo)
def get_audio_stream_url(cid):
    """Converte CID do IPFS para URL de streaming."""
    if cid.startswith("Qm"):
        return f"https://dweb.link/ipfs/{cid}/file.flac"  # Simulado
    return None

# Verificar se há faixa tocando atualmente (mock)
faixa_atual = None

# Exibir player fixo no rodapé quando houver seleção
if len(obras_filtradas) > 0:
    st.markdown("---")

    col_player, _, col_info = st.columns([3, 1, 4])

    with col_player:
        # Gerar URL de áudio para primeira obra selecionada (simulado)
        primeiro_obra = obras_filtradas[0] if obras_filtradas else None

        if primeiro_obra:
            cid = primeiro_obra.get("cid_ipfs", "QmXyZ...abc123456789")

            # Renderizar player da faixa atual
            track_info = f"{primeiro_obra['nome']} - {primeiro_obra['artista']}"

            st.markdown(f"""
            <div style="background:linear-gradient(180deg,#2a2a4a,#1a1a2e);
                        padding:24px; margin-bottom:32px; border-radius:12px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                    <span style="background:linear-gradient(180deg,#FF00FF,#FF6B00);
                                padding:12px 24px; border-radius:8px; color:#fff; font-size:13px; font-weight:bold;">
                        🎵 FAIXA TOCANDO
                    </span>
                    <span style="color:#FF6B00; font-size:12px;">{primeiro_obra['preco']}</span>
                </div>

                <audio id="main-player" src="https://dummy.audio/mp3/lofi.mp3" controls
                       style="width:100%; margin-top:12px; height:56px;">
                    Reprodução não disponível neste dispositivo.
                </audio>

                <div style="display:flex; justify-content:space-between; margin-top:16px;">
                    <div>
                        <p style="color:#FF6B00; font-size:12px; margin:0;"><strong>{primeiro_obra['genero']}</strong></p>
                        <small style="color:#666;">FLAC 16-bit/44.1kHz</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div style="background:rgba(10,10,10,0.8); padding:24px; margin-bottom:32px; border-radius:12px;">
            <h3 style="color:#FF6B00; font-size:16px; margin-top:0;">ℹ️ SOBRE O PLAYER</h3>
            <p style="color:#fff; font-size:14px; line-height:1.8;">
                Este player reproduz FLAC master de altíssima qualidade.<br>
                Os arquivos são armazenados em IPFS Kubo (descentralizado).<br><br>
                <strong>Vantagens:</strong><br>
                • Sem limitações de streaming<br>
                • Download direto no seu dispositivo<br>
                • Compatível com qualquer player FLAC<br>
                • Fallback para streaming se offline
            </p>
        </div>
        """, unsafe_allow_html=True)


# =============================================================================
# RODAPÉ — GRADIENTE INTENSO COM LINKS
# =============================================================================
st.markdown("""
<div class="footer-box">
    <h1 style="color:#000; text-shadow:none; margin:0 0 16px 0;">DOP FOUNDATION</h1>
    <p style="margin:0; font-size:18px;">INFRAESTRUTURA SOBERANA DE DISTRIBUIÇÃO MUSICAL</p>
    <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-top:16px;">
        <a href="#catalogo" style="background:#fff; color:#000; padding:10px 20px;
                                  border-radius:6px; text-decoration:none; font-weight:bold;">
            📜 Catálogo Completo
        </a>
        <a href="#about" style="background:rgba(255,255,255,0.2); color:#fff; padding:10px 20px;
                                border-radius:6px; text-decoration:none;">
            📖 Sobre
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SCRIPT DE INICIALIZAÇÃO DO PLAYER (JavaScript inline)
# =============================================================================
st.markdown("""
<script>
    // Inicializar player com faixa padrão
    document.addEventListener('DOMContentLoaded', () => {
        const tracks = """ + json.dumps({obra['nome']: f"https://dummy.audio/mp3/lofi.mp3" for obra in obras_filtradas}) + """;

        // Selecionar primeira faixa automaticamente
        Object.keys(tracks).forEach((trackName, index) => {
            setTimeout(() => {
                const player = document.getElementById('main-player');
                if (player && tracks[trackName]) {
                    player.src = tracks[trackName];
                    player.play();
                }
            }, 100 * index);
        });
    });
</script>
""", unsafe_allow_html=True)
