import streamlit as st
from flask import Flask, request, jsonify
from streamlit.web import cli

# Flask 인스턴스를 생성하여 Streamlit과 함께 사용
flask_app = Flask(__name__)

@flask_app.route('/multiply', methods=['POST'])
def multiply():
    """
    외부에서 POST 요청으로 'number'를 받아 100을 곱해서 반환하는 API 엔드포인트
    """
    data = request.get_json()  # JSON 요청 받기
    if not data or 'number' not in data:
        return jsonify({"error": "Invalid input. Please provide a 'number' field."}), 400

    try:
        number = float(data['number'])  # 숫자로 변환
        result = number * 100  # 곱하기 100
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "The 'number' must be numeric."}), 400


# Streamlit은 Flask의 URL과 함께 실행
def run_streamlit():
    st.title("Multiply API Host")
    st.write("This page is hosting an API endpoint at `/multiply`.")
    st.write("To test, send a POST request to `/multiply` with a JSON body containing a 'number'.")
    st.json({
        "endpoint": "/multiply",
        "method": "POST",
        "example_request": {
            "number": 5
        },
        "example_response": {
            "result": 500
        }
    })


if __name__ == "__main__":
    # Flask를 백그라운드로 실행
    import threading
    threading.Thread(target=lambda: flask_app.run(host="0.0.0.0", port=6000)).start()
    
    # Streamlit 실행
    cli.main()
