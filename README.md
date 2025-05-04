📄 智能客服系統 - 專案說明本專案是一個使用 FastAPI + MongoDB 搭配 Angular Material 建構的智能客服系統，具備常見問題查詢、GPT 回答與 UI 互動功能，適合部署至雲端或本地開發測試。

🧩 技術架構前端：Angular 15+、Angular Material UI
後端：FastAPI、Pymongo
資料庫：MongoDB Atlas
AI 模型：OpenAI GPT-3.5
部署平台：Zeabur / Local

📁 專案結構 fax-management/
├── backend/ # FastAPI 後端
│ ├── main.py # FastAPI 入口
│ ├── routes.py # API 路由定義
│ ├── database.py # MongoDB 連線設定
│ ├── openai_client.py # GPT 串接邏輯
│ ├── models.py # Pydantic 資料模型
│ └── seed.py # 初始 FAQ 資料填充
│
├── frontend/ # Angular 前端
│ ├── src/app/pages/chat-bot/
│ │ └── chat-bot.component.\* # 客服聊天 UI
│ ├── proxy.conf.json # 本地 API 代理設定
│ └── app.routes.ts # 路由配置
│
├── package.json # 可選的通用啟動指令
└── README.md # 本說明文件

📦 MongoDB FAQ 資料格式
{
"question": "如何開戶？",
"answer": "請攜帶身分證及健保卡至分行辦理。",
"category": "service"
}
