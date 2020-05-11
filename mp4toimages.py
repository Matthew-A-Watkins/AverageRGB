import cv2

def splitvideotoframes(filename):
  try:
    vidcap = cv2.VideoCapture(str(filename))
  except:
    return("INVALID FILENAME")
    exit()
  vidcap = cv2.VideoCapture(str(filename))
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    if not success:
        break
    count += 1
    

