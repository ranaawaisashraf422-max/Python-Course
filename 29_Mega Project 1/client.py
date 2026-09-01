from openai import OpenAI

client = OpenAI()

#defaults to getting the key using os.environ.get("OPEN_API_KEY")
# if you saved the key under a different environment variable name, you can do something like this:
client = OpenAI(
api_key="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",)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message)
#pip install openai