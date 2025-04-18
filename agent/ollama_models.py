import requests
import json
from langchain_core.messages import AIMessage


class OllamaModel:
    def __init__(self, temperature=0, model="llama3-groq-tool-use:latest"):
        self.headers = {"Content-Type": "application/json"}
        self.model_endpoint = "http://localhost:11434/api/generate"
        self.temperature = temperature
        self.model = model

    def invoke(self, messages):

        # This is tightly formatted in agent invoke method
        system = messages[0]["content"]
        user = messages[1]["content"]

        payload = {
            "model": self.model,
            "prompt": user,
            "system": system,
            "stream": False,
            "temperature": 0,
        }

        try:
            request_response = requests.post(
                self.model_endpoint, headers=self.headers, data=json.dumps(payload)
            )

            request_response_json = request_response.json()["response"]
            response = str(request_response_json)
            response_formatted = AIMessage(content=response)

            return response_formatted
        except requests.RequestException as e:
            response = {"error": f"Error in invoking model! {str(e)}"}
            response_formatted = AIMessage(content=response)
            return response_formatted
