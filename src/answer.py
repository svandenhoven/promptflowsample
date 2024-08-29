import urllib.request
import json
import os
import ssl

def ask_question(question):
    prompt_flow_key = os.getenv('PROMPT_FLOW_KEY')
    if not prompt_flow_key:
        raise Exception("A key should be provided to invoke the endpoint")

    prompt_flow_endpoint = os.getenv('PROMPT_FLOW_ENDPOINT')
    if not prompt_flow_endpoint:
        raise Exception("The environment variable PROMPT_FLOW_ENDPOINT is not set")

    prompt_flow_model = os.getenv('PROMPT_FLOW_MODEL')
    if not prompt_flow_endpoint:
        raise Exception("The environment variable PROMPT_FLOW_MODEL is not set")
    
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + prompt_flow_key,
        'azureml-model-deployment': prompt_flow_model
    }

    body = json.dumps({"question": question}).encode('utf-8')
    req = urllib.request.Request(prompt_flow_endpoint, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        return result
    except urllib.error.HTTPError as error:
        error_message = (
            f"The request failed with status code: {error.code}\n"
            f"{error.info()}\n"
            f"{error.read().decode('utf8', 'ignore')}"
        )
        return error_message