"""
Core Performance Reader

reads log an extract perfomance informations.
@author Ariel Iporre

"""
import numpy as np
import subprocess
import time

def getNativeFiltersTime():
    fileName = "/home/ariel/Documents/CorePerformance/MCB.log"
    word = "LPT.native: "
    marks = ["sourceFilter=", "pointInZone=", "doorEvent=", "shiftZone=", "identifiers=", "total="]
    marksPositions = [8, 9, 10, 11, 12, 13]
    with open(fileName) as f:
        for line in f:
            if word in line:
                a = []
                # print line
                b = line[:-1].split(" ")
                cnt = 0
                for mark in marks:
                    position = marksPositions[cnt]
                    cnt += 1
                    c = b[position]
                    offset = len(mark)
                    a.append(c[offset:])
                print a[0] + " " + a[1] + " " + a[2] + " " + a[3] + " " + a[4] + " " + a[5]

getNativeFiltersTime()
