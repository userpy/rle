#!/usr/bin/env python3
import argparse

class RleEncode:
    def __init__(self, data):
        self.data = data

    def rle_encode(self):
        encoding = ''
        prev_char = ''
        count = 1
        if not self.data:
            return ''

        for char in self.data:
            if char != prev_char:
                if prev_char:
                    encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:

                count += 1
        else:
            encoding += str(count) + prev_char
            return encoding


class RleDecode:
    def __init__(self, data):
        self.data = data

    def rle_decode(self):
        decode = ''
        count = ''
        for char in self.data:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        return decode

def encode(input, output):
    input = open(input, 'r')
    output = open(output, 'w')
    for i in input.readlines():
        val = RleEncode(i)
        output.write(val.rle_encode())
    input.close()
    output.close()

def decode(input, output):
    input = open(input, 'r')
    output = open(output, 'w')
    for i in input.readlines():
        val = RleDecode(i)
        output.write(val.rle_decode())
    input.close()
    output.close()


def main():


    parser = argparse.ArgumentParser(description='decoder')

    parser.add_argument('-i', '--input', default=None)
    parser.add_argument('-o', '--output', default=None)
    parser.add_argument('-e', '--encode', type=bool, nargs='?', const=True, default=False)
    parser.add_argument('-d', '--decode', type=bool, nargs='?', const=True, default=False)

    args = parser.parse_args()
    if args.encode:
        encode(output=args.output, input=args.input)
    elif args.decode:
        decode(output=args.output, input=args.input)



if __name__ == '__main__':
    main()
