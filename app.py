import csv
import pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

with open('data/model.sav', 'rb') as file:
    model = pickle.load(file)

def load_questions():
    data = []
    with open('data/autism_spectrum_quotient.csv') as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader, start=1):
            data.append({
                'id': row['id'],
                'question': row['question']
            })
    return data

@app.route('/questions', methods=['GET'])
def questions():
    data = load_questions()
    response = jsonify(data)

    return response

@app.route('/diagnosis', methods=['POST'])
def diagnosis():
    inputs = [
        request.json['A1'],
        request.json['A2'],
        request.json['A3'],
        request.json['A4'],
        request.json['A5'],
        request.json['A6'],
        request.json['A7'],
        request.json['A8'],
        request.json['A9'],
        request.json['A10'],
    ]

    predict = model.predict([inputs])

    diagnosis = predict.tolist()[0]
    response = {}
    if diagnosis == 1:
        response = {
            'result': 'Autisme',
            'message': 'Anda kemungkinan mengidap autisme.'
        }
    else:
        response = {
            'result': 'Bukan Autisme',
            'message': 'Anda kemungkinan tidak mengidap autisme.'
        }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)