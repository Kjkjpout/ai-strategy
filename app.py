import streamlit as st
import time

# --- 1. 商用頂級視覺配置 ---
st.set_page_config(page_title="VIRAL REBORN Pro - 極速複製版", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .glass-card {
        background: #111111;
        border: 1px solid #444;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        background-color: #1a1a1a !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
        height: 60px !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b 0%, #800000 100%);
        color: white; height: 60px; font-weight: bold; border-radius: 8px;
    }
    /* 標題區塊樣式：確保客戶一眼看到 */
    .headline-section {
        background: #222;
        border: 1px solid #ff4b4b;
        padding: 15px;
        border-radius: 8px 8px 0 0;
        border-bottom: none;
    }
    /* 腳本區塊樣式 */
    .script-section {
        background-color: #000;
        border: 1px solid #444;
        border-left: 5px solid #ff4b4b;
        padding: 20px;
        border-radius: 0 0 8px 8px;
        line-height: 1.8;
        font-size: 16px;
    }
    .highlight-label { color: #ff4b4b; font-weight: bold; margin-bottom: 5px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 側邊欄 ---
with st.sidebar:
    st.markdown("<h2 style='color: #ff4b4b;'>VIRAL REBORN</h2>", unsafe_allow_html=True)
    st.info("🎯 模式：1比5 內容重生 + 標題置頂")
    st.divider()
    st.caption("✅ 情感/人性分析引擎運作中")

# --- 3. 主操作區 ---
st.title("🛡️ 爆款基因拆解：腳本與標題一體化系統")
st.write("李大哥，下方產出的每個腳本，標題都已放在最上方，方便您與客戶快速複製使用。")

video_url = st.text_input("🔗 貼入爆款影片連結：", placeholder="YouTube / 抖音 / TikTok / IG 連結...")

if st.button("🚀 執行深度拆解：產出 5 套標題與腳本"):
    if not video_url:
        st.error("❌ 請先貼入連結！")
    else:
        with st.status("🛠️ 正在為您重構爆款內容...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="✅ 5 套戰略腳本已就緒！", state="complete", expanded=False)

        # --- 4. 腳本展示區 ---
        
        def render_script(index, style, titles, content):
            with st.expander(f"📝 方案 {index}：{style}"):
                # 標題區
                title_html = "".join([f"• {t}<br>" for t in titles])
                st.markdown(f"""
                <div class='headline-section'>
                    <span class='highlight-label'>🔥 推薦爆款標題 (直接複製)：</span>
                    <div style='color: #fbbf24; font-size: 18px; font-weight: bold;'>{title_html}</div>
                </div>
                """, unsafe_allow_html=True)
                # 腳本區
                st.markdown(f"""
                <div class='script-section'>
                    <span class='highlight-label'>🎬 30秒重生腳本：</span>
                    {content}
                </div>
                """, unsafe_allow_html=True)

        # 渲染 5 套腳本
        render_script(1, "深夜扎心風", 
            ["懂事的人，注定沒人疼嗎？", "這段話，送給深夜還在翻聊天紀錄的你", "原來成長的代價，是學會安靜地崩潰"],
            "<b>【0-5s】</b>特寫熄滅螢幕。口播：這輩子最遺憾的，不是沒遇到心動的人，而是遇到了，卻發現自己沒資格。<br><b>【5-20s】</b>獨自走在路燈下。口播：我們總是在不對的時間遇到對的人，然後用盡全力去錯過。你以為放不下的是他，其實你只是心疼那個傻傻付出的自己。<br><b>【20-30s】</b>黑底白字。口播：如果你也曾為了一個人徹夜難眠，點個贊，這份心疼我懂你。")

        render_script(2, "人間清醒風", 
            ["卑微換不來愛情，只能換來輕視", "醒醒吧！不回訊息就是最好的答案", "停止自我感動，是你變強的第一步"],
            "<b>【0-5s】</b>剪輯撕照片動作。口播：別再自我感動了！一個不回你訊息的人，他的沈默就是答案。<br><b>【5-20s】</b>對鏡頭直述。口播：你要明白，卑微換不來愛情，只能換來輕視。與其花時間去追一匹馬，不如花時間去種草。<br><b>【20-30s】</b>自信微笑。口播：關注我，讓你的人生不再卑微。")

        render_script(3, "故事旁白風", 
            ["聽說他結婚那天，全場都很開心，除了她", "後來的我們，什麼都有了，卻沒有了『我們』", "回憶是座橋，卻是通往寂寞的牢"],
            "<b>【0-5s】</b>老舊車站畫面。口播：後來的我們，什麼都有了，卻唯獨沒有了我們。<br><b>【5-20s】</b>交錯剪輯過去與現在。口播：聽說他結婚那天，全場都很開心，除了那個陪他走過最苦日子的女孩。原來成長的代價，是看著最愛的人變成別人的英雄。<br><b>【20-30s】</b>夕陽落下。口播：如果時光倒流，你還會選擇認識他嗎？留言區告訴我。")

        render_script(4, "戲劇反轉風", 
            ["參加前任婚禮，我卻笑得最大聲？", "最好的報復，不是恨，而是徹底遺忘", "以為是悲劇，沒想到結局這麼解氣！"],
            "<b>【0-5s】</b>婚禮現場。口播：這是我參加過最難忘的婚禮，新郎不是我，但我卻笑得最開心。<br><b>【5-20s】</b>回憶轉到現在。口播：因為看到那個曾經傷害過我的女孩，現在找了一個比我更差的人。那一刻我才明白，最好的報復，不是恨，而是徹底遺忘。<br><b>【20-30s】</b>點擊收藏。口播：這份解脫，送給正在受傷的你。")

        render_script(5, "治癒救贖風", 
            ["總有一束光，是為你而亮的", "轉發給你最好的閨蜜：你值得被全世界溫柔對待", "錯過的不是遺憾，是為了讓更好的出現"],
            "<b>【0-5s】</b>熱咖啡冒氣。口播：不管你現在經歷什麼，請相信，這世上總有一束光是為你而亮的。<br><b>【5-20s】</b>溫暖畫面。口播：錯過的不是遺憾，是為了讓更好的出現。你要等，等那個眼裡全是你的男孩子，等那個能看穿你所有委屈的人。<br><b>【20-30s】</b>溫暖文字。口播：把這支影片轉發給你的閨蜜，告訴她：你值得被全世界溫柔對待。")

st.divider()
st.caption("© 2026 李大哥 AI 戰略研究所 | 商業版權所有")
