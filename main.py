from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# استخدم متغير البيئة بدلاً من كتابة المفتاح في الكود
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

@app.route('/ask')
def ask():
    msg = request.args.get('msg')
    if not msg:
        return jsonify({"error": "يرجى كتابة msg في الرابط"}), 400
    try:
        response = model.generate_content(msg)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})
