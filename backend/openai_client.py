import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion

load_dotenv()

# 初始化 OpenAI Client（>=1.0）
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def filter_relevant_faqs(question: str, faqs: List[Dict], limit: int = 3) -> List[Dict]:
    """
    根據使用者提問中的關鍵字過濾 FAQ（用於縮短 token 使用）
    """
    keywords = set(question.lower().split())
    scored = []
    for faq in faqs:
        score = sum(1 for word in keywords if word in faq["question"].lower())
        if score > 0:
            scored.append((score, faq))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [faq for _, faq in scored[:limit]] if scored else faqs[:limit]


def ask_gpt(question: str, faqs: List[Dict]) -> str:
    """
    傳送問題與相關 FAQ 給 GPT，取得簡短回覆
    """
    relevant_faqs = filter_relevant_faqs(question, faqs)

    faq_prompt = "\n".join(
        [f"Q: {f['question']}\nA: {f['answer']}" for f in relevant_faqs]
    )

    prompt = (
        f"你是銀行的智能客服，請根據以下 FAQ 回答使用者問題。\n\n"
        f"{faq_prompt}\n\n使用者問：{question}"
    )

    try:
        response: ChatCompletion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "你是銀行客服，請根據資料提供簡潔正確的回覆。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300,  # 控制字數與成本
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ 無法回覆：{e}"
