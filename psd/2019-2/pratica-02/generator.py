import threading
import queue
import time
from kafka import KafkaProducer

def readfile(filename=None,pq=None):
    global stop_program
    f = open(path+filename)
    for l in f.readlines():
        words = l.split(",")
        ts,code,name,lat,lng,temp,umid = words[0], words[1], words[2], words[3], words[4], words[16], words[17]
        if (ts == "timestamp"):
            continue
        message = '{\n'+ \
                    '\t\"ts\":'+str(ts)+',\n'+ \
                    '\t\"values\": {\n' + \
                    '\t\t\"code\": \"'+str(code)+'\", '+ \
                    '\"name\": \"'+str(name.rstrip())+'\", '+ \
                    '\"lat\": '+str(lat)+', '+ \
                    '\"long\": '+str(lng)+', '+ \
                    '\"temp\": '+str(temp)+', '+ \
                    '\"umid\": '+str(umid)+'\n'+ \
                    '\t}\n' + \
                    '}'
        pq.put((ts,code,message))
        if stop_program:
            break
    f.close()

def sendToKafka(msg=""):
    global producer
    print(msg[2])
    producer.send('petro',msg[2])

def generate(pq=None):
    global stop_program
    if stop_program:
        return
    if pq.empty():
        return None
    e = pq.get()
    ts_first = e[0]
    sendToKafka(e)
    while True:
        if pq.empty():
            return None
        e = pq.get()
        ts = e[0]
        if ts <= ts_first:
            sendToKafka(e)
        else:
            pq.put(e)
            t = threading.Timer(BASETIME/SPEEDUPFACTOR,generate,args=[pq])
            t.start()
            return None

if __name__ == "__main__":    
    path="/home/rsi-psd-vm/Documents/rsi-psd-codes/psd/2019-2/pratica-02/data/"
    files = ["A301.csv","A307.csv","A309.csv","A322.csv","A328.csv","A329.csv","A341.csv","A349.csv","A350.csv","A351.csv","A357.csv","A366.csv","A370.csv"]
    pq = queue.PriorityQueue()
    BASETIME = 3600.0
    SPEEDUPFACTOR = 3000.0
    stop_program = False
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

    for fi in files:
        t = threading.Thread(target=readfile,args=(fi,pq))
        t.start()

    print("Waiting 5 seconds to populate queue...")
    t = threading.Timer(5,generate,args=[pq])
    t.start()
    print("Running...")
    try:
        while True:
            time.sleep(1)
            if pq.empty():
                break
    except (KeyboardInterrupt, SystemExit):
        stop_program = True
        print("Aborted! Stopping threads...")
    print("It's over!")
