from flask import Flask,jsonify,abort

app = Flask(__name__)

movies_ratings = [('The Wolf of Wall street', 8.0),('Rocky Balboa', 9.2),('The Shawsank Redemption', 9.0),('Enthiran', 10)]

@app.route('/')
def index():
    return "Testing"


@app.route('/get/movies', methods=['GET'])
def get_movies():
    print "movies"
    return jsonify(movies_ratings)

@app.route('/rating/<movie>', methods=['GET'])
def get_rating(movie):
    print movie
    rating = dict(movies_ratings).get(movie.capitalize())
    if rating is None:
        abort(404)
    return jsonify({'rating': rating})

if __name__ == '__main__':
    app.run(debug=True)
