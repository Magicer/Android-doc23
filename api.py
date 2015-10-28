#coding=utf-8
import os
s1='''<!-- Magicer:http://magicer.xyz -->'''
s2='''<script src="https://developer.android.com/ytblogger_lists_unified.js" type="text/javascript"></script>'''
s3='''<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:light,regular,medium,thin,italic,mediumitalic,bold"
  title="roboto">'''

for root,dirs,files in os.walk(r'/home/magicer/github/docs/'):
	for file in files:
		fd=root+os.sep+file
		if ".html" in fd:
			print fd
			f=open(fd,'r')
			s=f.read().replace(s2,s1)
			f.close()
			f=open(fd,'w')
			f.write(s)
			f.close()