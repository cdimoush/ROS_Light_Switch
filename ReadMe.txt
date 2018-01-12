ros_light_switch

Launch Commands
---------------------------------------------------------------------
roslaunch arduino_service arduino_light.launch port:= [port]
	-If the port is not given it will default to /dev/ttyACM0

or 

python scripts/arduino_python_launch.py
	-This python script determines if an are aduino is attached via usb connection. If an arduino is detected it will use a subprocess to run the arduino_light.launch file and give the launch file the correct port


----------------------------------------------------------------------

This package communicates with an arduino to control...
- a mechanical relay

The arduino_server.py script has "light_on" and "lights_off"
services to turn on and off the mechanical relay.

To communicate with the arduino the services publish empty
messages to their repective topics. The arduino is subscribed
to these topics and the messages activates the respective function. The arduino code exists on the arduino but I included it in the library.

Launch files are used to run the package. In addition to the python
scripts the rosserial_library is used to communicate with the
 arduino. The launch file defaults to the arduino being on the 
/dev/ttyACM0 port. But the arduino_python_launch.py file can be run to find the port and launch

light launch file does not include the
servo service.

