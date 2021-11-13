import sys

def formatCNN(fileP, fileN):
    with open("dataset500CNN.txt", 'w') as f:
        sys.stdout = f
        print("sequence,Bound")
        with open(fileP) as fP:
            while True:
                a = fP.readline().strip('\n')
                if(a==""):
                    break
                b = fP.readline().strip('\n')
                print(b + ", 1")
            fP.close()
        with open(fileN) as fN:
            while True:
                a = fN.readline().strip('\n')
                if(a==""):
                    break
                b = fN.readline().strip('\n')
                print(b + ", 0")
            fN.close()
        

formatCNN("dataset500.txt", "dataset500_negative.txt")