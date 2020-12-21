# Smart Parking: node
## Brief summary of the architecture
The smart parking architecture comprehends **nodes**, **effectors** and a **brain**. In addition to them, we have **devices**, that represent users. The **nodes** allow occupancy detection, whereas **effectors** are the components that provide feedback to the users. The **brain** is centralized and its main contribution is the activation of the effectors wrt the position of a device, and wrt the available parking slots.

Currently, we don't have specifics on whether effectors and devices may be actually different, so please consider them as different entities that may relate to the same component (e.g.: smartphone).

This code refers to the **nodes**. It is written in Python and it has been executed on a Raspberry with Raspbian OS; despite that, it should easily work on most of devices.

## Downloading and building
To download and build this repository, you should simply clone the repo and run ```pip install -r requirements.txt```. A keys directory will follow, containing certificates in case MQTT is encrypted. The node will communicate with MQTT as a **node** client.

## Used software: tools and libraries
We use [paho-mqtt](https://pypi.org/project/paho-mqtt/) to connect the MQTT client, jsonpickle to serialize Python objects.

## Protocol
- **parking/node/config**: node communicates to brain the need of configuration. This is required as each node, when started, is not aware of its configuration. Thus it asks the park to which it refers and the slots that were assigned to him (see parking structure [here](https://github.com/filipkrasniqi/smartparking-brain/blob/master/README.md)). 
- **parking/node/occupancy**: a configured node communicates to brain whether the slots it is controlling are occupied. The payload is an instance of the [OccupancyMessage](https://github.com/filipkrasniqi/smartparking-node/blob/29975f48ae64df07f46675502b201413a53f45e6/mqtt/messages/node.py#L10) class.
- **parking/brain/config**: brain communicates to node its configuration.

## Execution
One should run the [main.py](https://github.com/filipkrasniqi/smartparking-node/blob/29975f48ae64df07f46675502b201413a53f45e6/main.py). This code will run the MQTTPublisher thread, that initializes MQTT stuff (connection, subscribing to topics) and starts the [config timer](https://github.com/filipkrasniqi/smartparking-node/blob/29975f48ae64df07f46675502b201413a53f45e6/mqtt/timer/config_timer.py). Once node is correctly configured, the [brain timer](https://github.com/filipkrasniqi/smartparking-node/blob/29975f48ae64df07f46675502b201413a53f45e6/mqtt/timer/brain_timer.py) is executed.

## Occupancy
Current implementation is dummy. For each slot, we randomly draw true or false to set the slot as occupied or not.

## Short term TODOs
- adding certificate for MQTT encryption
