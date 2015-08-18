import cv2

with open('cv2.txt','a') as fout:
	cv2_dir = dir(cv2)
	for cv in cv2_dir:
		fout.write(cv+'\n')