from flask import jsonify, request, redirect,  Response, render_template, url_for
from app import es, app
from test_app.models import Employee

index = 'names'
_type = 'python_employees'

@app.route("/")
def home():
    query = request.args.get('search')
    if query:
        return redirect(url_for('view_search', key=query))
    return render_template('index.html', **locals())

@app.route("/search/<key>")
def view_search(key):
    res = es.search(index=index, doc_type=_type, body={"query": {"match": {"name": key}}})
    print res
    if res['hits']['hits']:
        for item in res['hits']['hits']:
            e = Employee(name=item['_source']['name'] , job=item['_source']['Job'])
            e.save()
        print "done"
        
        return jsonify({'name':item['_source']['name'], 'Designation':item['_source']['Job'], 'store':'mongo'})
    else:
        return Response('Record Not Found')

@app.route("/es/")
def view_elastic_data():
    res = es.search(index=index, doc_type=_type, body={"query": {"match_all": {}}})
    return jsonify(res)
    
