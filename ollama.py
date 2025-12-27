from fastapi import FastAPI, Depends
import requests
from database import engine
import models
from database import session
from sqlalchemy.orm import Session
from schemas import text1,main_city,search
import logging
from datetime import datetime
import os

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def data1():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/chat")
def chats(user_prompt: text1, db: Session = Depends(data1)):

    # FIX 1: Extract the string (.prompt), don't pass the whole object
    db_data = models.data(prompt=user_prompt.prompt)

    try:
        things = {"model": "llama3", "prompt": user_prompt.prompt, "stream": False}

        # Ensure this is 127.0.0.1
        url_key=os.getenv("url")

        report = requests.post(url_key, json=things)
        report.raise_for_status()

        # FIX 2: Spelling "response" (with an S)
        ai_data = report.json().get("response", "")

        # FIX 3: Assignment (=), not Function call ()
        db_data.responce1 = ai_data
        niw = datetime.now()
        db_data.data = niw

        db.add(db_data)
        db.commit()
        db.refresh(db_data)

        return {
            "user_text": user_prompt.prompt,
            "ai_answer": ai_data,
            "id_number": db_data.id,
            "data_and_time": niw,
        }

    except Exception as e:
        logging.error(f"Crash detected: {e}")
        return {"error": str(e)}


@app.get("/data")
def real_all_chats(db: Session = Depends(data1)):
    try:
        return db.query(models.data).all()

    except Exception as e:
        logging.error(f"detais:{e}")
        return {"error": str(e)}
    
@app.post("/search_city")
def search_E(search_data : search):
    try:
        url = "http://api.openweathermap.org/geo/1.0/direct"
        params={
            "q":search_data.query,
            "limit":5,
            "appid":"",
        }
        response=requests.get(url,params=params)
        response.raise_for_status()
        data = response.json()
        results=[]
        for city in data:
            results.append({
                "city": city.get("name"),
                "country": city.get("country"),
                "lat": city.get("lat"),
                "lon": city.get("lon")
            })
        return {"match":results}
            
    except Exception as e:
        return {"error":str(e)}

@app.post("/weather_data")
def weather(city_data: main_city):

    try:
        params = {"appid": "", 
                  "q": city_data.city}
        url = "https://api.openweathermap.org/data/2.5/weather"

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
