# GEMINI_Stratos
Project Gemini Script for Initial State

## Requirements

You will need to obtain an [Initial State]('http://www.initialstate.com') account, this can either be a free or a premium account. Within the site create a new data stream and replace the information in the line:

<code>streamer = Streamer(bucket_name="YourBucketID", bucket_key="YourBucketKey",access_key="YouAPIKey")</code>

Finally replace the line

<code>f = open('DownlinkTelemetryExample.txt')</code>

To contain the location of your output data file. For Linux this is in the form <code>'~/folder/data.txt'</code>, whereas for Windows this takes the form <code>'C:\Users\folder\data.txt'.
