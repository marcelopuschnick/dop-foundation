#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DOPEFLACK STREAMLIT DASHBOARD V2 — Clean, minimalista agressivo (v4-hybrid design)"""

import streamlit as st

st.set_page_config(
    page_title="DOPEFLACK FOUNDATION", 
    page_icon="🎵", 
    layout="wide"
)

# =============================================================================
# GRID LAYOUT V4-HYBRID (left sidebar + main content + cultural fund right sidebar)
# =============================================================================
col1, col2, col3 = st.columns([260, 1, 320])

# Left sidebar/navigation  
with col1:
    st.markdown("""
        <div style="padding-right: calc(var(--space-sm));color:#FFF;">
            <h4 style="font-weight:900;color:orange;margin-bottom:.5rem">⚛️ DOPEFLACK</h4>
            <a href="#" style="display:block;color:#77;padding:8px 8px;margin-bottom:.2rem;background:none;width:100%" aria-current="page">Dashboard</a>
            <a href="#" style="display:block;color:#77;padding:8px 8px;margin-bottom:.2rem">Library</h3>
            <a href="#" style="display:block;color:#77;padding:8px 8px;margin-bottom:.2rem">Grants</h3>         
        </div>

""", unsafe_allow_html=True)

# =============================================================================
# PLAYER SECTION (Main Content) - v4-hybrid waveforms + glow badges
# =============================================================================
with col1:
    st.markdown("""
    <div style="background:#0a0a16;padding:var(--space-lg);border-radius:-8px;">
        <p>MASTER EDITION 09/250</p>
        <h3 class="player-title">Vanta Bloom</h3>
        <span>Sable Systems · Event Horizon / 2026 — LOSSLESS AUDIO</span>
        <br><br>
        <button style="background:linear-gradient(90deg,orange,transparent)" color:white;cursor:pointer" onclick="console.log('▶ PLAY')">▶ PLAY TRACK</button>
        
        <!-- Waveforms simulated via st.metric (v4-hybrid visual) -->  
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# CULTURAL FUND DASHBOARD (Right Sidebar - v4-hybrid design system)
# =============================================================================
with col3:
    st.markdown("""
        <div style="background:#0a0a16;padding:var(--space-lg);border-radius:-8px;text-align:center">
            <h4>CULTURAL CULTURAL FUND</h4>
            <span style="font-size:12px;color:#99;margin-left:auto" class="LIVE-AUDITED">LIVE · AUDITED ✓</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Fund value metric  
    st.metric(label="Total Fund Value", value="$<b>$2,481,790.42 USD</b>")
    
    # Active grants + Paid grid  
    col_sub1, col_sub2 = st.columns([1, 1])
    with col_sub1:
        st.caption("Active grants • 18 active • 67 artists funded")
    with col_sub2:
        st.caption("Paid to date • $<b>$684.2K USD</b>")

# =============================================================================
# RECENT RELEASES (Main content - below player)
# =============================================================================
with col1:
    st.markdown("""
    <div style="margin-top:calc(var(--space-xl))/2;background:#0a0a38;padding:var(--space-lg);border-radius:-6px;">
        <h4>Recent Releases</h4>
        <ul style="list-style:none;color:#77;gap:var(--space-sm)">
            <li>Memory Dial — Arca Meridian</li>
            <li>Soft Collapse — Lumen Vessel</li>
            <li>Nocturne 404 — Kairo Static</li>
        </ul>
    </div>

""", unsafe_allow_html=True)

# =============================================================================
# FOOTER (Streamlit version - não v4-hybrid)
# =============================================================================
with col1:
    st.markdown("""
    <div style="background:linear-gradient(90deg,orange,transparent);padding:var(--space-lg);margin-top:auto;text-align:center;color:white";">
        <h4>▶ PLAY NOW — LIVE SIGNAL</h4>
        <span class="btn-glow" onclick="console.log('Broadcast to peers')">BROADCAST TO PEERS</span>
    </div>

""", unsafe_allow_html=True)

st.markdown("---")