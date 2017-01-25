# Analyzing Real time twitter data 

##Project: 
1. Transforming realtime twitter stream and storing them in a data storage. 
2. Parsing over the tweets and derving meaning insights from it. 
3. Searching for results based on input keywords

Analysis:

1. US states sentiments and Acitvities
Dashboard:
https://spotfire.cloud.tibco.com/spotfire/wp/render/QZGmidrJVAwGE15CfM/analysis?file=/users/anagrawa/Public/twitterDataAnalysis&waid=tcpVDzeF_UOtKK_qv2Vv7-1803055da5xPpJ&wavid=0

2. Deriving people’s sentiments for the presidential candidates
Dashboard:
https://spotfire.cloud.tibco.com/spotfire/wp/OpenAnalysis?file=84784eb5-ded0-4cb4-aeac-23e17fbc3ada

3. Results for Text search:

   

##Workflow: 
twitter->pipeline->load->analyze

1. Formatting the realtime twitter data : cleaning up data (encoding unicode text, initializing locations)
2. transform jason data into metdata format and store extracted results in aoracle database as records
3. Accessing the database to build business intelligence dashbards
4. Ability to stream real-time twitter feed and derive analysis
5. Text search control, providing valid results based on keyword search in twitter text data.
