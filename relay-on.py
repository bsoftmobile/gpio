#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import ConfigParser
 
config = ConfigParser.RawConfigParser()            #Ğ²Ğ¾ÑĞ¿Ğ¾Ğ»ÑŒĞ·ÑƒĞµĞ¼ÑÑ ĞºĞ¾Ğ½Ñ„Ğ¸Ğ³Ğ¾Ğ¼
config.read("/home/sboichenko/prj/gpio/global-config.conf")         #ÑÑ‡Ğ¸Ñ‚Ğ°ĞµĞ¼ ĞºĞ¾Ğ½Ñ„Ğ¸Ğ³
pin_number = config.getint("relay_pins", "relay1") #Ğ¿Ğ¸Ğ½Ğ° Ğ¸Ğ· ĞºĞ¾Ğ½Ñ„Ğ¸Ğ³Ğ° Ğ¿Ñ€Ğ¸ÑĞ²Ğ¾ĞµĞ¼ Ğ¿ĞµÑ€ĞµĞ¼ĞµĞ½Ğ½Ğ¾Ğ¹ pin_number
  
print "use pin:"+str(pin_number)
   
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)            
GPIO.setup(pin_number, GPIO.OUT)   #¿¿¿¿¿¿¿¿¿¿¿¿¿ ¿¿¿ ¿¿ ¿¿¿¿¿¿¿¿ ¿¿¿¿¿¿
GPIO.output(pin_number, GPIO.HIGH) #¿¿¿¿¿¿ ¿¿¿¿¿¿



