import os
from google import genai

os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"


client = genai.Client()

print("Google Gemini AI Chatbot is Ready! (Type 'exit' to quit)\n")

while True:
    user_input = input("your query: ")
    if user_input.lower() == 'exit':
        break
        
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input,
        )
        print(f"AI: {response.text}\n")
    except Exception as e:
        print(f"Error occurred: {e}\n")
