# Import the necessary libraries
import os
import keyboard
import pyperclip
import time
import requests
import openai
import tkinter as tk

# Set up the OpenAI API key
# Replace "YOUR API KEY HERE" with your actual OpenAI API key
openai.api_key = "YOUR API KEY HERE"

# Define the GPT engine
# We're using the "text-davinci-003" engine for this script
engine = "text-davinci-003"

# Define the hotkey
# We're using the 'win+alt+c' hotkey to trigger the script
keyboard.add_hotkey('win+alt+c', lambda: send_to_gpt())

# Define the function that sends the highlighted text to GPT
def send_to_gpt():
    # Get the highlighted text from the clipboard
    highlighted_text = pyperclip.paste()

    # Send the text to GPT
    # We're asking for a maximum of 1024 tokens in the response
    response = openai.Completion.create(
        engine=engine,
        prompt=highlighted_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response from GPT
    gpt_response = response.choices[0].text

    # Copy the response to the clipboard
    pyperclip.copy(gpt_response)

    # Display the response in a GUI window
    root = tk.Tk()
    root.title("GPT Response")

    label = tk.Label(root, text=gpt_response)
    label.pack()

    root.mainloop()

# Wait for the user to press a key
# The script will keep running until the user presses the defined hotkey
while True:
    pass
