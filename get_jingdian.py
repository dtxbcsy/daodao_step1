import os
import sys
import re

trim_pat_1=re.compile(r'[\n\r\t]',re.S|re.M)
trim_pat_2=re.compile(r'>[ ]*?<',re.S|re.M)

pat0=re.compile(r'<div class="geo-item first">(.*?)<div class="item-other">',re.S|re.M)
pat1=re.compile(r'<a href="(/Attractions.*?)" onclick="ta\.run\(\'ta\.util\.cookie\.setPIDCookie\', \{\}, (.*?)\);">景点',re.S|re.M)
pat2=re.compile(r'<h3 class="item-header">(.*?)<em>(.*?)</em></a>(.*?)</h3>',re.S|re.M)

fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()
text=trim_pat_1.sub('',text)
text=trim_pat_2.sub('><',text)

ret0=pat0.findall(text)

if len(ret0)==1:
	ret1=pat1.findall(ret0[0])
	ret2=pat2.findall(ret0[0])
	if len(ret1)>=1 :
		print sys.argv[2]+"\t"+str(len(ret1))+"\t"+ret1[0][0]+"\t"+ret2[0][1]+"\t"+ret2[0][2]
	else:
		print sys.argv[2]+"\t"+"0"
