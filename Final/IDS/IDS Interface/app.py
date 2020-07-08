from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

app._static_folder = './static'

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

# @app.route("/result", methods=['GET', 'POST'])
# def result():
#     if request.method == 'GET':
#         return render_template('analyse.html')


@app.route("/anacapt", methods=['GET', 'POST'])
def analyse():
    if request.method == 'GET':

        url = 'http://127.0.0.1:5000/captureanalyse'

        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        r = requests.get(url, headers=headers)

        # print(r, r.json)

        output = r.json
        output = json.loads(r.text)
        print(output['output']['Message'])


        return render_template('analyse.html', output = output)



if __name__  == "__main__":
    app.run(debug=True, host='127.0.0.2')
