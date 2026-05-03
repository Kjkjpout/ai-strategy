import streamlit as st
import urllib.request

# --- 1. 視覺設計 ---
st.set_page_config(page_title="ViralAI", page_icon="🔥")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .viral-title { font-size: 42px; font-weight: 800; color: white; margin-bottom: 5px; }
    .stTextInput input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    .stButton > button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 55px !important; width: 100% !important;
        font-weight: bold; font-size: 18px !important;
    }
    .card { background-color: #1c2533; padding: 20px; border-radius: 15px; border-left: 6px solid #ff4b2b; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 登入邏輯 (加強模糊比對) ---
if 'login' not in st.session_state:
    st.session_state.login = False

# 白名單：我們把常見的格式都寫進去
ALLOWED_USERS = ["972896266", "0972896266"] 

if not st.session_state.login:
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    st.write("全平台爆款內容拆解引擎")
    u_phone = st.text_input("🔑 手機號碼驗證", placeholder="輸入手機號碼...")
    
    if st.button("立即進入系統"):
        # 清除輸入內容的所有空格
        clean_input = u_phone.strip().replace(" ", "")
        
        # 只要輸入的號碼包含白名單號碼，或是白名單號碼包含輸入的號碼就放行
        is_allowed = False
        for user_phone in ALLOWED_USERS:
            if clean_input in user_phone or user_phone in clean_input:
                is_allowed = True
                break
        
        if is_allowed:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("❌ 號碼未授權，請聯繫管理員")

else:
    # --- 3. 分析功能 ---
    st.markdown('<div class="viral-title">🔥 ViralAI</div>', unsafe_allow_html=True)
    url = st.text_input("在此貼上影片連結", placeholder="https://...")

    if st.button("啟動 AI 深度拆解"):
        if url:
            with st.spinner("🧠 正在提取數據..."):
                try:
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        html = resp.read().decode('utf-8', errors='ignore')
                        v_title = html.split('<title>')[1].split('</title>')[0]
                        v_title = v_title.split('-')[0].split('|')[0].strip()
                    st.success(f"✅ 已識別：{v_title}")
                    
                    kw = v_title[:8]
                    st.markdown(f'<div class="card"><b>🔥 爆款建議：</b><br>這部關於【{kw}】的影片流量密碼在於開頭前3秒。建議搭配豆包AI生成「反直覺」標題。</div>', unsafe_allow_html=True)
                    st.balloons()
                except:
                    st.error("❌ 讀取失敗，請確認連結。")
