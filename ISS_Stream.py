import time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="Gemini II Stream", bucket_key="GEMINI2_KEY001",access_key="QEALAzlStgU4FGlY2OH826wVpKeTqGaO")

f = open('C:\Users\gxk928\dl-fldigi.files\Testdata.log')
length=-1

while(1 != 2):
    lineList = f.readlines()
    if(length < len(lineList)):
        f.seek(0)
        line = f.readlines()[-1]
        columns = line.split(' : ')
        streamer.log("Time",columns[1])
        if(columns[0] == "WSS.txt"):
            streamer.log("Experiment","WSS")
            streamer.log("WSS Container 1",columns[2])
            streamer.log("WSS Container 2",columns[3])
        elif(columns[0] == "Matrix.txt"):
            streamer.log("Experiment","MATRIX")
            streamer.log("Matrix Container 1",columns[2])
            streamer.log("Matrix Container 2",columns[3])
            streamer.log("Matrix Container 2",columns[4])
            streamer.log("Matrix Container 2",columns[5])
            streamer.log("Matrix Container 2",columns[6])
            streamer.log("Matrix Container 2",columns[7])
            streamer.log("Matrix Container 2",columns[8])
            streamer.log("Matrix Container 2",columns[9])
            streamer.log("Matrix Container 2",columns[10])
            streamer.log("Matrix Container 2",columns[11])
        elif(columns[0] == "Rads.txt"):
            streamer.log("Experiment","RADS")
            streamer.log("RADS Counts per Minute",columns[2])
            streamer.log("RADS Counts per Quart",columns[3])
    length = len(lineList)
    f.seek(0)


    '''
while(1 != 2):
    lineList = f.readlines()
    if(length < len(lineList)):
        f.seek(0)
        line = f.readlines()[-1]
        columns = line.split(' : ')
       # streamer.log("Time",columns[1])
        print columns[1]
        if(columns[0] == "Matrix.txt"):
            #streamer.log("Experiment","WSS")
            print columns[2]
            print columns[3]
        elif(columns[0] == "Matrix.txt"):
            streamer.log("Experiment","MATRIX")
            streamer.log("Matrix Container 1",columns[2])
            streamer.log("Matrix Container 2",columns[3])
            streamer.log("Matrix Container 2",columns[4])
            streamer.log("Matrix Container 2",columns[5])
            streamer.log("Matrix Container 2",columns[6])
            streamer.log("Matrix Container 2",columns[7])
            streamer.log("Matrix Container 2",columns[8])
            streamer.log("Matrix Container 2",columns[9])
            streamer.log("Matrix Container 2",columns[10])
            streamer.log("Matrix Container 2",columns[11])
        elif(columns[0] == "Rads.txt"):
            streamer.log("Experiment","RADS")
            streamer.log("RADS Counts per Minute",columns[2])
            streamer.log("RADS Counts per Quart",columns[3])
    length = len(lineList)
    f.seek(0)
    
'''
