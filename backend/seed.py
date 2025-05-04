# backend/seed.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
collection = db["faqs"]

# 刪除原有資料
collection.delete_many({})

# 插入預設 FAQ（分類）
faq_data = [
    {"question": "如何申請數位帳戶？", "answer": "您可以透過官網或行動銀行線上申請。", "category": "account"},
    {"question": "我可以變更手機號碼嗎？", "answer": "請至分行或網銀進行變更。", "category": "account"},
    {"question": "客服服務時間？", "answer": "客服全年無休，24 小時提供服務。", "category": "service"},
    {"question": "如何查詢交易紀錄？", "answer": "請登入網銀後點選交易查詢。", "category": "order"},
    {"question": "是否有跨行轉帳手續費？", "answer": "視帳戶類型而定，數位帳戶有免費額度。", "category": "order"}
]

collection.insert_many(faq_data)
print("✅ 清除完畢，並插入預設 FAQ（分類）")