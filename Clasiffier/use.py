import sklearn.datasets
import sklearn.metrics
import sklearn.cross_validation
import sklearn.svm
import sklearn.naive_bayes
import sklearn.neighbors
import cPickle

def main():
    with open('classifier.pkl', 'rb') as fid:
        clf = cPickle.load(fid)

    with open('count_vector.pkl', 'rb') as fid:
        count_vector = cPickle.load(fid)

    newData = count_vector.transform(["bestia do gier", "nikon nowy zielony", "windows gtx nikon", "gtx komputer"])
    prediction = clf.predict(newData)
    print(prediction)



if __name__ == '__main__':
    main()