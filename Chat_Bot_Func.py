from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def mistral(api_key, query):
    client = MistralClient(api_key=api_key)
    model = "mistral-large-latest"
    chat_response = client.chat(model=model,
                                messages=[ChatMessage(role="user", content=query)]
                                )

    return chat_response.choices[0].message.content