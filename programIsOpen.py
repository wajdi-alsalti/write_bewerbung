import psutil


def checkIfProgrammeOpen(programName:str):
	if programName in (p.name() for p in psutil.process_iter()):# program is open
		return True
	else:
		return False
