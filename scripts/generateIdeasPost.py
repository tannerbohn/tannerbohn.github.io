from time import strftime, localtime
import subprocess

if __name__ == "__main__":

	# open markdown file
	f = open('/home/tanner/Dropbox/sandbox/IdeaManager/ideas.markdown')
	links = f.read()
	f.close()

	head = "layout: page\ncomments: false\ntitle:  \"Ideas\"\npermalink: /ideas/"
	#date = "date: "+strftime("%Y-%m-%d %H:%M:%S", localtime())
	#head = '---\n'+head +'\n'+date+'\n---\n'
	head = '---\n'+head +'\n---\n'

	preamble = 'A truncated (depth and length) collection of project ideas.\n'
	preamble += 'Projects that are already started, completed, easy, or promising are marked.\n'
	'''
		---
		layout: page
		comments: false
		title: Ideas
		permalink: /ideas/
		---
	'''

	pageText = head+preamble+links

	DIR = '/home/tanner/Dropbox/website/tannerbohn.github.io/'
	fname = "ideas.markdown"

	f = open(DIR+fname, 'w')
	f.write(pageText)
	f.close()