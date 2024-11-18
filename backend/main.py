from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

# DB 세션 의존성 주입
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

