import os 
import google.generativeai as genai
from dotenv import load_dotenv

# load environment variable from the .env file
load_dotenv()

# Configuring the Gemini API with the key from .env file
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    print("Error! The GEMINI_API_KEY was not found.")
    exit()

# Creating the Generative Model
model = genai.GenerativeModel('gemini-2.0-flash')

# Start a chat session with no context or history
chat = model.start_chat(history=[])

#Main Chat Loop
print("Gemini Chatbot is ready! We are using 2.0 flash version! Type 'quit' if you want to exit the chatbot.")
print("="*50)

while True:
    #Get input from the user
    user_input = input("You : ")

    if not user_input.strip():
        print("Gemini needs something to work with you idiot!")
        continue
        #Skips to the next iteration of the loop if data is null

    #Check if the user wants to exit the chatbot
    if user_input.lower() == "quit":
        print("\nGoodbye thank you for chatting with Gemini 2.0 flash")
        break

    try:
        # User input is sent to the LLM
        response = chat.send_message(user_input, stream=True)

        #Printing the LLM's response
        print("Gemini : ",end="")
        for chunk in response:
            print(chunk.text, end="")
        print("\n")
    except Exception as e:
        print(f"Gemini has an error occur while getting a response : {e}")
        print("\n")
    


