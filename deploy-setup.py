#!/usr/bin/env python3
"""Upload DopeFlack Dashboard ao Streamlit Cloud — Preparar deployment"""

from pathlib import Path
import shutil

# Configurações
dop_dir = r"C:\Users\marce\dop-foundation"
dashboard_dir = Path(dop_dir) / "dashboard"
streamlit_app = dashboard_dir / "app-streamlit-clean-v2.py"

print("\n[DEPLOY DOPEFLACK STREAMLIT CLOUD - UPLOAD]")
print("=" * 70 + "\n")

# Verificar arquivo app v2 clean  
if streamlit_app.exists():
    print("Arquivo app-streamlit-clean-v2.py encontrado!") 
    
    # Criar deploy bundle
    deploy_bundle = dashboard_dir / "deploy"
    deploy_bundle.mkdir(exist_ok=True)
    
    # Copiar app v2 clean pra deploy folder
    shutil.copy(streamlit_app, deploy_bundle / "app.py")
    
    print(f"\nBundle de deployment criado em: {deploy_bundle}")
    print(f"Arquivo app : {deploy_bundle}/app.py")

print("\n[UPLOAD STREAMLIT CLOUD]")
print("1. Navegar pra /c/Users/marce/dop-foundation/dashboard/deploy")
print("2. rodar: streamlit cloud upload --app-dir=.")
print(f"\nNovo URL sera: https://dopeflack-streamlit.app/")

else:
    print("Arquivo app-streamlit-clean-v2.py nao encontrado!")

print("\n[PRONTO]")