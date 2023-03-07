import os
import cv2
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv


load_dotenv()

UPLOAD_FOLDER      = './upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    if request.method == 'GET':
        return jsonify({"message":"index"}), 200

  
@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == 'GET':
        return jsonify({"message":"predict get method"}), 200
    
    if "file" not in request.files:
        return jsonify({"message":"no file found"}), 400
    
    file = request.files['file']
    if request.files['file'].filename == '':
            return jsonify({"message":"No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        path_file = os.path.abspath(os.path.join(os.getcwd(),"upload",filename))

        cascade_src = "cooking_oil.xml"
        car_cascade = cv2.CascadeClassifier(cascade_src)

        img  = cv2.imread(path_file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        items = car_cascade.detectMultiScale(gray, 1.1, 1)  

        return jsonify({"message":len(items)}), 200
    

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("API_HOST"), port=int(os.getenv("API_PORT")))
