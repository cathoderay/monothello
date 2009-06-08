from pylab import *


def plot(p1_name, p1_score, p2_name, p2_score, ties):
    figure(1, figsize=(4,4))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    labels = [p1_name, 'Tie', p2_name ]
    fracs = [p1_score, ties, p2_score]

    explode=(0, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('%s x %s' % (p1_name, p2_name), bbox={'facecolor':'0.8', 'pad':10})

    show()

