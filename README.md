# boulder_paragliding_weather

## Dependencies

* [pySmartWeatherUDP](https://github.com/briis/pysmartweatherudp)
    * `$ python3 -m pip install pysmartweatherudp`

## Datasets

* If needed to develop, see the enclosed datasets from wireshark. A program such as [tcpreplay] can play back the logs for processing

* To capture raw data with tcpdump, use the following `$ sudo tcpdump -Al -nei wlx9848273fbac6 port 50222`
  * the `-l` and `-A` make the packet data print in ascii and greppable

## Pushing data to EC2

* EC2 Instance
  * Dashboard: https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:sort=monitoring
  * `$ ssh -i ~/Development/certs/ryan5410_pair.pem ubuntu@ec2-3-21-114-123.us-east-2.compute.amazonaws.com`

* Sending UDP traffic with iperf:
  * https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/

  * SSH onto EC2 and monitor: `sudo tcpdump -nei eth0 port 5001 -Al`
  * Send data with iperf from Boulder host: ` iperf -c 3.21.114.123 -u -b 5g`
  * Send data with my discovery script: `python discovery.py comms_tester -u -iu 3.21.114.123 -m "hi"`
  
 ## Decreasing data usage in upload
 
 Goal: Decrease amount of network data usage during normal operation of the weather station
 
### Methods

* Decrease frequency of upload -> linear effect
* Decrease amount of information per packet 
* Decrease packet size moving from JSON to something more efficient

Certain data is more useful often, such as current wind speed than something that changes less often. The proposed packet structure and frequencies are shown below:

* Wind Packet = every 1 minute
  * uint8 current wind velocity
  * uint8 wind direction (value of 180 = wind direction of 360 degrees, so 2 degree resolution
  * uint8 gust velocity
  * uint8 lull velocity
* Temperature Packet = every 30 minutes
  * uint8 temperature
* Rain Packet = push packet on start of rain
  * uint32 = time of start
* Lightning Packet = push packet on first strike and every 10m while strikes exist
  * uint32 = time of last strike
  * uint8 = distance of strike
  
 * The remaining data could be query only, which may get queried for remote debugging. Because of the low frequency of data, maybe it's ok to send as JSON. 
  
  
