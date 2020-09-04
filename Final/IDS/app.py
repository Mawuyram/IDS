from flask import Flask, jsonify
from flask_restful import Api, reqparse, Resource
from Packet_Capture import CApacket, GenerateFeatures
from model_pipeline.model import PacketAnalyzerIDS
import numpy as np
from syslog import SyslogUDPHandler


import pickle

app = Flask(__name__)
api = Api(app)

model = PacketAnalyzerIDS().clf_RFC

path = './lib/models/RandomForestClassifier.pkl'

with open(path, 'rb') as f:
    model.clf = pickle.load(f)

class CaptureAnalyse(Resource):

    def get(self):
        output = CApacket.main()
        print(output)

        # GenerateFeatures.path = './lib/data/GF.csv'
        y = GenerateFeatures.GF(output['Protocol'])
        print(y)
        input_variable = [y]

        prediction = np.array2string(model.predict(input_variable))[1]
        if prediction == "0":
            prediction = "Normal Traffic"
        else: prediction = "Anomalous Traffic !!!"

        return jsonify({"output":  output, 'p':{"prediction": prediction}})
    log =SyslogUDPHandler

api.add_resource(CaptureAnalyse,'/captureanalyse')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
