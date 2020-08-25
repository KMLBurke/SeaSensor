# SeaSensor
Monitoring TBay

Design and build an ocean proof enclosure housing a microcontroller connected to sensors (temp, accelerometer, Gyro).
Enclosure to be attached to marine buoy.

# Requirements

LPWAN enabled micrrocontroller (Pycom SiPy/LoPy)

LiPo battery (high capacity)

Waterproof temperature Sensor (DS18B20)

Waterproof Accelerometer

Waterproof Gyro

Ocean proof housing allowing for exposure of antenna and temperature sensor. (3d printed).

Additional: Possible way to measure current direction and force.
3x flow meters or pressure sensors

Collaborators: Abaz Bajrami and Kevin Burke


# Intermediate Report 1:

Abaz:
I tried to connect my pycom and sipy boards to my laptop. The board could not be recognized by my laptop or pi.
Done some research on the different commands and code you can use with sipy and VSCode.

Kevin:
A Pycom SiPy was decided on as the base for the project, with a PyMakr expansion board to allow us to connect the external sensors.


![SiPy](https://user-images.githubusercontent.com/46967737/77871425-ffe42480-723b-11ea-9451-61c301d8bc15.jpg)
![PyMakr](https://user-images.githubusercontent.com/46967737/77871359-c8757800-723b-11ea-8a3e-64505e913547.jpg)

After adding some python code for the boot sequence, along with a main programme, the ID and PAC numbers of the SiPy was obtained. This data was then used to register the device with SigFox.
(see code folder)

 # Update 25/08/20

Due to Covid-19 and other complications such as lack of access to hardware, the initial design had to be rethought. 
Design and build (as much as possible) a wireless device containing a micro-controller and temperature sensor, suitable for deployment off the wifi grid, in a water rich envirenment.

 # Advancements

Modified the code in main.py to integrate with Sigfox.

Further modified this code to send data 10 times, with a 30 second delay.
![Screenshot_27](https://user-images.githubusercontent.com/46967737/91189528-70f40f00-e6ea-11ea-85b9-05f77fc355ed.png)

Successfully recieved a message on SigFox from the SiPy.
LPWAN connectivity achieved.

Attempted to create a callback to Wia, however login creditials (the API login and password generated by SigFox backend) are deemed invalid by Wia.

![Screenshot_26](https://user-images.githubusercontent.com/46967737/91184833-0096bf00-e6e5-11ea-9427-154a05ac350f.png).

Successfully created a callback to ThingSpeak. The 10, 30 second delayed data dumps previously observed on SigFox, are clearly observed in Field1.

![Screenshot_28](https://user-images.githubusercontent.com/46967737/91190491-8ae22180-e6eb-11ea-8454-e2239c97dd72.png)


Attaching a DS18B20 via the breakout headers on the Pymakr board allowed temperature to be taken. This was first achieved using a breadboard for temporary testing, followed by soldering the wires, and encasing them in heat shrink. A 3.3v, ground and data pin were used, with a pull up resistor connecting the data line to power also.

![118398475_1085932558529324_8968797473658105095_n](https://user-images.githubusercontent.com/46967737/91221227-44092180-e715-11ea-8836-0d4934abbb50.jpg)
![118356288_607666843265484_8188685056252506972_n](https://user-images.githubusercontent.com/46967737/91221234-479ca880-e715-11ea-9413-50121ad8f75b.jpg)




The send code was then modified to send this temperature data, rather than generic bytes (See code folder). The data was sucessfully seen on both sigfox and thingspeak.

![Screenshot_29](https://user-images.githubusercontent.com/46967737/91224450-05299a80-e71a-11ea-9999-31ad8d5d8795.png)
![Screenshot_30](https://user-images.githubusercontent.com/46967737/91224452-05c23100-e71a-11ea-9252-69a6762fd2d3.png)

The final assemly was then encased in an IP67 waterproof Pycom enclose.


![118316109_246672803106109_6759879579930718185_n](https://user-images.githubusercontent.com/46967737/91225288-479fa700-e71b-11ea-9dcc-a5788cbb8ef1.jpg)



# Additions required

LiPo battery for standalone power, along with a simple on/off switch. 

Waterproofing the holes through which the antenna and temperature sensor enter the enclosure.

Additional sensors such as an accelerometer or gyro to expand the usefulness of the station beyond just sea temperature. 


# YouTube Demonstration

[https://youtu.be/lzbIaL_26Rc](url)

# Website

[https://kmlburke.github.io/SeaSensor/](url)
