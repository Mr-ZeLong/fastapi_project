from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    """根路径处理函数，返回欢迎信息。"""
    return {"Hello": "World"}