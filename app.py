import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

st.title("LLM質問アプリ：小学生向けスポーツ練習案提供アプリ")

st.write("##### 野球・バスケットボールの練習案を専門家が提案します")
st.write("下記からスポーツを選択し、練習テーマや質問を入力してください。")

def get_system_message(expert_type: str) -> str:
    if expert_type == "野球":
        return (
            "あなたは野球の専門家です。小学生を対象とした野球の練習案について、"
            "安全で楽しく、基礎技術が身につくような内容で専門的な知識を活かして提案してください。"
        )
    else:
        return (
            "あなたはバスケットボールの専門家です。小学生を対象としたバスケットボールの練習案について、"
            "安全で楽しく、基礎技術が身につくような内容で専門的な知識を活かして提案してください。"
        )

# スポーツ専門家の選択
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("野球", "バスケットボール")
)

# 入力フォーム
user_input = st.text_input("練習テーマや質問を入力してください:")

if st.button("送信") and user_input:
    system_message = get_system_message(expert_type)
    llm = OpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=1000)  # max_tokensを増やす
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", user_input)
    ])
    response = llm(prompt.format())
    st.markdown("### 回答")
    st.markdown(response, unsafe_allow_html=True)  # markdownで表示

