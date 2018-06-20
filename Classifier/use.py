import sklearn.datasets
import sklearn.metrics
import sklearn.cross_validation
import sklearn.svm
import sklearn.naive_bayes
import sklearn.neighbors
import cPickle

from flask import Flask, render_template, request

def main(url):
    print(url)
    with open('classifier.pkl', 'rb') as fid:
        clf = cPickle.load(fid)

    with open('count_vector.pkl', 'rb') as fid:
        count_vector = cPickle.load(fid)

    newData = count_vector.transform(["bestia do gier", "nikon nowy zielony", "windows gtx nikon", "gtx komputer"])
    prediction = clf.predict(newData)
    print(prediction)

app = Flask(__name__)


@app.route('/')
def output():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['username']
        # print(result)
        main(result)
        # result = json.dumps(result.text, sort_keys=True, indent=4, separators=(',', ': '))
        return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
