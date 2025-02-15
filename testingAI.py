from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_input = input("Give me your notes to make Quizlet style questions: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Make flashcard type questions based on {user_input}"}
    ]
)

# Print only the AI's response content
print("\nAI Response:\n")
print(completion.choices[0].message.content)