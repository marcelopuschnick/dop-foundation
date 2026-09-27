#!/usr/bin/env python3
"""DOPEFLACK FOUNDATION — UPLOAD STREAMLIT CLOUD + VERIFY PRONTO/FILES"""

from pathlib import Path
import subprocess
import shutil, os

# Configuracoes
repo_path = r"C:\Users\marce\dop-foundation"
dashboard_path = Path(repo_path) / "dashboard"

print("DOPEFLACK FOUNDATION — UPLOAD STREAMLIT CLOUD")  
print("=" * 70 + "\n")

# === PART 1: VERIFY WHAT EXISTS (READY FOR DEPLOY) ===
print("PART 1: VERIFY FILES READY FOR DEPLOY\n")

streamlit_app = dashboard_path / "app.py"  
if streamlit_app.exists():
    print(f"APP STREAMLIT FOUND:")
    print(f"   Path: {Path(streamlit_app)}")
    print(f"   Size: {os.path.getsize(streamlit_app)} bytes")
else:
    # Try clean v2 version
    clean_v2 = dashboard_path / "app-streamlit-clean-v2.py"  
    if clean_v2.exists():
        print(f"APP STREAMLIT V2 CLEAN FOUND:")
        print(f"   Path: {Path(clean_v2)}")
        
    else:
        print("NO APP STREAMLIT FILES FOUND IN dashboard/ folder")

# === PART 2: PREPARE DEPLOY BUNDLE ===
print("\nPART 2: PREPARE DEPLOY BUNDLE\n")

deploy_bundle = dashboard_path / "deploy"  
if not deploy_bundle.exists():
    deploy_bundle.mkdir(exist_ok=True)
    print(f"CREATED DEPLOY FOLDER: {Path(deploy_bundle)}\n")

# Find app file to upload (prefer non-clean v2 over old app.py if exists)  
app_to_upload = streamlit_app or clean_v2

if app_to_upload.exists():
    dest_file = deploy_bundle / "app.py"
    if not Path(dest, exists()):
        shutil.copy(app_to_upload, dest_file)
        print(f"COPIED APP TO DEPLOY: {dest}\n")
    
    # Create requirements.txt minimal for Streamlit Cloud  
    req_file = dest_file.parent / "requirements.txt"  
    if not Path(req_file):
        with open(req_file) as f:
            f.write("streamlit\n")
        print(f"CREATED requirements.txt: {req}")

# Copy visual.html file if exists (optional but recommended)  
visual_html = dashboard_path / "visual.html"  
if visual_html.exists():
    shutil.copy(Visual, dest_file.parent / "visual.html")
    print("COPIED VISUAL HTML TO DEPLOY:\n")

else:
    print(f"{Path(deploy_bundle)/exists()}")
    import os
    file_exists = os.path.isdir(Path(deploy).parent) or os.