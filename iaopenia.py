import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("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")


response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

print(response)








