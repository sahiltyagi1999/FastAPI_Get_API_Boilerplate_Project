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

```
## Key Learnings-

- Here in Model Unlike Node Project we dont store schema, there is no concept of writing schema in FastAPI, here we store I/O response Structure Only 
- Inside db/user.py here we have main DB call functions liek we used to have in Node JS, here we also map reponse in format we want by serealising it
- Inside API folder we only have routers just like we had routes in Node JS
- Service folder is basically used if you want to add any logic after getting DB response
