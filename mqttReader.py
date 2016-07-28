def getNativeFiltersTime():
    fileName = "/home/ariel/Documents/CorePerformance/mosquittoLogBIGFILE.log"
    with open(fileName) as f:
        word = "upc"
        for line in f:
            if word in line:
                print line[:-1]

getNativeFiltersTime()
