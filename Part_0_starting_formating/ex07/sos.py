
import sys

def main():
    argc = len(sys.argv) - 1
    argv = sys.argv
    if argc == 0:
        s = input().upper()
    elif argc == 1:
        s = argv[1].upper()
    elif argc > 1:
        print("AssertionError")
        return

    to_print = ""
    morse_dict = { " ": "/ ", 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ',':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}
    for c in s:
        if c not in morse_dict:
            print("AssertionError")
            return
        to_print += morse_dict[c] + " "
    print(to_print)

if __name__ == "__main__":
    main()