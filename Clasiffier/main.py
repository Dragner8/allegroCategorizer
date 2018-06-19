
import sklearn.datasets
import sklearn.metrics
import sklearn.cross_validation
import sklearn.svm
import sklearn.naive_bayes
import sklearn.neighbors
import cPickle

from termcolor import colored
import sys



def main():



    dir_path = 'dataset'



    # load data
    print colored('Loading files into memory', 'green', attrs=['bold'])
    files = sklearn.datasets.load_files(dir_path)

    #print(files)
    #print(files.target)

    print colored('Calculating BOW', 'green', attrs=['bold'])


    # create bags of words
    count_vector = sklearn.feature_extraction.text.CountVectorizer()
    word_counts = count_vector.fit_transform(files.data)
    print count_vector.vocabulary_


    #print (word_counts.toarray())
    #print (word_counts)

    # create classifier
    clf = sklearn.svm.LinearSVC()
    # clf = sklearn.naive_bayes.MultinomialNB()

    # test the classifier
    print '\n\n'
    print colored('Train and test clasiffier', 'magenta', attrs=['bold'])
    train_test_classifier(word_counts, files.target, clf, test_size=0.2, y_names=files.target_names)

    newData=count_vector.transform(["bestia do gier","nikon nowy zielony","windows gtx nikon", "gtx komputer"])
    prediction= clf.predict(newData)
    print(prediction)

    # save the classifier
    with open('classifier.pkl', 'wb') as fid:
        cPickle.dump(clf, fid)
    with open('count_vector.pkl', 'wb') as fid:
        cPickle.dump(count_vector, fid)

def train_test_classifier(X, y, clf, test_size, y_names):
    # train-test split
    print 'test size is: %2.0f%%' % (test_size * 100)
    X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X, y, test_size=test_size)

    clf.fit(X_train, y_train)
    y_predicted = clf.predict(X_test)


    print colored('Classification report:', 'magenta', attrs=['bold'])
    print sklearn.metrics.classification_report(y_test, y_predicted, target_names=y_names)
    print colored('Confusion Matrix:', 'magenta', attrs=['bold'])
    print sklearn.metrics.confusion_matrix(y_test, y_predicted)



if __name__ == '__main__':
    main()
