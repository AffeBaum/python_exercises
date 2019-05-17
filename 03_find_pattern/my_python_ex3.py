# -*- coding:utf-8 -*-
import re

def main(f_name, target):
    pattern = re.compile("^"+target)
    with open(f_name,"r",encoding="utf-8") as f:
        for line in f:
            if pattern.match(line):
                print(line)
            
if __name__ == "__main__":
    main("README.md", "##")