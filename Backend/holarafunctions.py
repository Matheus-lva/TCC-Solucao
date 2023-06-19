import requests
import json
import base64

API_KEY = ' '
url = 'https://holara.ai/holara/api/external/1.0/generate_image'

def execute_holara(textprompt):
  
    data = {
        'api_key': API_KEY,
        'model': 'Vibrance', #required
        'num_images': 1, #required
        'prompt': textprompt, #required
        'negative_prompt': '', #optional
        'width': 512, #required
        'height': 768, #required
        'steps': 30, # optional
        'cfg_scale': 12, #optional
    }

    response = requests.request('POST', url, data=data)
    if response.status_code != 200:
        print(f'Error: {response.status_code} {response.content}')
        return None
    else:
        response = json.loads(response.content)
        # print basic response information
        print("")
        print(f'Status: {response["status"]}')
        print(f'Execution Time: {round(response["execution_time"], 2)}s')
        print(f'Generation Cost: {response["generation_cost"]}')
        print(f'Hologems Remaining: {response["hologems_remaining"]}')
        print(textprompt)
        print("")

        # if you'd like to display the image on a website, you may directly set an image element's src to the base64 string
        # if you'd like to instead save the image, you must convert the base64 string to bytes and save it to a file:
        image_base64 = response['images'][0]
        image_bytes = base64.b64decode(image_base64)
        return image_bytes
