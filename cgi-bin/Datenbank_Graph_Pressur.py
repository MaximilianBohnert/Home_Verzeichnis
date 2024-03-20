#!/usr/bin/python3
import rrdtool
filname="/home/MMB/BMP280.rrd"
ret =  rrdtool.graph('-' ,
	'--imgformat', 'PNG' ,
	'--width', '640' ,
	'--height', '400' ,
	'--start', '-1hour' ,
	'--end', 'now' ,
	'--vertical-label', "hP" ,
	'--alt-autoscale' ,
	'--title', 'Pressur' ,
	'DEF:Pressur='+filname+':Pressur:AVERAGE' ,
	#'AREA:Pressur#CCCCFF:' ,
	'LINE1:Pressur#0000FF:Pressur BMP280' ,
	'GPRINT:Pressur:MIN:Min\\: %4.2lf hP' ,
	'GPRINT:Pressur:MAX:MAX\\: %4.2lf hP' ,
	'GPRINT:Pressur:AVERAGE:Avg\\: %4.2lf hP' ,
	'GPRINT:Pressur:LAST:Aktuell\\: %4.2lf hP')
