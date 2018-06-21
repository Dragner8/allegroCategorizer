import sklearn.datasets
import sklearn.metrics
import sklearn.cross_validation
import sklearn.svm
import sklearn.naive_bayes
import sklearn.neighbors
import cPickle

from flask import Flask, render_template, request

def main(url):
    listOfItems = url.split("-")
    if 'allegro' not in listOfItems[0]:
        return -1
    del listOfItems[-1]
    del listOfItems[0]
    items = " ".join(listOfItems)

    with open('classifier.pkl', 'rb') as fid:
        clf = cPickle.load(fid)

    with open('count_vector.pkl', 'rb') as fid:
        count_vector = cPickle.load(fid)

    # newData = count_vector.transform(["bestia do gier", "nikon nowy zielony", "windows gtx nikon", "gtx komputer"])
    newData = count_vector.transform([items])
    prediction = clf.predict(newData)
    return prediction

app = Flask(__name__)


@app.route('/')
def output():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['username']
        svmResult = main(result)
        message = 'This is not a valid Allegro web auction.'
        if svmResult == 1:
            message = 'This is a computer.'
        if svmResult == 0:
            message = 'This is NOT a computer.'
        return render_template("index.html", result=message)


if __name__ == '__main__':
    app.run()
