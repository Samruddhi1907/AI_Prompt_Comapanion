from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # Enable CORS for frontend to communicate with backend
GEMINI_API_KEY = YOUR_API_KEY # Your unique API Key

# Gemini API endpoint
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route('/')
def index():
    """Serves the main HTML file for the frontend."""
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles chat requests from the frontend.
    Receives user prompt and conversation history, calls Gemini API, and returns response.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_ACTUAL_UNIQUE_API_KEY_PASTE_HERE":
        return jsonify({"error": "API Key not configured on the backend. Please ensure GEMINI_API_KEY is correctly set in ai_companion_backend.py"}), 500

    data = request.json
    user_prompt = data.get('userPrompt')
    frontend_chat_history = data.get('chatHistory', [])

    if not user_prompt:
        return jsonify({"error": "No user prompt provided."}), 400

    api_chat_history = []

    # This tells the model how to format its code output.
    api_chat_history.append({"role": "user", "parts": [{"text": "You are an AI assistant. When providing code, always format it within a Markdown code block, specifying the language (e.g., ```python\\nprint('Hello')\\n```). Also, provide explanations in regular text."}]})
    api_chat_history.append({"role": "model", "parts": [{"text": "Understood. I will format all code within Markdown code blocks and provide explanations in regular text."}]})


    for msg in frontend_chat_history:
        if msg['role'] == 'user':
            api_chat_history.append({"role": "user", "parts": [{"text": msg['text']}]})
        elif msg['role'] == 'ai' and msg['type'] not in ['Error', 'Initial Welcome']:
            api_chat_history.append({"role": "model", "parts": [{"text": msg['text']}]})
    
    api_chat_history.append({"role": "user", "parts": [{"text": user_prompt}]})

    if len(api_chat_history) > 1 and api_chat_history[-1]['role'] == api_chat_history[-2]['role']:
        print("Warning: Consecutive roles detected in API chat history. This might cause a Bad Request from Gemini.")

    payload = {
        "contents": api_chat_history
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload)
        response.raise_for_status()
        
        gemini_result = response.json()
        print(f"DEBUG: Raw Gemini API Response: {gemini_result}")

        if gemini_result.get('candidates') and len(gemini_result['candidates']) > 0 and \
           gemini_result['candidates'][0].get('content') and \
           gemini_result['candidates'][0]['content'].get('parts') and \
           len(gemini_result['candidates'][0]['content']['parts']) > 0:
            ai_text_response = gemini_result['candidates'][0]['content']['parts'][0]['text']
            return jsonify({"response": ai_text_response})
        else:
            if gemini_result.get('promptFeedback') and gemini_result['promptFeedback'].get('blockReason'):
                block_reason = gemini_result['promptFeedback']['blockReason']
                return jsonify({"error": f"Response blocked by safety filters: {block_reason}. Please try a different prompt."}), 400
            return jsonify({"error": "Unexpected response structure from AI or empty content."}), 500

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh.response.status_code} - {errh.response.text}")
        return jsonify({"error": f"HTTP Error {errh.response.status_code}: {errh.response.text}"}), errh.response.code
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return jsonify({"error": f"Connection Error: {errc}"}), 500
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return jsonify({"error": f"Timeout Error: {errt}"}), 500
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
        return jsonify({"error": f"Request Error: {err}"}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": f"An unexpected server error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
