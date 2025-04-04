from picozero import Speaker
from machine import Pin, UART, time_pulse_us
from time import sleep
import network
import socket
import BlynkLib
import os
import uping
import utime
import time




'''import audiomp3


audio= audiopwmio.PWMaudioOut(board.GP22)
door_note= audioMP3.MP3Decoder(open ("water-relaxing-sound-121599.mp3", "rb"))

audio.play=(door_note)'''



#asigning a channel and baudrate to hc-05(Bluetooth module)



#assigning pin 14 to LED


TV = Pin(2, Pin.OUT)
BULB= Pin(3, Pin.OUT)
EXTEND = Pin(4, Pin.OUT)
FAN= Pin(5, Pin.OUT)
POWER_LED= Pin(6, Pin.OUT)
BLUETOOTH_LED= Pin(7, Pin.OUT)
WIFI_LED= Pin(8, Pin.OUT)
notifier= Speaker(9)
Doorbell = Pin(10, Pin.OUT)
LAMP = Pin(11, Pin.OUT)
trig= Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)
SOUND_SPEED =340
TRIG_PULSE_DURATION_US = 0

def door_sense():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig.value(0)
    
    duration= time_pulse_us(echo, 1, 30000)
    global distance
    distance= SOUND_SPEED * duration / 20000
    time.sleep_ms(500)
    




i=0

for n in range (3):
    notifier.play(536, 0.3, wait=False)        
    POWER_LED.value(1)
    sleep(0.5)
    
    
POWER_LED.value(1)
sleep(1)

def fan_switch_on():
    TV.value(1)
    
'''def bulb_switch_on():
    BULB.value(1)
    
def lamp_switch_on():
    LAMP.value(1)
    
def TV_switch_on():
    FAN.value(1)'''
    
    
led_one=FAN
led_two=BULB
led_three=LAMP
led_four=TV
led_five=EXTEND
led_six=Doorbell




#code to recieve command from Bluetooth

for a in range (6):
    global ssid
    global password
    ssid='HUAWEI Y5 lite'
    password = '2fea2e972c8d'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
BLYNK_TEMPLATE_ID = "TMPL2Pgpph1Id"
BLYNK_AUTH= "BsBrJYqh6p-_bvGvuNH3wVbwVcx0ZugX"
BLYNK_TEMPLATE_NAME= "ACTIVATOR"

    

def Network():
    ssid
    password
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

        
    max_wait = 10
    print('Waiting for connection')
    while max_wait > 10:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1    
        sleep(1)
    status = None
    '''if wlan.status() != 3:
        raise RuntimeError('Connections failed')
    else:'''
    status = wlan.ifconfig()
    print('connection to', ssid,'succesfull established!', sep=' ')
    print('IP-adress: ' + status[0])

    ipAddress = status[0]
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    #addre = socket.getaddrinfo('0.0.0.0', 00) [0][-1]
    global s
    s = socket.socket()
    #s.bind(addre)
    s.bind(addr)
    s.listen(1)
    
        
print (wlan.ifconfig())

####################################################################
def blynks():

        blynk = BlynkLib.Blynk(BLYNK_AUTH)

        @blynk.on("V0") #virtual pin V0
        def v0_write_handler(value): #read the value
            if int(value[0]) == 1:
                BULB.value(1) #turn the led on        
            else:
                BULB.value(0)    #turn the led off
                
        @blynk.on("V1") #virtual pin V0
        def v1_write_handler(value): #read the value
            if int(value[0]) == 1:
                FAN.value(1) #turn the led on        
            else:
                FAN.value(0)    #turn the led off
                

        @blynk.on("V2") #virtual pin V0
        def v2_write_handler(value): #read the value
            if int(value[0]) == 1:
                LAMP.value(1) #turn the led on        
            else:
                LAMP.value(0)    #turn the led off
                
        @blynk.on("V3") #virtual pin V0
        def v3_write_handler(value): #read the value
            if int(value[0]) == 1:
                TV.value(1) #turn the led on        
            else:
                TV.value(0)    #turn the led off
                
        @blynk.on("V4") #virtual pin V0
        def v4_write_handler(value): #read the value
            if int(value[0]) == 1:
                #FAN.value(1) 
                #BULB.value(1) 
                #LAMP.value(1) 
                #TV.value(1)
                wifi()
            #else:
                #FAN.value(0) 
                #BULB.value(0) 
                #LAMP.value(0) 
                #TV.value(0)
                #blynks
                
     
                

        while True:
            door_sense()
         
            if distance >=6 and distance <=30:
             
                 Doorbell.value(1)
                 sleep(0.1)
                 Doorbell.value(0)
                 sleep(0.1)
                 print(distance)
                 BLUETOOTH_LED.value(0)
                 sleep(0.2)
                 BLUETOOTH_LED.value(1)
                 sleep(0.2)
            blynk.run()
###################################################################
    
def wifi():
    
        global wlan
        
        print('Wi-Fi  Mode')
        
        while True:
            
            global WIFI_LED
            global BLUETOOTH_LED
            BLUETOOTH_LED.value(0)
            WIFI_LED.value(1)
            
            '''door_sense()
            
            if distance >=6 and distance <=30:
             
                 Doorbell.value(1)
                 sleep(0.1)
                 Doorbell.value(0)
                 sleep(0.1)
                 print(distance)
                 BLUETOOTH_LED.value(0)
                 sleep(0.2)
                 BLUETOOTH_LED.value(1)
                 sleep(0.2)
           '''
            
            
            
            
            

            global s
            cl, addr = s.accept()
            print('Connection from ', addr, "accepted!")
            request = cl.recv(1024)
            request = str(request)
            
            
            
            
            if request.find('/led/one') == 6:
                led_one.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            if request.find('/led/two') == 6:
                led_two.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            if request.find('/led/three') == 6:
                led_three.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            
            if request.find('/led/four') == 6:
                led_four.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            if request.find('/led/five') == 6:
                led_five.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
                
            if request.find('/led/all') == 6:
                led_one.toggle()
                led_two.toggle()
                led_three.toggle()
                led_four.toggle()
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            if request.find('/led/door') == 6:
                Doorbell.value(1)
                sleep(0.2)
                Doorbell.value(0)
                sleep(0.2)
                
                WIFI_LED.value(0)
                sleep(0.2)
                WIFI_LED.value(1)
                sleep(0.2)
                
            if request.find('/led/blue') == 6:
                global i
                i=2
                blue_tooth()
                
            if request.find('/led/internet') == 6:
                blynks()
                    
                
                
            
                
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(Website())
            cl.close()
            
            
                
                   
def blue_tooth():
     global WIFI_LED
     global BLUETOOTH_LED
     WIFI_LED.value(0)
     
     
     uart = UART (0,9600)
     while True:
         global i
         i=i+0
         break
     print ('Bluetooth mode',i)

     while True:
         BLUETOOTH_LED.value(0)
         sleep(0.2)
         BLUETOOTH_LED.value(1)
         sleep(0.2)
         
         if uart.any():
             break
     
    
     while True:
         door_sense()
         
         if distance >=6 and distance <=40:
             
             Doorbell.value(1)
             sleep(0.1)
             Doorbell.value(0)
             sleep(0.1)
             print(distance)
             BLUETOOTH_LED.value(0)
             sleep(0.2)
             BLUETOOTH_LED.value(1)
             sleep(0.2)
             
         
         if uart.any():                 #check if connection is available
                data=uart.read()             #Read data from the conection
                data=str(data)              #Convert the data collected back to string
                data=data.upper()
                print (data)               #display the data received
                
                
                

                if ("TV ON" in data):      # if LED_ON is the data recieved    
                    TV.value(1)    #turn on the led
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif("TV OFF" in data):  # else if LED_OFF is the data recieved
                    TV.value(0)             #turn off the led
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                if ('BULB ON' in data):
                    BULB.value(1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif ('BULB OFF' in data):
                    BULB.value(0)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                if ('LAMP ON' in data):
                    LAMP.value(1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif ('LAMP OFF' in data):
                    LAMP.value(0)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                if ('FAN ON' in data):
                    FAN.value(1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif ('FAN OFF' in data):
                    FAN.value(0)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                    
                if ('EXTENSION ON' in data):
                    EXTEND.value(1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif ('EXTENSION OFF' in data):
                    EXTEND.value(0)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                
                if ('ALL OFF' in data):
                    FAN.value(0)
                    
                    TV.value(0)
                    BULB.value(0)
                    LAMP.value(0)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                elif ('ALL ON' in data):
                    FAN.value(1)
                    TV.value(1)
                    BULB.value(1)
                    LAMP.value(1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                if ("JINGLE BELL" in data):
                    Doorbell.value(1)
                    sleep(0.1)
                    Doorbell.value(0)
                    sleep(0.1)
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                    
                if ('DISCONNECTED' in data):
                    blue_tooth()
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                    
                if ('WIFI ON' in data):
                    
                    BLUETOOTH_LED.value(0)
                    sleep(0.2)
                    BLUETOOTH_LED.value(1)
                    sleep(0.2)
                    
                    global wlan
                    if wlan.isconnected()==False:
                        global ssid
                        ssid
                        global password
                        password 
                        wlan = network.WLAN(network.STA_IF)
                        wlan.active(True)
                        wlan.connect(ssid, password)
                        global ssid
                        ssid
                        global password
                        password
                        wlan = network.WLAN(network.STA_IF)
                        wlan.active(True)
                        wlan.connect(ssid, password)
                        blue_tooth()
                    
                    if wlan.isconnected():
                        global i
                        if i==0:
                            Network()
                            wifi()
                        else:
                            wifi()
                            
                    
                
                
                


                

def Website():
    value_one = led_one.value()
    value_two = led_two.value()
    value_three=led_three.value()
    value_four= led_four.value()
    value_five = led_five.value()
    website = """<!DOCTYPE html>
    <html>
        <head> <title> ACTIVATOR </title>
        <style>
        td{
                font-size: 40px;
        padding: 20px;
        
            }
            
        th{
                font-size: xx-large;
            }
            
            
          h2{
                font-size: 50px;
                padding: 20px;
            }

          h1{
                font-size: 100px;
            }
        
        
        </style>
        </head>
    
        <body>
            <!--<h1><center> ACTIVATOR </center></h1>--!>
        
            <!--<h2><center>ACTIVATOR WIRELESS CONTROL</center></h2>--!>
            
            <table style="width:1020px" class="center">
                  <tr>
                    <th><center>DEVICES </center></th>
                    <th><center>SWITCHES </center> </th>
                    <th><center>DEVICE STATES</center> </th>
                  </tr>
                  <tr>
                    <td><center><b> FAN </td>
                    <td><center><input type='button'style='width:350px; height:150px; font-size:30px' value='ON/OFF' onclick='toggleLed("one")'/> </center></td>
                    <td> <center>  <span id="value_one">""" + str(value_one) + """</span></center> </td>
                  </tr>
                  <tr>
                    <td><center><b>BULB</center> </td>
                    <td><center><input type='button' style='width:350px; height: 150px; font-size:30px' value='ON/OFF' onclick='toggleLed("two")'/></center></td>
                    <td><center>  <span id="value_two">""" + str(value_two) + """</span></center></td>
                   </tr>
                   <tr>
                    <td><center><b>LAMP</center> </td>
                    <td><center><input type='button' style='width:350px; height: 150px; font-size:30px' value='ON/OFF' onclick='toggleLed("three")'/></center></td>
                    <td><center>  <span id="value_three">""" + str(value_three) + """</span></center></td>
                   </tr>
            <tr>
                    <td><center><b>TV</center> </td>
                    <td><center><input type='button' style='width:350px; height: 150px; font-size:30px' value='ON/OFF' onclick='toggleLed("four")'/></center></td>
                    <td><center>  <span id="value_four">""" + str(value_four) + """</span></center></td>
                   </tr>
                   
            <tr>
                    <td><center><b>Extension Socket</center> </td>
                    <td><center><input type='button' style='width:350px; height: 150px; font-size:30px' value='ON/OFF' onclick='toggleLed("five")'/></center></td>
                    <td><center>  <span id="value_five">""" + str(value_five) + """</span></center></td>
                   </tr>
            
                   
            <tr>
                    <td><center><b>ALL</center> </td>
                    <td><center><input type='button' style='width:350px; height: 150px; font-size:30px' value='ON/OFF' onclick='toggleLed("all")'/></center></td>
                    <td><center>  <span id="value_all"> </span></center></td>
                   </tr>
                   
            <tr>
                    <td><center><b>Doorbell</center> </td>
                    <td><center><input type='button' style='width:220px; height: 100px; font-size:30px' value='Doorbell' onclick='toggleLed("door")'/></center></td>
                    <td><center>  <span id="value_door"> </span></center></td>
                   </tr>
            
                   
            <tr>
                    <td><center><b>MODE</center> </td>
                    <td><center><input type='button' style='width:220px; height: 100px; font-size:30px' value='BLUETOOTH' onclick='toggleLed("blue")'/></center></td>
                    <td><center>  <span id="value_blue"> </span></center></td>
                   </tr>

            <tr>
                    <td><center><b>MODE</center> </td>
                    <td><center><input type='button' style='width:220px; height: 100px; font-size:30px' value='Internet' onclick='toggleLed("internet")'/></center></td>
                    <td><center>  <span id="value_internet"> </span></center></td>
                   </tr>

            </table>
              <!--  <p>
                   <center>
                   <br> <input type='button' value='Check Update 'style='width:350px; height: 20px; font-size:large' onclick='update()'> </br>
                   </center>
                </p> --!>
                                    
            <script>
                function toggleLed(led){
                    var xhttp = new XMLHttpRequest();
                    xhttp.open('GET', '/led/'+led, true);
                    xhttp.send();
                     
                }
                function update(){
                    location.reload(true);
                }
                    
            </script>
        </body>
    </html>
    """
    return website


    
   

        
#if wlan.ifconfig()[0]=='192.168.43.123':
if wlan.isconnected():
    Network()
    wifi()
    blue_tooth()
      
     
elif wlan.isconnected()==False:
    blue_tooth()
    Network()
    wifi()

        
       
#Reset()