import os
from flask import Flask, request, jsonify, json
from dotenv import load_dotenv
from predict.task import predict_image

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        return jsonify({"message":"index"}), 200
    
@app.route("/predict", methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return jsonify({"message":"predict"}), 200
    else:
        data = json.loads(request.data)
        predict_image.apply_async(queue="predict_image", args=[data])
        return jsonify({"message":"OK"}), 200
    

if __name__ == "__main__":
    app.run(host=os.getenv("API_HOST"), port=os.getenv("API_PORT"))
