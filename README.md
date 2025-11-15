# 🚀 FastAPI + MongoDB Starter (Windows Guide)

A simple FastAPI backend with MongoDB using Motor, Pydantic v2, and a clean modular structure.

---

## 📦 Requirements
- Windows 10 / 11
- Python 3.9+
- MongoDB Local or MongoDB Atlas

---

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
or
pip install fastapi uvicorn[standard] motor pydantic pydantic-settings email-validator
python -m uvicorn app.main:app --reload
