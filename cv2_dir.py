import cv2
import sys
import pydoc

with open('cv2.md','a') as fout:
	cv2_dir = dir(cv2)
	fout.write('# Parameters\n')
	for cv in cv2_dir[1:1179]:
		fout.write('`' + cv + '`\n')
	sys.stdout = fout
	fout.write('# Functions\n')
	for cv in cv2_dir[1179:]:
		fout.write(cv+'\n')
		fout.write('======\n')
		pydoc.help('cv2.' + cv)
		fout.write('\n')