from time import strftime, localtime
import subprocess

if __name__ == "__main__":

	# open markdown file
	f = open('/home/tanner/Dropbox/sandbox/LinkSaver/links.markdown')
	links = f.read()
	f.close()

	head = "layout: post\ncomments: true\ntitle:  \"LinkSaver\"\nexcerpt: \"Links with notes I have saved\""
	date = "date: "+strftime("%Y-%m-%d %H:%M:%S", localtime())
	head = '---\n'+head +'\n'+date+'\n---\n'
	'''
		---
		layout: post
		comments: true
		title:  "LinkSaver"
		excerpt: "Links with notes I have saved"
		date:   2016-02-26 17:00:00
		---
	'''

	pageText = head+links

	DIR = '/home/tanner/Dropbox/website/tannerbohn.github.io/_posts/'
	fname = "2016-02-26-linksaver.markdown"

	f = open(DIR+fname, 'w')
	f.write(pageText)
	f.close()