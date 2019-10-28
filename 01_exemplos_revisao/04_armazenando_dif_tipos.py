x,y,z=43,44,45
s='spam'
d={'a':1,'b':2}
l=[1,2,3]
arq=open('datafile.txt','w')
arq.write(s+'\n')
arq.write('{}, {}, {} \n'.format(x, y, z)) # using python3 pattern
arq.write(str(l)+'$'+str(d)+'\n')
arq.close()
