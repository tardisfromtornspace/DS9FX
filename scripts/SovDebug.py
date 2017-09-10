import nt

bWrite = 0
sFile = "scripts\\Custom\\DS9FX\\SovDebug.log"

def debug(sLine):
	if bWrite:	
		from time import time, localtime, strftime
		sTime = strftime("%d %b %Y %H:%M:%S", localtime(time()))
		sLine = "Time: " + sTime + ", Logged: " + sLine + "\n"
		file = nt.open(sFile, nt.O_WRONLY | nt.O_APPEND | nt.O_CREAT)
		nt.write(file, sLine)
		nt.close(file)