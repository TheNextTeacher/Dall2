from flask import Flask, request, jsonify
import openai
app = Flask(__name__)

openai.api_key = "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"

@app.route('/generate-image', methods=['GET'])
def generate_image():
    prompt = request.args.get('prompt')

    if not prompt:
        return jsonify({"error": "需要输入提示(prompt)。"}), 400

    generation_response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url",
    )

    image_url = generation_response['data'][0]
    markdown_image = f"![Alt Text]({image_url})"

    return markdown_image

if __name__ == '__main__':
    app.run(port=8080)
