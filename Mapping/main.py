from fastapi import FastAPI, Query
from typing import List
import  services
app = FastAPI()

@app.get("/mapper")
async def get_purchase_order(key: List[str] = Query(None), value: List[str] = Query(None)):
    return services.data_mapper(key, value)