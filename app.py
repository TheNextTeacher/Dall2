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
    return generation_response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8761)

