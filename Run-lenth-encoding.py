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




class FileReader:
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.RleEncode = RleEncode
        self.RleDecode = RleDecode

    def __enter__(self):
        self.input = open(self.input, 'r')
        self.output = open(self.output, 'w')
        return self

    def encode(self):
        for i in self.input.readlines():
            val = self.RleEncode(i)
            self.output.write(val.rle_encode())

    def decode(self):
        for i in self.input.readlines():
            val = self.RleDecode(i)
            self.output.write(val.rle_decode())


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.input.close()
        self.output.close()


def main():
    parser = argparse.ArgumentParser(description='decoder')
    parser.add_argument('-i', '--input', default=None)
    parser.add_argument('-o', '--output', default=None)
    parser.add_argument('-e', '--encode', type=bool, nargs='?', const=True, default=False)
    parser.add_argument('-d', '--decode', type=bool, nargs='?', const=True, default=False)
    args = parser.parse_args()

    if args.encode:
        with FileReader(output=args.output, input=args.input) as f:
            f.encode()


    elif args.decode:
        with FileReader(output=args.output, input=args.input) as f:
            f.decode()



if __name__ == '__main__':
    main()
