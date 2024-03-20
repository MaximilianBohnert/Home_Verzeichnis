#!/usr/bin/env python3

import spidev
def massage_erstellen(LEDs):
	msg = []
	for farbe in LEDs:
        	for farb_byte in farbe:
                	for bit in range(7,-1,-1):
                        	if (farb_byte>>bit)&1 == 0:
                                	msg.append(0x80)
                	        else:
              	                	msg.append(0xF8)
	return msg

LEDs = [[16,0,0],[0,16,0],[0,0,16],[16,16,16],[0,55,0]]

msg = massage_erstellen(LEDs)

spi = spidev.SpiDev()
spi.open(0,0)
spi.xfer(msg,int(8/1.25e-6))
 
