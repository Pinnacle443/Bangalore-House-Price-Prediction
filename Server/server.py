from flask import Flask, request, jsonify
app = Flask(__name__)
import util


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })

    return response


    return "hii"

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()