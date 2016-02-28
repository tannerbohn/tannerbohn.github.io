from time import strftime, localtime
import subprocess

if __name__ == "__main__":

	# open markdown file
	f = open('/home/tanner/Dropbox/sandbox/LinkSaver/links.markdown')
	links = f.read()
	f.close()

	head = "layout: page\ncomments: true\ntitle:  \"LinkSaver\"\npermalink: /linksaver/"
	#date = "date: "+strftime("%Y-%m-%d %H:%M:%S", localtime())
	#head = '---\n'+head +'\n'+date+'\n---\n'
	head = '---\n'+head +'\n---\n'
	'''
		---
		layout: post
		comments: true
		title:  "LinkSaver"
		excerpt: "Links with notes I have saved"
		date:   2016-02-26 17:00:00
		---

		---
		layout: page
		mathjax: true
		comments: true
		title: Hacker's guide to Neural Networks
		permalink: /neuralnets/
		---
	'''

	pageText = head+links

	DIR = '/home/tanner/Dropbox/website/tannerbohn.github.io/'
	fname = "linksaver.markdown"

	f = open(DIR+fname, 'w')
	f.write(pageText)
	f.close()