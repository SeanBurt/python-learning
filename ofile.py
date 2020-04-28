#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def finallyOpen():
    f = None
    try:
        f = open('demo.py', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('file not found')
    except LookupError:
        print('unknown encoding')
    except UnicodeDecodeError:
        print('decoding failed')
    finally:
        if f:
            f.close()

def withOpen():
    try:
        with open('demo.py', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('file not found')
    except LookupError:
        print('unknown encoding')
    except UnicodeDecodeError:
        print('decoding failed')

def main():
    finallyOpen()
    withOpen()

if __name__ == '__main__':
    main()
