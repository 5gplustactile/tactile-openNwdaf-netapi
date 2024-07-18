# naas6g-openNwdaf-netapi

## Project description

The Network Data Analytics Function (NWDAF) is a 3GPP standard that provides network operators with the ability to collect, analyze, and store network data in real time. This data can be used to improve network performance, optimize resource utilization, and troubleshoot problems.

## Project status

### NWDAF Services Status

*  `Nnwdaf_AnalyticsSubscription Service`[🛠️DEVELOPING🛠️] [R17] 
*  `Nnwdaf_AnalyticsInfo Service`[🛠️DEVELOPING🛠️]  [R17]  
*  `Nnwdaf_DataManagement Service`[🛠️DEVELOPING🛠️]  [R17]  
*  `Nnwdaf_MLModelProvision Service`[🛠️DEVELOPING🛠️][R17] 
*  `Nnwdaf_MLModelInfo service`[❌TBD❌]      [R17]  
*  `Nnwdaf_RoamingAnalytics Service`[❌TBD❌]   [R18] 
*  `Nnwdaf_RoamingData Service`[❌TBD❌]       [R18] 
*  `Nnwdaf_MLModelMonitor Service`[❌TBD❌]     [R18] 
*  `Nnwdaf_MLModelTraining Service`[❌TBD❌]    [R18] 
*  `Nnwdaf_MLModelTrainingInfo Service`[❌TBD❌][R18]  

### Events Status

*  `NF_LOAD` [🛠️DEVELOPING🛠️]
*  `SLICE_LOAD_LEVEL`[🛠️DEVELOPING🛠️]

## Technologies

* Python
* Flask
* Docker
* MongoDB
* Nginx

## How to run NWDAF services in this Repository

To use Discovery's NWDAF you need to have docker installed, with this we have simplified the way to set up all the necessary NWDAF services. 
To do this you can execute:

```
cd services/

./run.sh
```

This will lift all necessary NWDAF services, including mongodb and nginx.

You can also set the host as follows:

```
./run.sh nwdaf_hostname
```

If no host is provided, it will default to **localhost**.

## How to test NWDAF APIs

Discovery NWDAF APIs can be tested using curl.

### Testing the apis using curl

To test the apis using curl we have created some example curl with the json necessary to execute them.
We have the test curls in the curl_cli.txt file, which you can see with the following command:

```
cat tests/curl/curls_cli.txt
```

This will display the commands we created for testing. To use one you would simply have to copy it and run it in the terminal from the root directory of the project. 
Example of creating analytics subscription:

```
curl -X POST -H "Content-Type: application/json" -d @./tests/curl/Events_Subscription_json/sub2.json http://localhost:8080/nnwdaf-eventssubscription/v1/subscriptions
```

To test the sending of notifications, two APIs have also been created that listen to receive the notifications. To run these api you can use the following command:

```
python utils/api_port_2222.py
```

## Important URLs
### Mongo DB Dashboard

To simplify viewing and managing mongo, we use Mongo Express in the following addresses:

```
http://0.0.0.0:8082/ (if accessed from localhost) 

or

http://<Mongo Express Host IP>:8082/ (if accessed from another host)
```
## Documents

* [Architecture enhancements for 5G System (5GS) to support network data analytics services](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3579)
*  [System; Network Data Analytics Services; Stage 3](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3355)
