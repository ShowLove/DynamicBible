import os
import sys
import fileinput

f = open("/Users/carlosgarzon/Desktop/Bereshit/Bereshit_Data.txt",'r')
filedata = f.read()
newdata = filedata.replace("["," ")
newdata = newdata.replace("]"," ")
newdata = newdata.replace("{"," ")
newdata = newdata.replace("}"," ")
newdata = newdata.replace("in~him","in~him 9990")
newdata = newdata.replace("to~you(mp)","to~you(mp) 9991")
newdata = newdata.replace("to~them(mp)","to~them(mp) 9992")
f.close()

f = open("/Users/carlosgarzon/Desktop/Bereshit/Bereshit_Data_Parsed.txt",'w')
f.write(newdata)
f.close()
