#!/usr/bin/env python3
"""
DOPEFLACK FOUNDATION — GIT CLEANUP + COMMIT RELATÓRIO
Arquivos essenciais commitar, lixo remover não regredir projeto!
"""

from pathlib import Path
import subprocess
import shutil

repo_path = r"C:\Users\marce\dop-foundation"
dashboard_path = Path(repo_path) / "dashboard"

print("=" * 80)
print("DOPEFLACK FOUNDATION — GIT CLEANUP + COMMIT RELATÓRIO")
print("=" * 80 + "\n")

# === PART 1: LISTAR ARQUIVOS TRACKED (COMMITAR) ===
print("=== FILES TRACKED PRONTO COMMITAR ===")  
tracked_files = [
    "dashboard/app.py",                          # APP STREAMLIT PRINCIPAL
    "dashboard/visual.html",                      # DASHBOARD VISUAL MINIMALISTA
]

for f in tracked_files:
    filepath = Path(f)
    if filepath.exists():
        print(f"✅ {f} — TRACKED")
    else:
        print(f"❌ {f} — MISSING (commitar se criar)")

# === PART 2: ARQUIVOS LIXO (REMETER/PRONTO DELETAR) ===
print("\n=== FILES UNTRACKED (LIXO — REMOVER) ===")  

junk_files_pattern = [
    r"^dashboard/[^.]*\.html$",      # remove .html untrackeds simples  
    r"^dashboard/app-streamlit-v2.*\.py$",     # app streams testados
    r"^dashboard/sketches/.*",        # folder sketches inteira
    r"docs/README-SYNTHWAVE-.*\.md",     # readme variantes teste
    r".*streamlit-cloud-config.*\.py$",   # config teste
    r".*deploy-setup\.py$",              # setup teste
]

untracked_count = 0  
for item in Path(repo_path).rglob("*") if repo_path.exists() else []:
    relpath = Path(item).relative_to(repo_path)
    name = str(relpath.name)
    
    is_junk = any(name == f or name.startswith(f + "/") for f in junk_files_pattern[1:]) # exclude visual.html, app.py
    
    if item.is_file() and not item.name.startswith(".") and "git" not in item.name:
        if "visual.html" not in str(relpath) and "app.py" not in str(relpath):  
            print(f"⚠️  {relpath} — UNTRACKED (LIXO)")
            untracked_count += 1

print(f"\nTotal files untrackeds limpo: {untracked_count}")

# === PART 3: COMMIT STATUS ===  
print("\n=== GIT STATUS DETALHADO ===")  

try:
    git_status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_path, capture_output=True, text=True, timeout=5
    )
    
    print(git_status.stdout) if git_status.returncode == 0 else "Erro git status"

except Exception as e:
    print(f"Erro rodar git status: {e}")

# === PART 4: COMMITAR APENAS ESSENCIAIS + DELETAR LIXO ===  
print("\n=== COMMITAR APENAS ESSENCIAIS — PRONTO ===")  

if "dashboard/app.py" in tracked_files and Path(relpath := Path(repo_path)/tracked_file).exists():
    subprocess.run(
        ["git", "add", str(Path(repo_path) / f)],
        cwd=repo_path, capture_output=True
    )

print(f"\n✅ Ready commit: {['app.py', 'visual.html']}")

# === PART 5: FINAL STATUS ===  
print("\n=== FINAL STATUS DO PROJETO ===")  
try:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_path, capture_output=True, text=True
    )
    
    if result.returncode == 0:
        lines = result.stdout.strip().split("\n")
        
        # Contar modified + untracked  
        modified = sum(1 for line in lines if line.startswith("M"))
        unstaged = sum(1 for line in lines if "?" not in line and line.lstrip().startswith((" M",)))
        
        print(f"Modified files: {modified}")
        print(f"Unstaged changes: {unstaged}")

    print("\n✅ Relatório de cleanup pronto!")  
    print("Commit apenas o essencial, remover lixo via 'git reset' + delete local")
    
except Exception as e:
    print(f"Erro final status: {e}")

print(f"\n✅ RELATÓRIO COMPLETO DO PROJETO DOPEFLACK FOUNDATION!")  