# coding:utf-8
import json
import numpy as np
import matplotlib.pyplot as plt

a = [json.loads(line) for line in open('data.txt')]
b = []
iphone = 0
android = 0
for i in a:
    for k in i['comments']:
        if u'iPhone' in k['userClientShow']:
            iphone += 1
        elif u'Android' in k['userClientShow']:
            android += 1

b = [iphone, android]
                
        
plt.rc('font', family='STXihei', size=9)
a=np.array([1,2])
plt.bar([1,2],b,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('x')
plt.ylabel('y')
plt.title('用户手机型号')
plt.legend(['用户手机型号'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.xticks(a,('iPhone','Android'))
plt.show()


