from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.connection import connect_to_mongo
from routes import auth, transactions, reports, ai, tax, dashboard

app = FastAPI(title="AI Personal Finance Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.get("/")
async def root():
    return {"message": "API Running!"}

app.include_router(auth.router, prefix="/auth")
app.include_router(transactions.router, prefix="/transactions")
app.include_router(tax.router, prefix="/tax")
app.include_router(ai.router, prefix="/ai")
app.include_router(reports.router, prefix="/reports")
app.include_router(dashboard.router, prefix="/dashboard")