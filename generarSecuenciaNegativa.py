import random
import sys

def shuffleSet(file):
    with open(file) as fileS:

        with open("dataset500_negative.txt", 'w') as f:
            sys.stdout = f
            while True:
                a = fileS.readline().strip('\n')
                if(a==""):
                    break
                print(a)
                b = fileS.readline().strip('\n')
                bArr = [b[i:i+2] for i in range(0, len(b), 2)]
                random.shuffle(bArr)
                result = ''.join(bArr)
                print(result)
            f.close()
        fileS.close()


shuffleSet("dataset500.txt")

