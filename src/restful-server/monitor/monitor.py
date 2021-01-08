from fastapi import FastAPI
# import array
from _rmt_py_wrapper import *

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "RMT_VERSION": RMT_VERSION
    }

@app.get("/search/{opt_num}")
async def search(opt_num: int):    
    result = rmt_search(opt_num)
    return {        
        "result": result
    }

@app.get("/monitor/robot-{robot_id}")
async def monitor_robot(robot_id: str):
    if robot_id == "all":        
        return {
            "target": robot_id,
            #"content": rmt_get();
        }   
    else:
        return {
            "target": robot_id,
            "content": {
                "test": 1,
            }
        }