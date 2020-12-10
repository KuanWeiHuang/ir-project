# import os
# import time
import sys
from query import search_query
from music import Music
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
    count, datas = search_query(query)    
    # use the index2.html template to show the result
    return render_template('index2.html',header='IMSLP / Petrucci Music Library', query=query, datas=datas, count=count)

if __name__ == '__main__':
    app.run(debug=True)