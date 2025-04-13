from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyCG0jDK2LEOrauyvwRmLxErgrE1h1C5ims")
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
