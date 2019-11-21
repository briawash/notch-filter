"""
Brianca Washington
1001132562
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def plotting(fig,title,results,upperbound, lowerbound, t):
	plt.plot(fig)
	plt.title(title)
	# plot the functions
	if(t>10) :
		length=np.arange(0,t,1)
		plt.plot(length,results)
	else:
		plt.plot(results)
	if(t==1):
		plt.ylim(lowerbound, upperbound)
	else:
		plt.xlim(lowerbound, upperbound)
	plt.show()
def applyNotch(fs, dataFile) :

    #open the and extract the signal
	sig = np.genfromtxt(dataFile, delimiter=",")
	x=np.append(sig,np.zeros(100))
	f=17
	w=(2*np.pi*f/fs)
	y=np.zeros(len(x))
	# what we know/assume
	y[0]=x[0]
	y[1]=x[1]
	i=2
	#notch filter from the already values
	for i in range(len(x)):
	 	y[i]= -2*np.cos(w)*x[i-1] + x[i-2] + x[i] + 1.8744*np.cos(w)*y[i-1] -.8783*y[i-2]

	 # make 10+33 Hz sig 
	length=np.arange(0,len(x),1)
	ten= np.cos(2*np.pi*10*(length/fs)) 
	thirtythree=np.cos(2*np.pi*33*(length/fs))
	third= ten +thirtythree
	#plot
	plotting(1,"Original Signal",sig,625,-25,0)
	plotting(2,"Filtered Signal",y,2.25,-2.25,1)
	plotting(3,"10Hz + 33Hz Signal",third,625,-25,len(y))



############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
