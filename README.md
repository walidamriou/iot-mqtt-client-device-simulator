# IoT-MQTT-Client-Device-Simulator
An IoT MQTT client device simulator written in Python for emulating both publication and subscription to MQTT brokers

# Setup Local MQTT Broker for Testing

To test this IoT MQTT client device simulator, you need a local MQTT Broker. Eclipse Mosquitto is an open-source MQTT broker that implements the MQTT protocol versions 5.0, 3.1.1, and 3.1. Mosquitto is lightweight and suitable for use on all devices, from low-power single-board computers to full servers.

* Mosquitto Project Website: https://mosquitto.org/
* Mosquitto documentation: https://mosquitto.org/documentation/

## Installation on MacOS

Mosquitto can be easily installed using Homebrew. If you don't have Homebrew installed, you can get it from [brew.sh](https://brew.sh). 

1. Once you have Homebrew, execute the following commands in your terminal:
```bash
brew install mosquitto
```
2. After installation, you can verify if Mosquitto was installed successfully by running:
```bash
mosquitto --help
```
## Installation on Windows

To install Eclipse Mosquitto on Windows: later

## Installation on Linux

Later

# Testing Mosquitto Local MQTT Broker (MacOS)
1. Start MQTT: open terminal window (window 1) and put this to start the MQTT broker:
```bash
mosquitto
```
2. Subscribe to topic using mosquitto_sub: open terminal window (window 2) and put this to subscribe to a topic:
```bash
mosquitto_sub -t ‘test/topic’ -v
```
3. Publish to topic using mosquitto_sub: open terminal window (window 3) and put this to publish to a topic (you will get this data in Window 2 because you subscribe to this topic):
```bash
mosquitto_pub -t ‘test/topic’ -m "hello worls"
```

### Copyright CC 2024 Walid Amriou
