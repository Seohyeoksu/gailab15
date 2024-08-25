import os
from openai import OpenAI
import streamlit as st

# Set up the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Configure the Streamlit page
st.set_page_config(
    page_title="카피라이터",
    page_icon="✒️",  # Elegant icon for the page
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for a more sophisticated, weighty UI
st.markdown("""
    <style>
        body {
            background-image: url('https://your-image-url-here.jpg'); /* Add your background image URL here */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            font-family: 'Georgia', serif; /* Formal, serif font for a classic feel */
        }
        .main {
            background-color: rgba(30, 30, 30, 0.9); /* Dark background with transparency */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5); /* Heavier shadow for a more solid feel */
            color: white; /* White text for contrast */
        }
        h1 {
            color: #BDB76B; /* Darker, muted gold for the heading */
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .section {
            margin-bottom: 20px;
        }
        label[for="주제"], label[for="장르"], label[for="글자 수"], label[for="느낌"] {
            font-size: 18px;
            color: white; /* White color for specific labels */
            font-weight: bold;
            margin-bottom: 5px;
            background-color: transparent; /* Ensure the background remains transparent */
        }
        textarea, .stTextInput, .stSelectbox {
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #8B4513; /* Dark brown border for inputs */
            background-color: #2F4F4F; /* Dark slate gray background for inputs */
            color: white; /* White text inside inputs */
        }
        .stButton>button {
            background-color: #8B4513; /* Dark brown button */
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #A0522D; /* Slightly lighter brown on hover */
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 30px;
            color: #BDB76B; /* Matching muted gold for footer text */
            padding: 20px 0;
            border-top: 1px solid #8B4513;
        }
        .footer img {
            width: 50px; /* Adjusted icon size */
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the application with an elegant icon
st.markdown("<h1>✒️ 카피라이터</h1>", unsafe_allow_html=True)

# User inputs organized in sections
st.markdown("<div class='section'>", unsafe_allow_html=True)

# Replace playful icons with more serious ones
topic_keyword = st.text_area("🖋️ 주제", height=100, placeholder="주제를 입력하여 주세요. 예시) 학교폭력, 학예회 공연명")
grade_options = ["📜 현수막", "📣 캠페인 문구", "📄 문서 제목", "📢 공지 사항", "🎟️ 행사명"]
grade_keyword = st.selectbox("🗂️ 장르", grade_options)

subject_options = ["✏️ 20자", "🖋️ 40자", "📏 60자", "📝 80자"]
subject_keyword = st.selectbox("🖋️ 글자 수", subject_options)

feeling_options = ["⚖️ 딱딱한", "🏛️ 권위적인", "🤝 친근한", "🌞 밝은", "🔥 활기찬", "💧 부드러운"]
feeling_keyword = st.selectbox("🎨 느낌", feeling_options)

st.markdown("</div>", unsafe_allow_html=True)

# Generate button
if st.button('📜 생성하기', key='generate_button'):
    with st.spinner('생성 중입니다...'):
        # Combine keywords into a single input
        keywords_combined = f"주제: {topic_keyword}, 장르: {grade_keyword}, 글자 수: {subject_keyword}, 느낌: {feeling_keyword}"
        
        # Create a chat completion request to OpenAI API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keywords_combined,
                },
                {
                    "role": "system",
                    "content": 
                        "당신은 교육과 관련된 문구를 전문적으로 만드는 카피라이터입니다. "
                        "입력받은 주제, 입력받은 느낌, 입력받은 장르, 입력받은 글자 수에 맞게 "
                        "전문가의 역량을 발휘하여 10개의 문구를 만들어 주세요. "
                        "1. 조건에 맞게 10개의 문구만 만들면 됩니다. "
                        "2. ~다.로 끝나는 문장은 사용하지 마세요. "
                        "3. 당신은 전문 카피라이터이니 그에 맞게 문장을 만들어 주세요."
    
                    
                }
            ],
            model="gpt-4o",
        )

        # Extract the generated content
        result = chat_completion.choices[0].message.content

        # Display the result in Streamlit app
        st.write(result)
st.markdown("""
<div class="footer">
    <img src="https://huggingface.co/spaces/powerwarez/gailabicon/resolve/main/gailab02.png" alt="icon"> 제작자: 교사 서혁수
</div>
""", unsafe_allow_html=True)