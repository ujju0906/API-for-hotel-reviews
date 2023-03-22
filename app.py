from flask import Flask, request, jsonify
#import Tensorflow 
#from tensorflow.keras import load_models
app = Flask(__name__)

@app.route('/home/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.json.get('name')
        message = f'Hello, {name}!'
        #model = load_models('my_best_model.hdf5')
        return jsonify({'message': message})
    else:
        return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(port= 50000,debug=True)