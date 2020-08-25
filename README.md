# SeaSensor
Monitoring TBay

Design and build an ocean proof enclosure housing a microcontroller connected to sensors (temp, accelerometer, Gyro).
Enclosure to be attached to marine buoy.

Requirements

LPWAN enabled micrrocontroller (Pycom SiPy/LoPy)

LiPo battery (high capacity)

Waterproof temperature Sensor (DS18B20)

Waterproof Accelerometer

Waterproof Gyro

Ocean proof housing allowing for exposure of antenna and temperature sensor. (3d printed).

Additional: Possible way to measure current direction and force.
3x flow meters or pressure sensors

Collaborators: Abaz Bajrami and Kevin Burke


Intermediate Report 1:

Abaz:
I tried to connect my pycom and sipy boards to my laptop. The board could not be recognized by my laptop or pi.
Done some research on the different commands and code you can use with sipy and VSCode.

Kevin:
A Pycom SiPy was decided on as the base for the project, with a PyMakr expansion board to allow us to connect the external sensors.


![SiPy](https://user-images.githubusercontent.com/46967737/77871425-ffe42480-723b-11ea-9451-61c301d8bc15.jpg)
![PyMakr](https://user-images.githubusercontent.com/46967737/77871359-c8757800-723b-11ea-8a3e-64505e913547.jpg)

After adding some python code for the boot sequence, along with a main programme, the ID and PAC numbers of the SiPy was obtained. This data was then used to register the device with SigFox.
(see code folder)

Update 25/08/20

Modified the code in main.py to integrate with Sigfox.

Further modified this code to send data 10 times, with a 30 second delay.
![Screenshot_27](https://user-images.githubusercontent.com/46967737/91189528-70f40f00-e6ea-11ea-85b9-05f77fc355ed.png)

Successfully recieved a message on SigFox from the SiPy.
LPWAN connectivity achieved.

Attempted to create a callback to Wia, however login creditials (the API login and password generated by SigFox backend) are deemed invalid by Wia.

![Screenshot_26](https://user-images.githubusercontent.com/46967737/91184833-0096bf00-e6e5-11ea-9427-154a05ac350f.png)


