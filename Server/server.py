from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Correcting spelling errors and retrieving POST data
        total_sqft = float(request.form['total_sqft'])  # Fixed 'total_sqrt' typo
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        # Call to util to get estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return the error if something goes wrong

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # Load artifacts when the server starts
    app.run(debug=True)
