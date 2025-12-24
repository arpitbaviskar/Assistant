# 🧠 My Assistant — A Voice-Activated Search App

My Assistant is a Python desktop application that listens to your voice, interprets your question using speech recognition, performs a Google search, and displays the first result in a graphical window. It combines simplicity with the power of web automation.

---

## 🚀 Features
- 🎙️ **Voice Recognition:** Speak your query instead of typing.
- 🌐 **Instant Search:** Automatically searches Google for your request.
- 🪶 **Lightweight GUI:** Built with Tkinter for a simple, intuitive interface.
- 🧩 **Web Scraping:** Uses BeautifulSoup to extract the top result.

---

## 🧰 Technologies Used
- **Python 3.x**
- **Tkinter** – for building the GUI  
- **SpeechRecognition** – to convert your speech to text  
- **Requests** – to fetch search results from the web  
- **BeautifulSoup4** – for parsing HTML content  

---

## ⚙️ Installation

1. **Clone this repository**
git clone https://github.com/your-username/my-assistant.git
cd my-assistant

text

2. **Install dependencies**
pip install tkinter
pip install SpeechRecognition
pip install requests
pip install beautifulsoup4
pip install pyaudio # required for microphone input

text

3. **Run the app**
python my_assistant.py

text

---

## 🧠 How It Works
1. Click on **"Ask me something"** in the GUI.  
2. Speak your query clearly into your microphone.  
3. The app captures your voice, sends it to Google’s speech recognition API, and converts it into text.  
4. It performs a Google search for your query.  
5. The first search result appears in the text box.

---

## ⚠️ Notes
- Make sure your microphone is connected and working.
- Internet access is required for search queries.
- Google may block frequent automated requests, so use responsibly.

---

## 🎯 Future Improvements
- Add voice output for responses.
- Integrate with official search APIs instead of scraping.
- Enhance error handling and support multiple results.

---


## 📄 License
This project is licensed under the MIT License — feel free to use, modify, and share!
