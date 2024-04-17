from paho.mqtt import client as mqtt  # Import the MQTT client library
import time  # Import the time module for sleep function
# import json

# MQTT broker details
broker_address = "localhost"  # Define the MQTT broker address
broker_port = 1883  # Define the MQTT broker port

# Callback function called when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:  # If the connection result code is 0 (success)
        print("Connected to MQTT broker")  # Print a success message
        client.subscribe("commands")  # Subscribe to the "commands" topic
        client.publish("commands", "Hello, world!")  # Publish a message to the "commands" topic
    else:  # If the connection result code is not 0 (failure)
        print("Failed to connect to MQTT broker with result code " + str(rc))  # Print an error message

# Callback function called when a message is received on a subscribed topic
def on_message(client, userdata, msg):
    print("Received message on topic " + msg.topic + ": " + msg.payload.decode())  # Print the received message
    handle_command(msg.payload.decode())  # Call the handle_command function with the received message as argument

# Callback function called when a message is successfully published
def on_publish(client, userdata, mid):
    print("Message published.")  # Print a message indicating that the message was published successfully

# Command handler function
def handle_command(command):
    if command == "reset":  # If the received command is "reset"
        print("Resetting device...")  # Print a message indicating that the device is resetting
        # Code to reset the device goes here
    elif command == "update":  # If the received command is "update"
        print("Updating device...")  # Print a message indicating that the device is updating
        # Code to update the device goes here
    else:  # If the received command is neither "reset" nor "update"
        print("Unknown command:", command)  # Print a message indicating that the command is unknown

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 
                     client_id="", 
                     clean_session=True, 
                     userdata=None, 
                     protocol=4, 
                     transport="tcp", 
                     reconnect_on_failure=True)

# Assign callback functions to corresponding MQTT events
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Connect to the MQTT broker
try:
    client.connect(broker_address, broker_port, 60)  # Attempt to connect to the broker
except ConnectionRefusedError:  # If connection is refused
    print("Connection refused: Unable to connect to MQTT broker")  # Print an error message

# Start the MQTT client network loop
client.loop_start()

# Wait for messages for 5 seconds
time.sleep(5)

# Stop the MQTT client network loop and disconnect from the broker
client.loop_stop()
client.disconnect()
exit()