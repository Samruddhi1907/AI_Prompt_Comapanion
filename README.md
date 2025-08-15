# AI Prompt Companion

### An Interactive Full-Stack AI Chat Application

![Project Screenshot Placeholder](https://placehold.co/800x450/EAE7ED/333333?text=Add+your+project+screenshot+here)

## Project Overview

The **AI Prompt Companion** is a robust, full-stack web application that provides a chat interface for interacting with a Large Language Model (LLM). It demonstrates a complete client-server architecture where a **Python Flask backend** securely manages the AI API communication and a responsive **HTML/JavaScript frontend** delivers a dynamic user experience.

This project is an excellent starting point for anyone looking to build a custom, AI-powered application.

## Features

* **Interactive Chat Interface:** A clean and responsive user interface for seamless conversation.
* **Real-time AI Responses:** Powered by the **Google Gemini 2.0 Flash API** for fast, dynamic content generation.
* **Markdown Rendering:** Displays rich text and formatted code blocks in a readable manner.
* **Conversation Context:** The backend maintains conversation history to provide context-aware responses.
* **Secure API Key Handling:** The Gemini API key is securely stored on the backend, away from the client-side code.
* **Simple & Scalable Architecture:** A clear separation of concerns between the frontend and backend makes the project easy to understand and extend.

## Technologies Used

### Backend
* **Python 3.x:** The core language for the server.
* **Flask:** A lightweight web framework for the backend API.
* **Requests:** A popular library for making HTTP requests to the Gemini API.
* **Flask-CORS:** Manages Cross-Origin Resource Sharing.

### Frontend
* **HTML5:** The structure of the web page.
* **JavaScript (ES6+):** Provides all the interactive functionality.
* **Tailwind CSS:** A utility-first CSS framework for rapid styling.
* **Marked.js:** A JavaScript library used to parse and render Markdown content.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* **Python 3.8+**
* **pip** (Python package installer)
* A **Google Cloud API Key** with the **Generative Language API** enabled. You can get one from the [Google Cloud Console](https://console.cloud.google.com/).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/ai-prompt-companion.git](https://github.com/your-username/ai-prompt-companion.git)
    cd ai-prompt-companion
    ```

2.  **Set up the backend:**
    Navigate to the project's root directory and install the required Python packages.
    ```sh
    pip install -r requirements.txt
    ```
    *Note: The `requirements.txt` file should contain `Flask`, `requests`, and `flask-cors`.*

3.  **Configure your API Key:**
    Open the `ai_companion_backend.py` file and replace `"YOUR_GEMINI_API_KEY"` with your actual API key.
    ```python
    # ai_companion_backend.py
    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY" # <-- Paste your API key here
    ```

### Running the Application

1.  **Start the Flask backend:**
    From the project's root directory, run the Python script.
    ```sh
    python ai_companion_backend.py
    ```
    The server will start and be accessible at `http://127.0.0.1:5000/`.

2.  **Access the web app:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`. You should now see the AI Prompt Companion running.

## File Structure

```
ai-prompt-companion/
├── ai_companion_backend.py     # The Python Flask backend
├── index.html              # The frontend HTML file
└── README.md                   # This file
```

## Future Enhancements

* **Streaming Responses:** Implement server-sent events or websockets to receive responses from the API in real-time, word-by-word.
* **Database Integration:** Use a database (like SQLite or Firestore) to save and retrieve chat history.
* **User Authentication:** Add user login functionality to provide personalized chat histories.
* **Copy-to-Clipboard Button:** Add a small button to each code block to allow for easy copying.
* **Dark Mode:** Implement a toggle to switch between light and dark themes.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

* **Google Gemini API** for providing the core AI functionality.
* **Flask** for the elegant and simple web framework.
* **Tailwind CSS** for making styling a breeze.
* **Marked.js** for Markdown rendering.
