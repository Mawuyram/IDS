import pandas as pd
import random

import sys
sys.path.append('../lib/data/GF.csv')
path = './lib/data/GF.csv'

df = pd.read_csv(path)
features = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'hot', 'logged_in', 'count', 'srv_count', 'rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']

for x in features:
    print(x, df[x].unique())

for x in features:
    print(x, df[x].agg(['min', 'max']))

def GF(protocol):
    duration = random.randint(0, 57715)
    if protocol == 'TCP, Transmission Control Protocol.':
        protocol_type = 0
    elif protocol == "UDP, User Datagram Protocol.":
        protocol_type = 1
    else: protocol_type = 2
    service = random.randint(1,69)
    flag = random.randint(0,10)
    src_bytes = random.randint(0,62825648)
    dst_bytes = random.randint(0, 1345927)
    hot = random.randint(0, 101)
    logged_in = random.randint(0, 1)
    count = random.randint(0, 511)
    srv_count = random.randint(0, 511)
    rerror_rate = random.randint(0,10)
    same_srv_rate = random.randint(0,10)
    diff_srv_rate = random.randint(0,10)
    dst_host_count = random.randint(0,255)
    dst_host_srv_count= random.randint(0,255)
    dst_host_same_srv_rate = random.randint(0,10)
    dst_host_same_src_port_rate = random.randint(0,10)
    dst_host_rerror_rate = random.randint(0,10)
    dst_host_srv_rerror_rate = random.randint(0,10)

    return [duration, protocol_type, service, flag, src_bytes, dst_bytes, hot, logged_in, count, srv_count, rerror_rate, same_srv_rate, diff_srv_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_same_src_port_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate]
