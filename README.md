# iot-mqtt-client-device-simulator
An IoT MQTT client device simulator written in Python for emulating both publication and subscription to MQTT brokers

## About
xxxxx

## Features
-
-

## Terms of Use
This tool is proprietary software. Usage, modification, and distribution of the IoT MQTT Client Device Simulator are not permitted without 
explicit written permission from the author.

## Installation
To test this IoT MQTT client device simulator, you need a local MQTT Broker. Eclipse Mosquitto is an open-source MQTT broker that implements the MQTT protocol versions 5.0, 3.1.1, and 3.1. Mosquitto is lightweight and suitable for use on all devices, from low-power single-board computers to full servers.  
Mosquitto Project Website: https://mosquitto.org/  
Mosquitto documentation: https://mosquitto.org/documentation/  

__MacOS__  
- Mosquitto can be easily installed using Homebrew. If you don't have Homebrew installed, you can get it from [brew.sh](https://brew.sh). 

- Once you have Homebrew, execute the following commands in your terminal:
```bash
brew install mosquitto
```
- After installation, you can verify if Mosquitto was installed successfully by running:
```bash
mosquitto --help
```
- To start MQTT: open terminal window (window 1) and put this to start the MQTT broker:
```bash
mosquitto
```
- To subscribe to topic using mosquitto_sub: open terminal window (window 2) and put this to subscribe to a topic:
```bash
mosquitto_sub -t ‘test/topic’ -v
```
- To publish to topic using mosquitto_sub: open terminal window (window 3) and put this to publish to a topic (you will get this data in Window 2 because you subscribe to this topic):
```bash
mosquitto_pub -t ‘test/topic’ -m "hello world"
```

- To use the tool, follow these steps:  
```
git clone https://github.com/walidamriou/iot-mqtt-client-device-simulator.git
cd iot-mqtt-client-device-simulator
```
Run the script from the command line:  
```
python main.py
```
### License
IoT MQTT Client Device Simulator © Walid Amriou  
All rights reserved. No part of this software may be reproduced, distributed, or transmitted in any form without prior 
written permission from the author.

### Disclaimer
Even if permission is granted to use, modify, or distribute this tool, the author and contributors are not liable for any damages, malfunctions, or issues that arise from its usage. Use this tool at your own risk.

The tool is provided “as is,” without any guarantees or warranties of any kind, either express or implied, including but not limited to fitness for a particular purpose or non-infringement.
