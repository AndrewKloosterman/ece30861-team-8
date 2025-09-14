from typing import Literal
from classes.llm_child_api import GenAiChatApi

url_type = Literal["model", "dataset", "code", "invalid"]

def identify_urltype(url: str, api_key: str) -> url_type:

    # Set prompt
    prompt = f"""
        Classify the given URL into exactly one of the following categories:

        - ML/AI model
        - A dataset used to train a ML/AI model
        - The source code to an ML/AI model
        - None of the Above

        Rules:
        1. Huggingface URLs
            a. If the path contains "/datasets/", classify as dataset.
            b. Otherwise, if it's a huggingface.co repo, classify as model.
            c. Hugging Face URLs are never "code".
        2. GitHub URLs are always "code".
        3. If the URL does not match these patterns, classify as "invalid".

        URL: {url}

        Answer with only one word: model, dataset, code, invalid
    """
    # Initialize the client
    chat_api = GenAiChatApi(
        base_url="https://genai.rcac.purdue.edu",
        model="llama3.1:latest"
    )

    # Set the token
    chat_api.set_bearer_token(api_key)

    # Ask for response
    response = chat_api.get_chat_completion(prompt)
    
    #Formatting response (precautionary) and return
    formatted_response = response.strip().lower()
    if formatted_response in ["model", "dataset", "code", "invalid"]:
        return formatted_response
    return False
