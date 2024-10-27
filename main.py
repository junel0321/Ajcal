from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/add")
def add(x: float, y: float):
    return {"operation": "addition", "result": x + y}

@app.get("/subtract")
def subtract(x: float, y: float):
    return {"operation": "subtraction", "result": x - y}

@app.get("/multiply")
def multiply(x: float, y: float):
    return {"operation": "multiplication", "result": x * y}

@app.get("/divide")
def divide(x: float, y: float):
    if y == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    return {"operation": "division", "result": x / y}



