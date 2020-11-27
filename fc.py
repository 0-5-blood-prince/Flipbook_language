#!/usr/bin/env python3
import sys
from PIL import Image
import os.path
def helper(s):
	st = ""
	l = []
	for i in range(len(s)):
		if s[i]=='\n':
			break
		if s[i] ==' ':
			l.append(st)
			st = ""
		else:
			st = st + s[i]
	l.append(st)
	return l
def save_as_pdf(f,images):
	if len(f)==0:
		images[0].save("images.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
	else:
		images[0].save(f, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
def save_as_gif(f,images):
	if len(f)==0:
		images[0].save("images.gif", format = "GIF" ,optimize = False, duration = 40 , loop = 0, save_all=True, append_images=images[1:])
	else:
		images[0].save(f, format = "GIF" ,optimize = False, duration = 40 , loop = 0 ,save_all=True, append_images=images[1:])
def compile(input):
	if(os.path.exists(input[1])):
		f = open(input[1],"r")
		lines = f.readlines()
		images = []
		for line in lines:
			l = helper(line)
			a = int(l[0])
			b = int(l[1])
			im = Image.open(l[2])
		
			for i in range(b-a+1):
				images.append(im)
		for im in images:
			im = im.resize((images[0].size[0],images[0].size[1]),Image.ANTIALIAS)
		if len(input)<=2:
			save_as_pdf("",images)
		else:
			if len(input)>=3:
				if(input[2]=="-pdf"):
					if(len(input)==4):
						save_as_pdf(input[3],images)
					else:
						save_as_pdf("",images)
				elif(input[2]=="-gif"):
					if(len(input)==4):
						save_as_gif(input[3],images)
					else:
						save_as_gif("",images)
				else:
					print("Wrong Argument")

	else:
		print("File doesn't exists")
		return
def main(s):
	print("Hello World")
if __name__ == "__main__":
	n = len(sys.argv)
	if n == 1 or n == 3:
		print("Few Arguments")
	elif n>=2 and n<=4:
		compile(sys.argv)
	else:
		print("UnValid Arguments")
