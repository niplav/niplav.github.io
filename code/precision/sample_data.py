import numpy as np
import algorithms

d1=np.array([[1,0.8],[0,0.4],[0,0.65],[1,0.99]]).T
oc=d1[0]
pr=d1[1]

d2=np.array([[1,0.8],[0,0.4],[0,0.65],[1,0.9]]).T
oc2=d1[0]
pr2=d1[1]

d3=np.array([[0,0.8],[1,0.4],[1,0.65],[0,0.9]]).T                           
oc3=d1[0]
pr3=d1[1]

differences1=score_differences(d1, samples=1000, low=0, high=25, div=50)
differences2=score_differences(d1, samples=1000, low=0, high=25, div=50)
differences3=score_differences(d1, samples=1000, low=0, high=25, div=50)
