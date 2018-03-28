from time import strftime, localtime
import subprocess

if __name__ == "__main__":

	# open markdown file
	f = open('/home/tanner/Dropbox/sandbox/ContentSavers/papers.markdown')
	papers = f.read()
	f.close()

	head = "layout: page\ncomments: true\ntitle:  \"PaperSaver\"\npermalink: /papersaver/"
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

	DIR = '/home/tanner/Dropbox/website/tannerbohn.github.io/'
	fname = "papersaver.markdown"

	f = open(DIR+fname, 'w')
	f.write(pageText)
	f.close()