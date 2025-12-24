import tkinter as tk
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

# Create a Tkinter window
window = tk.Tk()
window.title("My Assistant")

# Create a text box for displaying results
result_box = tk.Text(window, height=10, width=50)
result_box.pack()


# Create a function to handle user input
def handle_input():
    # Use speech recognition to get user input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Convert user input to text
    try:
        text = r.recognize_google(audio)
    except:
        print("Could not understand audio")
        return

    # Use the text to search the web
    url = f"https://www.google.com/search?q={text}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the first result and display it
    result = soup.find("div", class_="g").find("a").text
    result_box.insert(tk.END, result)


# Create a button to trigger user input
input_button = tk.Button(window, text="Ask me something", command=handle_input)
input_button.pack()

# Start the Tkinter event loop
window.mainloop()