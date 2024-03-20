#!/usr/bin/python3
import rrdtool
filname="/home/MMB/BMP280.rrd"
filname2="/var/www/html/temperatur2.rrd"
ret =  rrdtool.graph('-' ,
	'--imgformat', 'PNG' ,
	'--width', '640' ,
	'--height', '400' ,
	'--start', '-1hour' ,
	'--end', 'now' ,
	'--vertical-label', "Grad Celcius" ,
	'--alt-autoscale' ,
	'--title', 'Temperatur' ,
	'DEF:Temperatur='+filname+':Temperatur:AVERAGE' ,
	#'AREA:Temperatur#FFCCCC:' ,
	'LINE1:Temperatur#FF0000:Temperatur BMP280' ,
	'GPRINT:Temperatur:MIN:Min\\: %3.2lf °C' ,
	'GPRINT:Temperatur:MAX:MAX\\: %3.2lf °C' ,
	'GPRINT:Temperatur:AVERAGE:Avg\\: %3.2lf °C' ,
	'GPRINT:Temperatur:LAST:Aktuell\\: %3.2lf °C' ,
	'DEF:templ='+filname2+':templ:AVERAGE' ,
        #'AREA:templ#CCCCFF:' ,
        'LINE1:templ#0000FF:Temperatur DS18B20' ,
        'GPRINT:templ:MIN:Min\\: %3.2lf °C' ,
        'GPRINT:templ:MAX:MAX\\: %3.2lf °C' ,
        'GPRINT:templ:AVERAGE:Avg\\: %3.2lf °C' ,
        'GPRINT:templ:LAST:Aktuell\\: %3.2lf °C')
