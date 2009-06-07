from pylab import *


# make a square figure and axes
figure(1, figsize=(4,4))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = ['Baby', 'Tie', 'Weak' ]
fracs = [3800, 373, 5827]

explode=(0, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Baby x Weak', bbox={'facecolor':'0.8', 'pad':10})

show()

