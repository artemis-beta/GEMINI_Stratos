import datetime,time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="Gemini II Stream", bucket_key="3N5NPXMQ3S37",access_key="ofB7iFb2hjFV0ly6okazknFhLWOYQKG7")


length=-1

def checkFormat(string,form):
  if(len(string) != len(form)):
    print("DATA INVALID %s INVALID LENGTH" % str(columns[0]))
    return False
  for i in range(0,len(form)):
    if(form[i] == "i"):
        if(string[i].isdigit() == False):
            print("Failed Value (%s): %s" % (i+1,string[i])) 
            return False
    elif(form[i] == "c"):
        if(string[i].isalpha() == False):
          print("Failed Value (%s): %s" % (i+1,string[i])) 
          return False
    elif(form[i] == "-"):
        if(string[i] != "+" and string[i] != "-"):
          print("Failed Value (%s): %s" % (i+1,string[i])) 
          return False
    else:
      if(string[i] != form[i]):
          print("Failed Value (%s): %s" % (i+1,string[i]))
          return False
  return True

def convertGPS(string):
    Ndeg = float(string)/1E2
    print int(Ndeg)
    Nsec = float(string)-int(Ndeg)*1E2
    print Nsec
    Nsec = Nsec/60.
    print Nsec
    return int(Ndeg)+Nsec
    
def convertTime(string):
  time_ = datetime.datetime.now()
  date_time = '%d.%d.%d %d:%d:%d' % (int(time_.day),int(time_.month),int(time_.year),int(string[1]+string[2]),int(string[3]+string[4]),int(string[5]+string[6]))
  pattern = '%d.%m.%Y %H:%M:%S'
  epoch = int(time.mktime(time.strptime(date_time, pattern)))
  return epoch

while(1 != 2):
    f = open('DownlinkTelemetryExample.txt') # Need to Find Better way than re-opening file in future!
    numLines = len(f.readlines())
    if(numLines > length):
	f.seek(0)
        length = numLines
        line = f.readlines()[-1]
        columns = line.split(',')
        if(str(columns[0]) != "G2"):
            print("DATA INVALID %s INVALID START" % str(columns[0]))
            continue
        if(checkFormat(str(columns[1]),"iiiiiiii") == False and checkFormat(str(columns[1]),"-iiiiiii") == False):
            print("DATA INVALID %s COLUMN 1"% str(columns[1]))
            continue
        if(checkFormat(str(columns[2]),"iiii") == False and checkFormat(str(columns[2]),"-iii") == False):
            print("DATA INVALID %s COLUMN 2"% str(columns[2]))
            continue
        if(checkFormat(str(columns[3]),"-iiii") == False and checkFormat(str(columns[2]),"iiiii") == False ):
            print("DATA INVALID %s COLUMN 3"% str(columns[3]))
            continue
        if(checkFormat(str(columns[4]),"iiiii") == False and checkFormat(str(columns[4]),"-iiii") == False):
            print("DATA INVALID %s COLUMN 4"% str(columns[4]))
            continue
        if(checkFormat(str(columns[5]),"iiii") == False and checkFormat(str(columns[5]),"-iii") == False):
            print("DATA INVALID %s COLUMN 5"% str(columns[5]))
            continue
        if(checkFormat(str(columns[6]),"iiii") == False and checkFormat(str(columns[6]),"-iii") == False):
            print("DATA INVALID %s COLUMN 6"% str(columns[6]))
            continue
        if(checkFormat(str(columns[7]),"$iiiiii.ii") == False):
            print("DATA INVALID %s COLUMN 7"% str(columns[7]))
            continue
        if(checkFormat(str(columns[8]),"iiii.iiiii") == False and checkFormat(str(columns[8]),"-iii.iiiii") == False):
            print("DATA INVALID %s COLUMN 8"% str(columns[8]))
            continue
        if(checkFormat(str(columns[9]),"c") == False):
            print("DATA INVALID %s COLUMN 9"% str(columns[9]))
            continue
        if(checkFormat(str(columns[10]),"iiiii.iiiii") == False and checkFormat(str(columns[10]),"-iiii.iiiii") == False):
            print("DATA INVALID %s COLUMN 10"% str(columns[10]))
            continue
        if(checkFormat(str(columns[11]),"c") == False):
            print("DATA INVALID %s COLUMN 11"% str(columns[11]))
            continue
        print("Data Line Read Successfully...Exporting Data")
        epoch = convertTime(columns[7])
        streamer.log("GPS Location",[convertGPS(columns[8]),-1*convertGPS(columns[10])],epoch)
        print("GPS Location: %s,%s"%(convertGPS(columns[8]),-1*convertGPS(columns[10])))
        streamer.log("Wind Speed/Hz",int(columns[2]),epoch)
        print("Wind Speed/Hz: %s"%columns[2])
        streamer.log("Magnetometer",int(columns[3]),epoch)
        print("Magnetometer: %s"% columns[3])
        streamer.log("Accelerometer",int(columns[4]),epoch)
        print("Accelerometer: %s"%columns[4])
        streamer.log("Internal Temperature/Celsius",int(columns[5]),epoch)
        print("Internal Temperature/Celsius: %s"%columns[5])
        streamer.log("Radiation Level/cpm",int(columns[6])*4,epoch)
        print("Radiation Level: %d"% int(int(columns[6])*4))
    length = numLines
    f.close()
    time.sleep(15)	
