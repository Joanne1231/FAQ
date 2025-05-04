from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from database import faq_collection
from openai_client import ask_gpt

router = APIRouter()


class ChatInput(BaseModel):
    question: str = Field(..., example="我想開戶怎麼辦？")

@router.post("/chat")
async def chat_with_bot(payload: ChatInput):
    question = payload.question.strip()

    # 嘗試從 MongoDB 模糊比對（簡易關鍵字比對）
    keyword = {"$regex": question, "$options": "i"}
    matched = faq_collection.find_one({"question": keyword}, {"_id": 0, "answer": 1})

    if matched:
        return {"answer": matched["answer"]}

    # 若無匹配，則 fallback 給 GPT
    faqs = list(faq_collection.find({}, {"_id": 0, "question": 1, "answer": 1}))
    response = ask_gpt(question, faqs)

    return {"answer": response}


@router.get("/faqs/init")
async def get_all_faqs():
    try:
        result = list(
            faq_collection.find(
                {}, {"_id": 0, "question": 1, "answer": 1, "category": 1}
            )
        )
        return result
    except Exception as e:
        print(f"❌ FAQ 初始化錯誤: {e}")
        return []
