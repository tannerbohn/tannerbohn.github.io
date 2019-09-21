from time import strftime, localtime
import subprocess

if __name__ == "__main__":

	# open markdown file
	f = open('/home/tanner/GDrive/sandbox/ContentSavers/links.markdown')
	links = f.read()
	f.close()

	head = "layout: page\ncomments: false\ntitle:  \"LinkSaver\"\npermalink: /linksaver/"
	#date = "date: "+strftime("%Y-%m-%d %H:%M:%S", localtime())
	#head = '---\n'+head +'\n'+date+'\n---\n'
	head = '---\n'+head +'\n---\n'
	'''
		---
		layout: page
		comments: true
		title: LinkSaver
		permalink: /linksaver/
		---
	'''

	pageText = head+links

	DIR = '/home/tanner/GDrive/website/tannerbohn.github.io/'
	fname = "linksaver.markdown"

	f = open(DIR+fname, 'w')
	f.write(pageText)
	f.close()