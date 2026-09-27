#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DOPEFLACK STREAMLIT DASHBOARD V2 — Cultural Fund + UI Minimalista Agressivo
Integrado com v4-hybrid design system (borders, waveforms, glow badges)"""

import streamlit as st

# =============================================================================
# CONGURAR STREAMLIT COM UI DOPOEFLACK (V4-HYBRID DESIGN)
# =============================================================================

st.set_page_config(
    page_title="DOPEFLACK FOUNDATION",
    page_icon="🎵",
    layout="wide"
)

# Colunas para grid v4-hybrid
col1, col2, col3 = st.columns([280, 1, 340])

# =============================================================================
# SIDEBAR LEFT (Navigation)
# =============================================================================
with col1:
    st.markdown("""
        <div style="padding-right: calc(var(--space-sm));">
            <h4 style="font-weight:900;color:var(--primary);margin-bottom:.5rem">⚛️ DOPEFLACK</h4>
            <a href="#" style="display:block;color:#77;padding:4px 8px;margin-bottom:.2rem;background:none;border-radius:4px;width:100%" class="active" aria-current="page">Dashboard</a>
            <a href="#" style="display:block;color:#77;padding:4px 8px;margin-bottom:.2rem">Library</h3>
            <a href="#" style="display:block;color:#77;padding:4px 8px;margin-bottom:.2rem">Grants</h3>             
        </div>

""", unsafe_allow_html=True)

# =============================================================================
# PLAYER SECTION (Main Content) - v4-hybrid waveforms
# =============================================================================
with col1:
    st.subheader("🎵 DopeFlack Player — Vanta Bloom", divider="blue")
    
    # Master edition badge
    st.info("MASTER EDITION 09/250")
    
    # Album art + Title
    st.markdown("""
        <div style="display:flex;gap:var(--space-sm);align-items:center;padding-bottom:var(--space-lg)">
            <div style="width:128px;height:128px;background:#1a1a2e;border-radius:-8px">Vanta Bloom</div>
            <div style="flex:1">
                <h3 style="font-size:32px;font-weight:400;color:white;">Vanta Bloom</h3>
                <p style="color:#666;max-width:30ch">Sable Systems · Event Horizon / 2026 (24-bit/96kHz)</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Play button + live waveform simulation
    play_btn = st.button("▶ PLAY TRACK", use_container_width=True, type="primary")
    
    # Waveform simulated via st.metric (v4-hybrid visual)  
    st.metric(label="Signal Quality • OFFLINE VAULT", value="32.4 GB lossless audio • 68%", delta=None)

# =============================================================================
# CULTURAL FUND DASHBOARD (Right Sidebar - v4-hybrid design)
# =============================================================================
with col3:
    # Live badge + Title
    st.markdown("""
        <div class="fund-header">
            <h3 style="color:white;font-weight:400">Cultural Cultural Fund</h3>
            <span style="font-size:10px;color:#99;border-radius:4px;background:rgba(0,255,157,.1);padding:4px 8px;margin-left:auto">LIVE · AUDITED ✓</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Fund value live updates (simulated via streamlit.metric)  
    st.metric(
        label="Total Fund Value", 
        value="$2,481,790.42 USD" 
    )

    # Active grants + Paid to date grid
    col_active, col_paid = st.columns([1, 1])
    
    with col_active:
        st.caption("Active grants • 18 active • 67 artists funded")
    
    with col_paid:  
        st.caption("Paid to date • $684.2K USD")
