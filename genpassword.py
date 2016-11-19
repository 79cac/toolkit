import string
import sys

charset = string.letters + string.digits
charset += '!@#$%^&*()'

setlen = len(charset)

seed = 0

A = 48271
B = 233
C = 689
D = 1298

max_int = 2147483647

def pse_random(mini=0, maxi=setlen):
    global seed
    seed = (seed * seed * seed * A + seed *
            seed * B + seed * C + D) % max_int
    return seed % (maxi - mini) + mini

def genkey(klen):
    return ''.join([charset[pse_random()] for i in range(klen)])

def main():
    global seed

    if len(sys.argv) > 2:
        seed = int(sys.argv[1].encode('hex'), 16) % max_int
        print genkey(int(sys.argv[2]))
    else:
        seed = raw_input('seed: ')
        seed = int(seed.encode('hex')) % max_int
        print genkey(input("len: "))

if __name__ == '__main__':
    main()
