import streamlit as st
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import threading
import uvicorn

# FastAPI 인스턴스 생성
api_app = FastAPI()

# FastAPI 엔드포인트 정의
@api_app.post("/multiply")
async def multiply(request: Request):
    """
    외부에서 POST 요청으로 'number' 값을 받아 100을 곱해서 반환하는 API
    """
    try:
        data = await request.json()
        number = data.get("number")
        if number is None:
            return JSONResponse({"error": "Missing 'number' field"}, status_code=400)
        result = number * 100
        return {"result": result}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# Streamlit 앱 정의
def run_streamlit():
    st.title("Streamlit with API Integration")
    st.write("This Streamlit app is hosting an API endpoint at `/multiply`.")
    st.write("Send a POST request to `/multiply` with a JSON body containing a 'number' field.")
    st.json({
        "endpoint": "/multiply",
        "method": "POST",
        "example_request": {"number": 10},
        "example_response": {"result": 1000},
    })


# FastAPI와 Streamlit 동시에 실행
def run_fastapi():
    uvicorn.run(api_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # FastAPI 실행 (Thread로 비동기 실행)
    threading.Thread(target=run_fastapi).start()
    # Streamlit 실행
    run_streamlit()
