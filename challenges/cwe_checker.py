import subprocess as s

testFile = "C:\\Users\\Mathew Marchiano\\Desktop\\learnsecurecoding\\challenges\\cwe125.exe"

def cwe125_check(tempFile):
    '''
    Checks to see if user passed cwe125 challenge based off of output.
    '''
    results = s.run([tempFile], capture_output=True, text=True)
    results_arr = results.stdout.strip().split("\n")
    has_passed = True
    fail_reasons = []

    for result in results_arr:
        # Making the assumption that we will always be following a "<test component>: <Pass or fail>" format
        # for reporting results. If we don't do that, this method won't work for all cwe challenges.
        if result.split(": ")[1] == "FAIL":
            hasPassed = False
            fail_reasons.append(result)
    
    return hasPassed, fail_reasons

print(cwe125_check(testFile))