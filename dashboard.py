import os
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Agentic Sentry — Enterprise Modernization",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Modern Enterprise Glassmorphic Design System
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Global resets */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background-color: #090d16;
        background-image: 
            radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.12) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.08) 0px, transparent 50%);
        color: #f1f5f9;
    }

    /* Header styling */
    .hero-container {
        padding: 1.5rem 0 1.2rem 0;
        margin-bottom: 1.5rem;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #60a5fa;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        padding: 4px 10px;
        border-radius: 9999px;
        margin-bottom: 0.75rem;
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.025em;
        background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-top: 0.4rem;
    }

    /* Metric Cards */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin-bottom: 1.75rem;
    }
    .kpi-card {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        position: relative;
        overflow: hidden;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .kpi-card:hover {
        border-color: rgba(59, 130, 246, 0.4);
        transform: translateY(-2px);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
    }
    .kpi-red::before { background: linear-gradient(90deg, #ef4444, #f87171); }
    .kpi-emerald::before { background: linear-gradient(90deg, #10b981, #34d399); }
    .kpi-blue::before { background: linear-gradient(90deg, #3b82f6, #60a5fa); }

    .kpi-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #f8fafc;
        margin: 0.3rem 0;
        letter-spacing: -0.02em;
    }
    .kpi-pill {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 6px;
    }
    .pill-green { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .pill-blue { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }

    /* Code Container Headers */
    .pane-header-legacy {
        background: rgba(239, 68, 68, 0.08);
        border: 1px solid rgba(239, 68, 68, 0.25);
        border-bottom: none;
        border-radius: 8px 8px 0 0;
        padding: 8px 14px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #fca5a5;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .pane-header-modern {
        background: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-bottom: none;
        border-radius: 8px 8px 0 0;
        padding: 8px 14px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #86efac;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: rgba(15, 23, 42, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 4px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 7px;
        padding: 6px 14px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748b;
        background: transparent;
        border: none;
        transition: all 0.2s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    /* Code blocks typography tweak */
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.82rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Header Section
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-badge">⚡ Autonomous Engineering Squad • IBM Bob</div>
        <h1 class="hero-title">Agentic Sentry</h1>
        <div class="hero-subtitle">Automated Vulnerability Remediation, Microservice Refactoring & Deterministic Test Generation</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 4. Refined Glassmorphic KPI Row
st.markdown(
    """
    <div class="kpi-grid">
        <div class="kpi-card kpi-red">
            <div class="kpi-label">Vulnerabilities Remediated</div>
            <div class="kpi-value">2 Crit / 3 Med</div>
            <span class="kpi-pill pill-green">✓ 100% Resolved</span>
        </div>
        <div class="kpi-card kpi-emerald">
            <div class="kpi-label">Generated Test Coverage</div>
            <div class="kpi-value">94.2%</div>
            <span class="kpi-pill pill-green">↑ +94% Baseline Coverage</span>
        </div>
        <div class="kpi-card kpi-blue">
            <div class="kpi-label">Refactor Cycle Time</div>
            <div class="kpi-value">45 Sec</div>
            <span class="kpi-pill pill-blue">⚡ -99% Dev Overhead</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# 5. Safe File Loader
def read_file_safe(filename):
  if os.path.exists(filename):
    with open(filename, "r") as f:
      return f.read()
  return f"# Artifact {filename} will be populated once IBM Bob completes execution."


# 6. Tabbed Workspace
tab1, tab2, tab3 = st.tabs([
    "🔀 Code Diff & Modernization",
    "🧪 Auto-Generated Pytest Suite",
    "📄 OpenAPI 3.0 Contract",
])

with tab1:
  left_col, right_col = st.columns(2)
  with left_col:
    st.markdown(
        """
        <div class="pane-header-legacy">
            <span>❌ LEGACY MONOLITH (Flask 1.x)</span>
            <span>CWE-89 • CWE-798 Detected</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.code(read_file_safe("legacy_app.py"), language="python")

  with right_col:
    st.markdown(
        """
        <div class="pane-header-modern">
            <span>✅ REFACTORED MICROSERVICE (FastAPI)</span>
            <span>Hardened & Schema-Validated</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.code(read_file_safe("modern_app.py"), language="python")

with tab2:
  st.code(read_file_safe("test_modern_app.py"), language="python")

with tab3:
  st.code(read_file_safe("openapi.yaml"), language="yaml")