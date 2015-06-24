echo "GET Method"
curl -i -H "Content-Type: application/json" -X GET  http://localhost:5000/rating/

echo "POST Method"
curl -i -H "Content-Type: application/json" -X POST -d '{"movie":"Avengers", "rating":"8.5"}' http://localhost:5000/rating/add/

echo "PUT Method"
curl -i -H "Content-Type: application/json" -X PUT -d '{"rating":"7.7"}' http://localhost:5000/rating/update/Avengers

echo "DELETE Method"
curl -i -H "Content-Type: application/json" -X DELETE -d '{"rating":"6.5"}' http://localhost:5000/rating/del/Avengers

echo "GET Method again"
curl -i -H "Content-Type: application/json" -X GET  http://localhost:5000/rating/

