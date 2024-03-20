#!/bin/bash
filname="/var/www/html/temperatur2.rrd"
rrdtool graph - \
	--imgformat 'PNG' \
	--width 640 \
	--height 400 \
	--start -1hour \
	--end now \
	--vertical-label "Grad Celcius" \
	--alt-autoscale \
	--title Temperatur \
	DEF:temp1=$filname:templ:AVERAGE \
	AREA:temp1#CCCCFF: \
	LINE1:temp1#0000FF:'Temperatur DS18B20' \
	GPRINT:temp1:MIN:"Min\\: %3.2lf °C " \
	GPRINT:temp1:MAX:"MAX\\: %3.2lf °C" \
	GPRINT:temp1:AVERAGE:"Avg\\: %3.2lf °C " \
	GPRINT:temp1:LAST:"Aktuell\\: %3.2lf °C "
