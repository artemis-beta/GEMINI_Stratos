import datetime,time
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="Gemini II Stream Test", bucket_key="Testing",access_key="F36bpJ1QIdOxsVhZNvqiwnSIYDV9Utyv")

out_file = open('C:\Users\gxk928\dl-fldigi.files\GEMINI_%s_data.bkup' % time.time(),'w')

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
  Epoch = int(time.mktime(time.strptime(date_time, pattern)))
  return Epoch

while(1 != 2):
    f = open('C:\Users\gxk928\dl-fldigi.files\dl-fldigi20160423.log')
    numLines = len(f.readlines())
    if(numLines > length):
	f.seek(0)
        length = numLines
        line = f.readlines()[-2]
        out_file.write(line)
        columns = line.split(',')
        if(len(columns) >= 8):
            if(checkFormat(str(columns[7]),"$iiiiii.ii") == False):
                print("DATA INVALID %s COLUMN 7"% str(columns[7]))
                
            else:
                Epoch = convertTime(columns[7])
        if(len(columns) >= 2):
            if(checkFormat(str(columns[1]),"iiiiiiii") == False and checkFormat(str(columns[1]),"-iiiiiii") == False):
                print("DATA INVALID %s COLUMN 1"% str(columns[1]))
        if(len(columns) >= 3):       
            if(checkFormat(str(columns[2]),"iiii") == False and checkFormat(str(columns[2]),"-iii") == False):
                print("DATA INVALID %s COLUMN 2"% str(columns[2]))
                
            else:
                streamer.log_object(int(columns[2]),key_prefix="Wind Speed/Hz",epoch=Epoch)
                print("Wind Speed/Hz: %s"%columns[2])
        if(len(columns) >= 4):   
            if(checkFormat(str(columns[3]),"-iiii") == False and checkFormat(str(columns[2]),"iiiii") == False ):
                print("DATA INVALID %s COLUMN 3"% str(columns[3]))
                
            else:
                streamer.log_object(int(columns[3]),key_prefix="Magnetometer",epoch=Epoch)
                print("Magnetometer: %s"% columns[3])
        if(len(columns) >= 5):  
            if(checkFormat(str(columns[4]),"iiiii") == False and checkFormat(str(columns[4]),"-iiii") == False):
                print("DATA INVALID %s COLUMN 4"% str(columns[4]))
                
            else:
                streamer.log_object(int(columns[4]),key_prefix="Accelerometer",epoch=Epoch)
                print("Accelerometer: %s"%columns[4])
        if(len(columns) >= 6):   
            if(checkFormat(str(columns[5]),"iiii") == False and checkFormat(str(columns[5]),"-iii") == False):
                print("DATA INVALID %s COLUMN 5"% str(columns[5]))
                
            else:
                streamer.log_object(int(columns[5]),key_prefix="Internal Temperature/Celsius",epoch=Epoch)
                print("Internal Temperature/Celsius: %s"%columns[5])
        if(len(columns) >= 7):    
            if(checkFormat(str(columns[6]),"iiii") == False and checkFormat(str(columns[6]),"-iii") == False):
                print("DATA INVALID %s COLUMN 6"% str(columns[6]))
                
            else:
                streamer.log_object(int(columns[6])*4,key_prefix="Radiation Level/cpm",epoch=Epoch)
                print("Radiation Level: %d"% int(int(columns[6])*4))
        if(len(columns) >= 11):     
	        GPS_SUCCESS = True
	        if(checkFormat(str(columns[8]),"iiii.iiiii") == False and checkFormat(str(columns[8]),"-iii.iiiii") == False):
                    print("DATA INVALID %s COLUMN 8"% str(columns[8]))
                    GPS_SUCCESS =False
                if(checkFormat(str(columns[9]),"c") == False):
                    print("DATA INVALID %s COLUMN 9"% str(columns[9]))
                    
                if(checkFormat(str(columns[10]),"iiiii.iiiii") == False and checkFormat(str(columns[10]),"-iiii.iiiii") == False):
                    print("DATA INVALID %s COLUMN 10"% str(columns[10]))
                    GPS_SUCCESS = False
                if(checkFormat(str(columns[11]),"c") == False):
                    print("DATA INVALID %s COLUMN 11"% str(columns[11]))
                if(GPS_SUCCESS == True):    
                    streamer.log_object([convertGPS(columns[8]),-1*convertGPS(columns[10])],key_prefix="GPS Location",epoch=Epoch)
	            print("GPS Location: %s,%s"%(convertGPS(columns[8]),-1*convertGPS(columns[10])))
        
    length = numLines
    streamer.flush()
    I = raw_input(" ")
    if not I:
        print("Closing Down...")
        streamer.close()
        f.close()
        out_file.close()
        break
    f.close()
    time.sleep(35)	
