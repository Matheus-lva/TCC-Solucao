from flask import Flask, request, jsonify
from holarafunctions import execute_holara
import base64
from flask_cors import CORS
from openaifunctions import generate_prompts

app = Flask(__name__)
CORS(app)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt')
    if prompt is None:
        return jsonify({'error': 'Missing prompt parameter'}), 400
    # Splitting parameters by newline
    prompt_params = prompt.split('\n')
    gpt_prompts = generate_prompts(prompt_params)
    print(gpt_prompts)
    image = execute_holara(gpt_prompts[0])
    image_base64 = base64.b64encode(image).decode('utf-8')
    image2 = execute_holara(gpt_prompts[1])
    image_base64_2 = base64.b64encode(image2).decode('utf-8')
    if gpt_prompts[2] == 'Description: ' or gpt_prompts[2] == 'Description:':
        gpt_prompts.pop(2)
    return jsonify({'image': image_base64, 'image2': image_base64_2, 'prompts': gpt_prompts})

if __name__ == '__main__':
    app.run(debug=True)