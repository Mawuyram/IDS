from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np


class RFC(object):
    def __init__(self):
        self.le = LabelEncoder()
        self.clf = RandomForestClassifier()

    def encode_clean(self, data):
        obj_df = data.select_dtypes(include=['object']).copy()
        #Find and Replace

        cleanup_nums = {
                        "protocol_type":{'tcp':0,'udp':1, 'icmp':2},
                        "service": {'aol':0, 'auth':1, 'bgp':2, 'courier':3, 'csnet_ns':4, 'ctf':5, 'daytime':6, 'discard':7, 'domain':8, 'domain_u':9, 'echo':10, 'eco_i':11, 'ecr_i':12, 'efs':13, 'exec':14, 'finger':15, 'ftp':16, 'ftp_data':17, 'gopher':18, 'harvest':19, 'hostnames':20, 'http':21, 'http_2784':22, 'http_443':23, 'http_8001':24, 'imap4':25, 'IRC':26, 'iso_tsap':27, 'klogin':28, 'kshell':29, 'ldap':30, 'link':31, 'login':32, 'mtp':33, 'name':34, 'netbios_dgm':35, 'netbios_ns':36, 'netbios_ssn':37, 'netstat':38, 'nnsp':39, 'nntp':40, 'ntp_u':41, 'other':42, 'pm_dump':43, 'pop_2':44, 'pop_3':45, 'printer':46, 'private':47, 'red_i':48, 'remote_job':49, 'rje':50, 'shell':51, 'smtp':52, 'sql_net':53, 'ssh':54, 'sunrpc':55, 'supdup':56, 'systat':57, 'telnet':58, 'tftp_u':59, 'tim_i':60, 'time':61, 'urh_i':62, 'urp_i':63, 'uucp':64, 'uucp_path':65, 'vmnet':66, 'whois':67, 'X11':68, 'Z39_50':69},
                        "flag": {'OTH': 0, 'REJ': 1, 'RSTO':2, 'RSTOS0':3, 'RSTR':4, 'S0':5, 'S1':6, 'S2':7, 'S3':8, 'SF':9, 'SH':10},
                        "class": {'normal':0, 'anomaly':1}

                        }

        obj_df.replace(cleanup_nums, inplace=True)

        #Replacing Columns
        data['protocol_type'] = obj_df['protocol_type']
        data['service'] = obj_df['service']
        data['flag'] = obj_df['flag']
        data['class'] = obj_df['class']

        #Discretizing the data

        obj_df = data.select_dtypes(include=['float64']).copy()

        obj_df['serror_rate'] = np.array(np.round((obj_df['serror_rate'] * 10)),
                   dtype='int')

        obj_df['srv_serror_rate'] = np.array(np.round((obj_df['srv_serror_rate'] * 10)),
                           dtype='int')

        obj_df['rerror_rate'] = np.array(np.round((obj_df['rerror_rate'] * 10)),
                           dtype='int')

        obj_df['srv_rerror_rate'] = np.array(np.round((obj_df['srv_rerror_rate'] * 10)),
                           dtype='int')

        obj_df['same_srv_rate'] = np.array(np.round((obj_df['same_srv_rate'] * 10)),
                           dtype='int')

        obj_df['diff_srv_rate'] = np.array(np.round((obj_df['diff_srv_rate'] * 10)),
                           dtype='int')

        obj_df['srv_diff_host_rate'] = np.array(np.round((obj_df['srv_diff_host_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_same_srv_rate'] = np.array(np.round((obj_df['dst_host_same_srv_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_diff_srv_rate'] = np.array(np.round((obj_df['dst_host_diff_srv_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_same_src_port_rate'] = np.array(np.round((obj_df['dst_host_same_src_port_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_srv_diff_host_rate'] = np.array(np.round((obj_df['dst_host_srv_diff_host_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_serror_rate'] = np.array(np.round((obj_df['dst_host_serror_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_srv_serror_rate'] = np.array(np.round((obj_df['dst_host_srv_serror_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_srv_serror_rate'] = np.array(np.round((obj_df['dst_host_srv_serror_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_rerror_rate'] = np.array(np.round((obj_df['dst_host_rerror_rate'] * 10)),
                           dtype='int')

        obj_df['dst_host_srv_rerror_rate'] = np.array(np.round((obj_df['dst_host_srv_rerror_rate'] * 10)),
                           dtype='int')

        #Replacing Columns
        data['serror_rate'] = obj_df['serror_rate']
        data['srv_serror_rate'] = obj_df['srv_serror_rate']

        data['rerror_rate'] = obj_df['rerror_rate']
        data['srv_rerror_rate']  = obj_df['srv_rerror_rate']

        data['same_srv_rate'] = obj_df['same_srv_rate']

        data['diff_srv_rate'] = obj_df['diff_srv_rate']

        data['srv_diff_host_rate']  = obj_df['srv_diff_host_rate']

        data['dst_host_same_srv_rate']  = obj_df['dst_host_same_srv_rate']

        data['dst_host_diff_srv_rate']  = obj_df['dst_host_diff_srv_rate']

        data['dst_host_same_src_port_rate']  = obj_df['dst_host_same_src_port_rate']

        data['dst_host_srv_diff_host_rate']  = obj_df['dst_host_srv_diff_host_rate']

        data['dst_host_serror_rate']  = obj_df['dst_host_serror_rate']

        data['dst_host_srv_serror_rate']  = obj_df['dst_host_srv_serror_rate']

        data['dst_host_srv_serror_rate'] = obj_df['dst_host_srv_serror_rate']

        data['dst_host_rerror_rate']  = obj_df['dst_host_rerror_rate']

        data['dst_host_srv_rerror_rate']  = obj_df['dst_host_srv_rerror_rate']

        return data

    def train(self,X_train, y_train):
        print("Training Model with RandomForestClassifier...")
        self.clf.fit(X_train, y_train)
        return "Model Trained Successfully"

    def predict(self, X_test):
        print("Running Prediction...")
        prediction = self.clf.predict(X_test)
        print("Prediction Complete!")
        return prediction

