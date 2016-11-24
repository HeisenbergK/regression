Regression
This script does a regression of 1<=order<=10. Takes input from a csv file of format:

  xname,yname
  xunit,yunit
point1x,point1y
point2x,point2y
.......,.......

and does a fitting of a polynomial to them.
One can use regression.py to do the job even by calling it like:
./regression.py (-h) (filename.csv) (1=<order=<10)
