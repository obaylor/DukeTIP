import numpy as np

fivebyfour = np.ones((4, 5))
print (fivebyfour)
fivebyone = np.zeros(5)
print (fivebyone)
onesM = (fivebyfour * fivebyone)
print onesM
fivebyfour[1, 2] = 10
print fivebyfour
print (fivebyfour * 2)
np_sum = np.sum(fivebyfour[:])
print (np_sum)
print fivebyfour.sum()
print fivebyfour.sum(axis=0)
print fivebyfour.sum(axis=1)
