import streamlit as st

st.title('나의 첫 streamlit 프로젝트!')
st.write('Hello streamlit!')

import streamlit as st
import random

# ------------------------------
# MBTI to Career Mapping
# ------------------------------
mbti_jobs = {
    "ISTJ": ["🕵️‍♂️ 감사관", "📊 회계사", "🏛️ 법무관"],
    "ISFJ": ["🏥 간호사", "👨‍🏫 교사", "🛡️ 사회복지사"],
    "INFJ": ["🧠 심리학자", "✍️ 작가", "🎨 예술가"],
    "INTJ": ["🔬 과학자", "💼 전략가", "🖥️ 데이터 사이언티스트"],
    "ISTP": ["🛠️ 기술자", "🏍️ 정비사", "🚓 범죄 수사관"],
    "ISFP": ["🎨 디자이너", "📷 사진작가", "🌿 플로리스트"],
    "INFP": ["📝 시인", "🎭 예술가", "🌍 사회운동가"],
    "INTP": ["🧪 연구원", "💡 발명가", "👨‍💻 개발자"],
    "ESTP": ["📣 세일즈맨", "🚓 경찰관", "🕺 이벤트 기획자"],
    "ESFP": ["🎤 연예인", "🛍️ 쇼핑몰 CEO", "🎉 파티플래너"],
    "ENFP": ["🌟 콘텐츠 크리에이터", "✈️ 여행가", "🎬 영화감독"],
    "ENTP": ["📢 마케터", "💼 창업가", "🎤 방송인"],
    "ESTJ": ["📋 관리자", "🏢 기업임원", "🧾 세무사"],
    "ESFJ": ["🍽️ 서비스 매니저", "👩‍🏫 교육자", "👩‍⚕️ 병원 코디네이터"],
    "ENFJ": ["📚 교육 전문가", "🕊️ 인권운동가", "🎙️ MC"],
    "ENTJ": ["🧠 CEO", "🏛️ 정책기획자", "💼 비즈니스 컨설턴트"]
}

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="MBTI 진로 추천✨", layout="centered")
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>💫 MBTI 기반 진로 추천 시스템 💫</h1>
    <p style='text-align: center;'>당신의 MBTI를 선택하면 찰떡같은 직업을 알려드려요! 🎯</p>
""", unsafe_allow_html=True)

mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 골라주세요! 🎈", mbti_list)

if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti} 유형을 위한 찰떡 진로 추천 💼")
    recommendations = mbti_jobs[selected_mbti]
    random.shuffle(recommendations)

    for job in recommendations:
        st.success(f"{job}")

    st.balloons()
    st.markdown("""
        <hr>
        <p style='text-align: center;'>✨ 진로는 다양해요. MBTI는 참고일 뿐, 가능성은 무한하답니다! ✨</p>
    """, unsafe_allow_html=True)
else:
    st.warning("MBTI를 선택해주세요! 🙏")
