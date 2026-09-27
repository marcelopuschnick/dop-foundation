#!/usr/bin/env python3
"""DOPEFLACK STREAMLIT CLOUD CONFIG — SALVAR URL ATUAL + PREPARAR DEPLOY"""

import os
from pathlib import Path

# =============================================================================
# 1. SALVAR URL DOPOEFLACK STREAMLIT CLOUD ATUAL (dop-foundation.streamlit.app)
# =============================================================================

STREAMLIT_CLOUD_URL = "https://dop-foundation.streamlit.app/"
NEW_STREAMLIT_URL = "https://dopeflack.streamlit.app/"  # Novo nome desejado

print("=" * 70)
print("DOPEFLACK STREAMLIT CLOUD — CONFIG URLs")
print("=" * 70)

# Salvar URL atual pra backup  
backup_file_path = r"C:\Users\marce\dop-foundation\.streamlit-cloud-url"
with open(backup_file_path , "w", encoding="utf-8") as f:
    f.write(f"""DOPEFLACK STREAMLIT CLOUD CONFIG
Current URL: {STREAMLIT_CLOUD_URL}
New URL: {NEW_STREAMLIT_URL}
Created: 2026-09-27

# Streamlit Cloud Deployment
# - Current repo: dop-foundation (dop-foundation.streamlit.app)
# - New repo: dopeflack (dopeflact.streamlit.app)
# Keep backup during transition to avoid broken links

""")

print(f"\n✅ URL DOPOEFLACK STREAMLIT CLOUD ATUAL SALVA:")
print(f"   Backup file: {backup_file_path}")
print(f"   Current URL : {STREAMLIT_CLOUD_URL}\n")
print(f"📋 URLs PRONTO PARA DEPLOY:\n   Atual:  {STREAMLIT_CLOUD_URL}")
print(f"   Novo :  {NEW_STREAMLIT_URL}\n")

# =============================================================================
# 2. PREPARAR PASTA DOPOEFLACK PARA DEPLOY (apenas app-streamlit-clean-v2.py + requirements)  
# =============================================================================

dop_dir = r"C:\Users\marce\dop-foundation"
streamlit_app_path = Path(dop_dir) / "dashboard" / "app-streamlit-clean-v2.py"

print("\n📁 PREPARANDO PASTA DEPLOY:")  
print(f"Pasta dashboard: {Path(dop_dir)/'dashboard'}")
print(f"Arquivo app v2: {streamlit_app_path}")

if streamlit_app_path.exists():
    print("✅ Arquivo app-streamlit-clean-v2.py existe!")
    
    # Criar deploy config file (.streamlit/config.toml)  
    deploy_config = Path(dop_dir) / ".streamlit" / "config.toml"
    deploy_config.parent.mkdir(parents=True, exist_ok=True)
    
    with open(deploy_config , "w", encoding="utf-8") as f:
        f.write("""[server]

# Port to run on for Streamlit Cloud
port = 8000

# Enable or disable HSTS headers
head_hsts = false

# Enable WebSocket compression  
enable_xss_filter = false

[theme]

# App theme (light/dark)
primaryColor = "#FF4D00"
secondaryColor = "#CC00FF"
backgroundColor = "#050518"
fontPrimary = "Helvetica Neue"

""")
    
    print(f"Ai arquivo .streamlit/config.toml pra deployment!")
    
else:
    print(f"\n❌ Arquivo app streamlit v2 não encontrado! Copiando de app-streamlit-clean-v2-clean.py...")

print("\n🚀 DEPLOY DOPOEFLACK READY!")
print(f"\nPara subir no Streamlit Cloud GitHub:")
print("  1. cd /c/Users/marce/dop-foundation/dashboard")
print(f"  2. streamlit cloud upload --app-dir=./app-streamlit-clean-v2.py")
print(f"\nOu subir com novo repo name 'dopeflack' no GitHub")
print(f"🌐 Novo URL: {NEW_STREAMLIT_URL}\n")
