from flask import Flask, request, jsonify
from tensorflow import keras
from pred import predict


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.json.get('review')
       
        print(type(name))
        prediction = predict(name)
        return prediction
        
            #return name
    else:
        return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(port= 50001,debug=True)                                                         