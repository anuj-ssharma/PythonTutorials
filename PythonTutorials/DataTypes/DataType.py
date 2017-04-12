'''
Created on 10-Apr-2017

@author: anuj_
'''
#lists

list1 = [1,2,4,4,'a']
print list1

#Tuples are similar to lists but immutable

videoData = tuple(["SPSE Introduction",25,100,3])
videoTitle,runningTime,upVotes,downVotes = videoData
print videoTitle
print runningTime


#Sets - unordered collection of unique objects - Use this when you want to play around with the unique values

set1 = set(list1)
print set1

#Dictionary - unordered key value pair
# Values can change

myBio = {'name':'Anuj','age':27,'hobby':'hacking'}

#for key in myBio:
    #print key


#print myBio.keys()
#print myBio.values()
print myBio.items()
for t in myBio.items():
  print t