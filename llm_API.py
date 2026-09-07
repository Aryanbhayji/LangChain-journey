from openai import OpenAI

client = OpenAI()


def ask_ai(user_message):
    response = client.responses.create(
        model="gpt-5",
        instructions="You are a helpful AI assistant.",
        input=user_message
    )

    return response.output_text


print("AI Chatbot")
print("Type 'exit' to stop.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    try:
        answer = ask_ai(user_message)
        print("AI:", answer)

    except Exception as e:
        print("Error:", e)