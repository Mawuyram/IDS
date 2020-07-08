from model_pipeline.RFC import RFC
from model_pipeline.SVM import SVM
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn import metrics

import pickle


class PacketAnalyzerIDS(object):
    def __init__(self):
        self.version = 0.0
        self.clf_RFC = RFC()
        self.clf_SVM = SVM()



    def RFC_model_pipeline(self,data):
        X = self.clf_RFC.encode_clean(data)
        features = self.feature_selection(X)
        X[features].to_csv('../lib/data/GF.csv', index = False)
        features.append('class')
        X = self.train_test_split(X[features])
        self.clf_RFC.train(X[0],X[1])
        prediction = self.clf_RFC.predict(X[2])
        self.performance_metrics(X[3],prediction, "RandomForestClassifier")
        self.pickleClassifier(self.clf_RFC, "RandomForestClassifier")




    def SVM_model_pipeline(self, data):
        X = self.clf_SVM.encode_clean(data)
        features = self.feature_selection(X)
        features.append('class')
        X = self.train_test_split(X[features])
        self.clf_SVM.train(X[0],X[1])
        prediction = self.clf_SVM.predict(X[2])
        self.performance_metrics(X[3], prediction,"SupportVectorMachine(SVM)")
        self.pickleClassifier(self.clf_SVM, "SupportVectorMachine(SVM)")


    def feature_selection(self, data):
        # spliting data table into data X and class label y
        X = data.iloc[:,0:41].values
        Y = data.iloc[:,41].values

        feat_labels = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
       'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
       'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
       'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
       'num_access_files', 'num_outbound_cmds', 'is_host_login',
       'is_guest_login', 'count', 'srv_count', 'serror_rate',
       'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
       'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
       'dst_host_srv_count', 'dst_host_same_srv_rate',
       'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
       'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
       'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
       'dst_host_srv_rerror_rate']

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=0)

        # Create a random forest classifier
        clf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)

        # Train the classifier
        clf.fit(X_train, y_train)

        # Print the name and gini importance of each feature
        for feature in zip(feat_labels, clf.feature_importances_):
            print(feature)

        # Create a selector object that will use the random forest classifier to identify
        # features that have an importance of more than 0.012
        sfm = SelectFromModel(clf, threshold=0.012)

        # Train the selector
        sfm.fit(X_train, y_train)


        # Print the names of the most important features
        features = []
        for feature_list_index in sfm.get_support(indices=True):
            features.append(feat_labels[feature_list_index])
            print(feat_labels[feature_list_index])

        return features




    def train_test_split(self,data):
        X = data.iloc[:,0:19].values
        y = data.iloc[:,19].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=10)
        return [X_train, y_train, X_test, y_test]



    def performance_metrics(self, y_test, y_pred, clf_name):
        print("-----------Performance Metric for {} Model-------------".format(clf_name))
        print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
        print("Precision: ", metrics.precision_score(y_test, y_pred))
        print("Recall: ", metrics.recall_score(y_pred, y_test))
        print("Confusion Matrix: ", metrics.confusion_matrix(y_test, y_pred))


    def pickleClassifier(self, clf, model_name):
        path = '../lib/models/{}.pkl'.format(model_name)

        with open(path,'wb') as f:
            pickle.dump(clf, f)
            print("Pickled Classifier at {}".format(path))



