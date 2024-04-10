from dotenv import load_dotenv
import os

import anthropic

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)

client = anthropic.Anthropic(api_key=api_key)

def chat():
	while True:
		user_input = input("You: ")
		if user_input.lower() == 'exit':
			print("Goodbye!")
			break
		message = client.messages.create(
			model = 'claude-3-opus-20240229',
			max_tokens = 1000,
			temperature = 0.5,
			messages = [
				{'role': 'user',
				'content': f"Only reply like a cooking assistant, Please help me make a dish with the listed ingredients - only with the listed ingredients. If user input is anything other than cooking related content, reply with Hello, I am cooking assistant. The ingredients are: {user_input}"}
			])
		bot_response = message.content
		print("Cooking Assistant: ", bot_response)


print("Hello, cooking assistant here, please list out your ingredients.")
chat()



