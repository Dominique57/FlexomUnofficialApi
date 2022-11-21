# FlexomUnofficialApi

Python project to interact with the Flexom services (domotic application). 

## What is it

Create clients to interact with flexom services to handles lights, shutters and thermostats.

The API is undocumented thus I patched the android application to allow inspecting the application's
network traffic, create DTO models and simulate endpoint headers and data communication.

Thus you can create even more complex domotic scenarios such as regular web push notification to set
the temperature the morning and evening to reduce your energy consumption.

TODO: make a video of the temperature setting example

## Setup

### Tools

To be able to compile and run the program you need :
- [Python 3.8+](https://python.org/) (language)
- [Pip](https://pypi.org/project/pip/) (python dependency manager)

### Installation

Install python requirements in a virtual environment :
```bash
42sh$ python -m venv env
42sh$ source env/bin/activate
(env) 42sh$ pip install -r requirements.txt
```

## Usage

You can check the abilities of the clients in their respective files in the clients module !

Here is an example where we set the temperature on a connected thermostat :

```python
# Create a client
user_client = UserClient.build_client(USER_EMAIL, USER_PASS)
if not user_client:
    raise Exception("Failed to create client")

# Get a building information entity
binfos = user_client.get_buildings_info()
binfo = binfos.__root__[0]

# Create a building client
building_client = BuildingClient.build_client(user_client, binfo)

# Fetch a iot device with "somfy" in the name
iots = building_client.get_iots()
iot_tmp: Optional[Iot] = search_item(iots.__root__, lambda iot: "somfy" in iot.name.lower())
if iot_tmp is None:
    raise Exception("Failed to find temperature iot")

# Get actuator of the temperature iot
iot_actuators = building_client.get_actuators(iot_tmp.id)
if len(iot_actuators.__root__) < 1:
    raise Exception("Iot device does not have actuators")
iot_actuator = iot_actuators.__root__[0]

# Set temperature of iot temperature device using actuator
iot_tmp_value = 17
building_client.put_actuator_state(iot_tmp.id, iot_actuator.actuatorId, iot_tmp_value)
```
### Architecture

The application is layered in multiple modules :
- models : DTO object to mirror the api
- requests : low-level functions that create appropriate request headers and data
- clients : higher level of abstraction to interact with smart re-authentication on-the-fly

## Licensing
No license supplied

## Known issues
- TODO

## Contributions
- Dominique MICHEL <dominique.michel@epita.fr>
