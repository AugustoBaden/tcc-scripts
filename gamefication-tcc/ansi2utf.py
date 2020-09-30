import csv
import pymysql
import pandas as pd
import sys
import os
import time
import codecs
# caso seja necessario comverter algum arquivo csv para o formato utf 8
blockSize = 1048576
with codecs.open("nome arquivo origem.csv","r",encoding="mbcs") as sourceFile:
    with codecs.open("nome arquivo final.csv","w",encoding="UTF-8") as targetFile:
        while True:
            contents = sourceFile.read(blockSize)
            if not contents:
                break
            targetFile.write(contents)