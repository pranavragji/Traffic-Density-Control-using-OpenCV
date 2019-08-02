# Traffic-Density-Control-using-OpenCV

For this project you require

1.Raspberry Pi

2.Pi Cam

3.Python 3

4.OpenCV

In this project, I have created two lines perpendicular to each other. One line adds to the counter and one subtracts. When a car passes through line 1(add), the counter is increased. This will go on till the counter threshold which has been set. When that threshold is reached, the signal will increase for that lane as there is a large density of cars there. When a car leaves and goes through line 2(subtract), the counter decreases. This will then take the signal time to the normal amount.

Notes:

The Blue sticker side of the Pi Cam should be facing the USB ports.

sudo modprobe bcm2835-v4l2 <--- This is an important code which helped me throughout this project. If while running the camera you get an assertion failed error, running the code will solve it.

For displaying your raspberry pi to your Windows Computer you can use RemoteDesktop. You require your RaspberryPi's IP address which you can find by using the ifconfig command and taking the inet address. This address will connect you to your raspberry pi and you will have to put your username and password for your pi. Typically your username is "pi" and password is "raspberry". But you have to enable SSH from your interfacing options.

To shutdown your Raspberry Pi from RemoteDesktop run this Command. (sudo shutdown -h now)
