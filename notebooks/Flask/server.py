from flask import Flask, request, jsonify

app = Flask(__name__)

import pandas as pd
data = pd.read_csv('data\Topics.csv')
data['Title'] = data['Title'].str.normalize('NFKD').str.encode('ascii', errors = 'ignore').str.decode('utf-8')

@app.route('/get_recs', methods = ['PUT'])
def recommend_topic():
    input = request.get_json()
    film = input['film']
    number = int(input['number']) - 1
    topic = int(data[data['Title'].str.match(film, case = False)]['Topic'].iloc[0])
    title = data[data['Title'].str.match(film, case = False)]['Title'].iloc[0]
    top_recs = data[data['Topic'] == topic].sort_values('averageRating', ascending = False)
    top_recs = top_recs[~top_recs.Title.str.contains(film, case = False)]
    chosen_rec = top_recs.iloc[number]
    return jsonify(chosen_rec.to_json())

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
