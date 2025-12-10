from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, transactions, tax, ai, reports
from database.connection import connect_to_mongo

app = FastAPI(title="AI Personal Finance Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

app.include_router(auth.router, prefix="/auth")
app.include_router(transactions.router, prefix="/transactions")
app.include_router(tax.router, prefix="/tax")
app.include_router(ai.router, prefix="/ai")
app.include_router(reports.router, prefix="/reports")

@app.get("/")
def home():
    return {"message": "API running!"}