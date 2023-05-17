#!/usr/bin/env python3

with open("/path/to/output.txt", "w") as f:
    print("Hello stackoverflow!", file=f)
    print("I have a question.", file=f)
