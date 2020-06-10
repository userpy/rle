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

def main():
    parser = argparse.ArgumentParser(description='decoder')

    parser.add_argument('-data', '--data', default=None)
    parser.add_argument('-encode', '--encode', type=bool, nargs='?', const=True, default=False)
    parser.add_argument('-decode', '--decode', type=bool, nargs='?', const=True, default=False)

    args = parser.parse_args()
    if args.encode:
        val = RleEncode(args.data)
        print(val.rle_encode())
    elif args.decode:
        val_decode = RleDecode(args.data)
        print(val_decode.rle_decode())



if __name__ == '__main__':
    main()
