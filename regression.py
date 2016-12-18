#!/usr/bin/env python
#imports
import csv
import sys
from scipy import polyval, polyfit, sqrt
from pylab import plot, title, xlabel, ylabel, show, ylim, xlim
import numpy as np
from scipy.interpolate import spline

#test if call was correct
if len(sys.argv) >= 4 :
    print("Usage: regression (-h) (filename.csv) (1=<order=<10)\n-h: \t\tdisplay this help text\norder:\t\torder of polynomial to be fit\nfilename.csv:\txname,yname\n             \txunit,yunit\n             \tpoint1x,point1y\n             \tpoint2x,point2y\n             \t.......,.......")
    sys.exit()

#test if in help mode
if len(sys.argv) == 2 :
    if sys.argv[1] == '-h':
        print("Usage: regression (-h) (filename.csv) (1=<order=<10)\n-h: \t\tdisplay this help text\norder:\t\torder of polynomial to be fit\nfilename.csv:\txname,yname\n             \txunit,yunit\n             \tpoint1x,point1y\n             \tpoint2x,point2y\n             \t.......,.......")
        sys.exit()

#input file declaration
if len(sys.argv) == 2 or len(sys.argv) == 3:
    if sys.argv[1] != '-h':
        filenamevar = sys.argv[1]
else :
    filenamevar = raw_input("Enter the .csv file name to read the data from:\t")

#open file
with open(filenamevar, 'rb') as f:
    reader = csv.reader(f)   
    data = list(reader) 

#algorithm to detect if at any point there are more than 2 columns in the file 
count = 0
for i in range(0, len(data)):
    if len(data[i])==2:
        count = count + 1

#error reporting
if (count != len(data)) :
    print("More than 2 columns somewhere\n")
    sys.exit()
elif (count == len(data)):
    count = count - 2
    print(str(count) + " data points read\n")

#extract axis titles   
datanew = data[0]
xname = datanew[0]
yname = datanew[1]
del data[0]

#extract axis units
datanew = data[0]
xunit = datanew[0]
yunit = datanew[1]
del data[0]

#create two lsts, one with each axis data
x = []
y = [] 
for i in range(0, len(data)):
    dataobj = data[i]
    x.append(float(dataobj[0]))
    y.append(float(dataobj[1]))

#define order of polynomial
if len(sys.argv) == 3:
    orderf = float(sys.argv[2])
    order = int(orderf)
    if order < 1 or order > 10 :
        print("Polynomial order not correctly defined, switching to manual:")
        while True:
            order = input("Enter the order of polynomial you wish to fit (between 1 and 10):  ")
            if (order >= 1) & (order <= 10):
                break
else :
    while True:
        order = input("Enter the order of polynomial you wish to fit (between 1 and 10):  ")
        if (order >= 1) & (order <= 10):
            break
    
#calculations
z = np.polyfit(x, y, order)
p = np.poly1d(z)
print("Equation: y = \n %s" %p)
yr = p(x)
err = sqrt(sum((yr-y)**2)/len(y))
print("Standard Deviation = %.5g" %err)
print("Approximate roots: %s" %p.r)

#graphing
xnew = np.linspace(min(x),max(x),300)
ynew = p(xnew)
title(yname + " - " + xname)
plot(x,y,'g.')
plot(xnew,ynew,'r-')
if xunit == None:
    xlabel(xname)
else:
    xlabel(xname + " (" + xunit + ")")
if yunit == None:
    ylabel(yname)
else:
    ylabel(yname + " (" + yunit + ")")
ylim([min([min(y),min(ynew)])-((max([max(y),max(ynew)])- min([min(y),min(ynew)]))/10),max([max(y),max(ynew)])+((max([max(y),max(ynew)])- min([min(y),min(ynew)]))/10)])
xlim([min(x)-((max(x)-min(x))/10),max(x)+((max(x)-min(x))/10)])
show()
















