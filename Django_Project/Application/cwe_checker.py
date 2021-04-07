import subprocess as s
from datetime import datetime as date
from pathlib import Path, PurePath
import os
join = PurePath.joinpath

folderPath = join(Path(__file__).resolve().parent.parent, 'Challenges')
tempPath = join(folderPath, 'temp')

# create tempPath if it does not exist
if not os.path.exists(tempPath): os.makedirs(tempPath)

# This is the "main" function that takes user code, join/compile/runs it, and returns the response to the user (in HTML format).
def RunChecker(fileKey, userCode, thisTitle, nextTitle):
	
	has_passed, fail_reasons = JoinCompileAndRun(fileKey, userCode)
	
	if (has_passed):
		message = '<p class="lessonchallenge-congrats">Congratulations!</p>' + \
			'<p>You have completed the challenge for ' + thisTitle + '. ' + \
			'Click "proceed" to move on to ' + nextTitle + '.</p>'
	else:
		failMessage = ''
		for reason in fail_reasons:
			failMessage += ' - ' + str(reason) + '<br>'
		message = '<p class="lessonchallenge-sorry">Sorry, you did not successfully complete the challenge.</p>' + \
			'<p>Fail reason:</p>' + \
			'<pre>' + failMessage + '</pre>'
	
	return has_passed, message

# This is the function that joins the user code with the challenge code, compiles it, and runs it.
def JoinCompileAndRun(fileName, userCode):
	
	finalCode = joinCodeWithChallenge(fileName, userCode)
	
	# create a file key from the exact current time
	now = date.now()
	fileKey = now.strftime("%Y%m%d-%H%M%S-%f")
	
	# path for source code
	srcCodePath = join(tempPath, fileKey + '.c')
	# path for compiled executable (gcc on windows automatically adds .exe, so we need to account for that)
	executablePath = join(tempPath, fileKey)
	executablePathWin = join(tempPath, fileKey + '.exe')
	# Open source file, write the code to it, and close it
	srcCodeFile = open(srcCodePath, 'w+')
	srcCodeFile.write(finalCode)
	srcCodeFile.close()
	
	# compile
	didCompile, compileFailReasons = compile(srcCodePath, executablePath)
	
	# Default values for has_passed and fail_reasons, can be overrided when cwe#_check is executed
	has_passed = False
	fail_reasons = []
	
	# run checker if the compilation succeeded
	if didCompile == True:
		# Run checker for cwe125
		if (fileName == 'cwe125'):
			has_passed, fail_reasons = cwe_check(executablePath, 1)
			print(has_passed)
			print(fail_reasons)
		# cwe20 checker
		if (fileName == 'cwe20'):
			has_passed, fail_reasons = cwe_check(executablePath, 1)
			print(has_passed)
			print(fail_reasons)

		else:
			print('No other challenges yet supported.')
			fail_reasons.append('No other challenges yet supported.')
	else:
		#todo: implement failed compilation
		print('Did not successfully compile')
		fail_reasons.append('Did not successfully compile:')
		for reason in compileFailReasons:
			fail_reasons.append(reason)
		
	# and delete source+executable when done
	delete(srcCodePath)
	delete(executablePath)
	delete(executablePathWin)
	
	return has_passed, fail_reasons

# join user-provided code with challenge source code
def joinCodeWithChallenge(fileName, userCode):
	
	sourcePath = join(folderPath, fileName + '.c')
	source = open(sourcePath).read()
	
	# get the index of the "begin" statement (and add its length to get where it ends)
	startIdx = source.index('/* BEGIN USER-SUBMITTED */\n') + 27 
	endIdx = len(source)
	
	# join the code
	finalCode = source[0:startIdx] + userCode + source[startIdx:endIdx]
	
	return finalCode

# compile a given source into a given output file
def compile(filePath, outputPath):
	
	child = s.run(['gcc', str(filePath), '-o', str(outputPath)], capture_output=True, text=True)
	out = child.stdout.strip()
	err = child.stderr.strip()
	print(out)
	print(err)
	
	has_passed = True
	fail_reasons = []
	
	if (err):
		has_passed = False
		fail_reasons.append('Failed to compile') # TODO: add more info
	
	return has_passed, fail_reasons

def cwe_check(tempFile, numAttemptsRemaining):
	'''
	Checks to see if user passed cwe125 challenge based off of output.
	'''
	if (numAttemptsRemaining < 0): return False, ['Failed to Execute Binary (NOTE: This occasionally happens when the runtime environment detects an invalid behavior from the executable, such as an out-of-bounds read. You can try again, but your solution was most likely not complete.)']
	
	try: 
		# Sometimes the executable inexplicably crashes. We have to handle that by just catching an error and retrying.
		results = s.run([str(tempFile)], capture_output=True, text=True)
		results_arr = results.stdout.strip().split("\n")
		has_passed = True
		fail_reasons = []

		for result in results_arr:
			# Making the assumption that we will always be following a "<test component>: <Pass or fail>" format
			# for reporting results. If we don't do that, this method won't work for all cwe challenges.
			print(result)
			if result.split(": ")[1] == "FAIL":
				has_passed = False
				fail_reasons.append(result)
		
		return has_passed, fail_reasons
	except:
		# if failed to run executable, try again
		print('Failed to run executable. ' + str(numAttemptsRemaining) + ' attempts remaining.')
		return cwe_check(tempFile, numAttemptsRemaining - 1)


# little method to delete files
def delete(filePath):
	if os.path.exists(filePath): os.remove(filePath)
	return

# Run tests if this python script is being run by itself
if __name__ == '__main__':
	#1 and 2 are bad ones that fail, 3 is good one that passes
	testUserCode1 = "int getValueFromArray(int *array, int len, int index) {int value; value = array[index]; return value;}"
	testUserCode2 = "int getValueFromArray(int *array, int len, int index) {return 0;}"
	testUserCode3 = "int getValueFromArray(int *array, int len, int index) {int value;if (index < len && index >= 0) {value = array[index];}else {value = -1;}return value;}"

	cwe20_test = "bool checkInput(int *inputToCheck, int index) {bool isChecked; if ((inputToCheck[index] <= MAX_VAL) & (inputToCheck[index] >= MIN_VAL)) {isChecked = true;}else {isChecked = false;}return isChecked;}"


	#test run these three (now four) binaries
	print(RunChecker('cwe125', testUserCode1, 'title1', 'title2'))
	print(RunChecker('cwe125', testUserCode2, 'title1', 'title2'))
	print(RunChecker('cwe125', testUserCode3, 'title1', 'title2'))

	print(RunChecker('cwe20', cwe20_test, 'title1', 'title2'))
	


