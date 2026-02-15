from google import genai 

client = genai.Client(api_key="AIzaSyCID85nBbkIwRFeZ49UMipL2RudRMEErY8")

chat = client.chats.create(model="gemini-3-flash-preview")

response = chat.send_message("Hello!")
print("Gemini", response.text)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)