"""
Socket monitor,


"""
import numpy as np
# import matplotlib.pyplot as plt
import subprocess
import time
"""

"""
def getFTPConnection():
    p = subprocess.Popen('ss -t state established | grep ftp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lineCounter = 0
    for line in p.stdout.readlines():
        lineCounter += 1
    retval = p.wait()
    print "current connections: " + str(lineCounter)
    return lineCounter

a = []

for i in range(1,500):
    print "getting active fgit initytp connections. Time: " + str(i*0.1) + " seconds"
    a.append(getFTPConnection())
    time.sleep(0.1)
print "FTP count vector: " + str(a)

# f = plt.figure()
# f.plt(a)
# f.show()
