import streamlit as st

# Configuracao da pagina
st.set_page_config(
    page_title="Fundação DOP",
    page_icon="🎵",
    layout="wide",
)

# Cabecalho
st.title("🎵 Fundação DOP")
st.subheader("Infraestrutura soberana de distribuição musical")
st.markdown("---")

# Status dos modulos
st.markdown("### 📊 Status do sistema")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Módulo 0", value="Concluído", delta="DNA")
with col2:
    st.metric(label="Módulo 1", value="Em execução", delta="Infraestrutura")
with col3:
    st.metric(label="Módulos restantes", value="7", delta="Planejados")

st.markdown("---")

# Principios
st.markdown("### 🎯 Princípios inegociáveis")
st.markdown("""
1. Artista é dono do master e define o preço
2. Nenhum intermediário com poder de veto
3. Split automático e auditável em tempo real
4. Fundo comunitário obrigatório em cada venda
5. Governança com colégios e veto real
6. IA conselheira, nunca soberana
7. Código aberto, dados portáveis
8. FLAC de altíssima qualidade
9. Fallback apenas comunitário
10. Retorno social mensurável e publicado
""")

st.markdown("---")

# Status do ciclo tecnico
st.markdown("### 🔗 Ciclo técnico validado")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.success("✅ API local rodando")
with col_b:
    st.success("✅ Blockchain local (Ganache)")
with col_c:
    st.success("✅ Carteira lendo saldo")

st.markdown("---")

# Rodape
st.info("Dashboard em construção. Próximo passo: registrar a primeira obra na blockchain.")