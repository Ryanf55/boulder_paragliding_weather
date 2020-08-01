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
