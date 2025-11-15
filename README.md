🚀 FastAPI + MongoDB

A simple FastAPI backend with MongoDB, running inside a Python virtual environment.

▶️ How to Start This App (Windows)
1️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt


Or install manually:

pip install fastapi uvicorn[standard] motor pydantic pydantic-settings email-validator

3️⃣ Create .env in project root
MONGO_URL=your-mongo-url-here
DB_NAME=your-db-name

4️⃣ Run the Server
python -m uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000


API Docs:

http://127.0.0.1:8000/docs

🛑 Stop the Server
CTRL + C
