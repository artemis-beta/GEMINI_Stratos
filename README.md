# GEMINI_Stratos
Project Gemini Script for Initial State

## Requirements

You will need to obtain an Initial State account, this can either be a free account or a prerequisite one. Within the site create a new data stream and replace the information in the line:


streamer = Streamer(bucket_name="YourBucketID", bucket_key="YourBucketKey",access_key="YouAPIKey")

Finally replace the line


f = open('DownlinkTelemetryExample.txt')


To contain the location of your output data file. For Linux this is in the form <code>'~/folder/data.txt'</code>, whereas for Windows this takes the form <code>'C:\Users\folder\data.txt'.
