import os
import argparse

def rename(path,filename,extension):
	items = 0
	for file in os.listdir(path):
		new_file_name = str(filename)+str(items)+str(extension)
		os.rename(os.path.join(path,file),os.path.join(path,new_file_name))
		items += 1
		print(path,new_file_name)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--path', help="set ur folder path, default = ./", default='./', type=str)
	parser.add_argument('-f', '--file_name', help="set a new file name, default = data", default='data', type=str)
	parser.add_argument('-e', '--extension', help="set the file name extension, default = .jpg", default='.jpg', type=str)
	args = parser.parse_args()
	print(args.path,args.file_name)

rename(args.path,args.file_name,args.extension)