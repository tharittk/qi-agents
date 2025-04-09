import requests
from langchain_core.messages import AIMessage
import openai
from dotenv import dotenv_values
from azure.identity import get_bearer_token_provider, ClientSecretCredential
from typing import List, Dict, Any, Tuple
import traceback

config = dotenv_values("./agent/azure.env")
tenant_id = config["AZURE_TENANT_ID"]
client_id = config["AZURE_CLIENT_ID"]
client_secret = config["AZURE_CLIENT_SECRET"]
endpoint = config["OPENAI_ENDPOINT"]

model_collection = {
    "gpt-4o": {
        "resource": "OpenAI-gpt-4o",
        "api_version": "2024-05-01-preview",
    }
}


def _get_bearer_token_provider() -> str:
    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    bearer_token_provider = get_bearer_token_provider(
        credential, "https://cognitiveservices.azure.com/.default"
    )
    access_token = bearer_token_provider()
    return access_token


class GPTModel:
    def __init__(self, temperature=0, model="gpt-4o"):
        self.gpt_model_name = model
        self.gpt_model = model_collection[self.gpt_model_name]
        self.temperature = temperature
        self.token_provider = _get_bearer_token_provider

    def _create_data(
        self,
        system: str,
        prompt: str,
    ) -> Tuple[Dict[str, Any], int]:
        data = dict()

        messages = []
        if system != "":
            messages.append({"role": "system", "content": system})

        messages.append({"role": "user", "content": prompt})
        data.update({"messages": messages})

        # TODO: More parameters
        data.update({"temperature": self.temperature})
        return data

    # Provide same interface as Ollama Models
    def invoke(self, messages):

        system = messages[0]["content"]
        user = messages[1]["content"]

        data = self._create_data(system, user)

        try:
            deployment_client = openai.AzureOpenAI(
                api_version=self.gpt_model["api_version"],
                azure_endpoint=endpoint,
                azure_ad_token_provider=self.token_provider,
            )

            response = deployment_client.chat.completions.create(
                model=self.gpt_model["resource"],
                messages=data["messages"],
                temperature=data["temperature"],
            )

            # print("Response from GPT model: ", response)
            ans = str(response.choices[0].message.content.strip())
            print("GPT Model: ", ans)
            # request_response_json = request_response.json()["response"]
            # response = str(request_response_json)
            response_formatted = AIMessage(content=ans)
            return response_formatted

        except Exception as e:
            traceback.print_exc()
            return e
