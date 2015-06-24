from flask import Flask, jsonify, abort, request

app = Flask(__name__)

movies_ratings = {'The Wolf of Wall street': 8.0, 'Rocky Balboa': 9.2, 'The Shawsank Redemption': 9.0,'Enthiran': 10 }

@app.route('/')
def index():
    return "Testing"


@app.route('/rating/', methods=['GET'])
def get_movies():
    print "movies"
    return jsonify(movies_ratings)


@app.route('/rating/<movie>', methods=['GET'])
def get_rating(movie):
    print movie
    rating = movies_ratings.get(movie.capitalize())
    if rating is None:
        abort(404)
    return jsonify({'rating': rating})


@app.route('/rating/add/', methods=['POST'])
def register_movie():
    """
    curl -i -H "Content-Type: application/json" -X POST -d '{"movie":"Avengers", "rating":"8.5"}' http://localhost:5000/rating/add/
    """
    print request.json
    if not request.json or not 'movie' in request.json:
        abort(400)
    movies_ratings.update({request.json['movie']: float(request.json['rating'])})
    return jsonify({'Total Records':movies_ratings, \
                    'movie': {request.json['movie']: float(request.json['rating'])}, \
                    'add':True})


@app.route('/rating/update/<movie>', methods=['PUT'])
def update_movie_rating(movie):
    """
    curl -i -H "Content-Type: application/json" -X PUT -d '{"movie":"Avengers 2", "rating":"6.5"}' http://localhost:5000/rating/update/Avengers
    """
    print movie, request.json
    if not request.json or not 'rating' in request.json:
        abort(400)
    if movies_ratings.get(movie):
        movies_ratings[movie] = float(request.json['rating'])
        return jsonify({'Total Records':movies_ratings, 'movie': movie, \
                        'rating': movies_ratings[movie], 'update':True})
    else:
        abort(404)


@app.route('/rating/del/<movie>', methods=['DELETE'])
def remove_movie(movie):
    """
    curl -i -H "Content-Type: application/json" -X DELETE -d '{"rating":"6.5"}' http://localhost:5000/rating/del/Avengers
    """
    if movies_ratings.get(movie):
        del movies_ratings[movie]
        return jsonify({'movie':movie,'Total Records':movies_ratings, 'delete':True})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
