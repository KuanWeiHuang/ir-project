import os
# import time
import sys
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Page of post method
    if request.method == 'POST':
        # get the user's query
        query = request.form.get('query')
        # redirect to the result page
        return redirect(url_for('query_result',
                                    query=query))

    # Page of get method
    return render_template('index.html')

@app.route('/queryResult/<query>')
def query_result(query):
    tStart = time.time()
    # pass the query to the ranking function and get the 20 result docs
    docs = ranking.ranking3(query)

    tEnd = time.time()
    # get the execution duration and round it to the second decimal place
    executeTime = round(tEnd - tStart, 2)
    # # get the invertedList size in KB
    size = round(sys.getsizeof(docs) / 1024.0, 2)

    # use the index2.html template to show the result
    return render_template('index2.html',header='CS6200 Information Retrieval', sub_header='Kuan-Wei Huang',
                            list_header="Execution Time: " + str(executeTime) + " seconds, Space used: " + str(size) + " KB",
                            query=query, docs=docs)

if __name__ == '__main__':
    app.run(debug=True)