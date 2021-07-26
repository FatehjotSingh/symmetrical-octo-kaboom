import csv
import random
import pandas as pd
import statistics as st
import plotly.figure_factory as pff
import plotly.graph_objects as pgo

fil= pd.read_csv('StudentsPerformance.csv')

rs= fil['reading score'].tolist()

mean=sum(rs)/len(rs)
sd=st.stdev(rs)
median = st.median(rs)
mode=st.mode(rs)

print(mean)
print(sd)
print(median)
print(mode)

sd1s,sd1e =  mean-sd,mean+sd
sd2s,sd2e = mean-(2*sd),mean+(2*sd)
sd3s,sd3e = mean-(3*sd),mean+(3*sd)

grap= pff.create_distplot([rs],['name'],show_hist=False)

grap.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name='mean'))

grap.add_trace(pgo.Scatter(x=[sd1s,sd1s],y=[0,0.20],mode='lines',name='sd1s'))
grap.add_trace(pgo.Scatter(x=[sd1e,sd1e],y=[0,0.20],mode='lines',name='sd1e'))

grap.add_trace(pgo.Scatter(x=[sd2s,sd2s],y=[0,0.20],mode='lines',name='sd2s'))
grap.add_trace(pgo.Scatter(x=[sd2e,sd2e],y=[0,0.20],mode='lines',name='sd2e'))

grap.show()

sd1list=[result for result in rs if result>sd1s and result<sd1e]
sd2list=[result for result in rs if result>sd2s and result<sd2e]
sd3list=[result for result in rs if result>sd3s and result<sd3e]

print('{}% of data lies within 1 sd'.format(len(sd1list)*100/len(rs)))
print('{}% of data lies within 2 sd'.format(len(sd2list)*100/len(rs)))
print('{}% of data lies within 3 sd'.format(len(sd3list)*100/len(rs)))