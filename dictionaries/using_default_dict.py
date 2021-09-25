from collections import defaultdict
f = defaultdict(dict)
l =list(set(['I', 'do','not', 'like', 'using', 'because', 'because', 'because', 'is', 'normally', 'used', 'for', 'excuses']))
for i in l:
    if i[0].lower() in f:
        f[i[0].lower()].append(i)
    else:
        f[i[0]] = [i]
for i,j in sorted(f.items()):
    print("{}: {},".format(i,j))
    
"""    
 O/P
 --
  {
    b: because,
    d: do,
    e: excuses,
    f: for,
    i: i is,
    l: like,
    n: normally not,
    u: used using
   }
   
"""
"""
#Traditonal approach

l =list(set(['I', 'do','not', 'like', 'using', 'because', 'because', 'because', 'is', 'normally', 'used', 'for', 'excuses']))
l.sort()
d = dict()
q = dict()
p = []
for i in l:
    i = i.lower()
    if i[0] in d.keys():
        l = d[i[0]]
        p.append(l)
        q[l[0]] = l
    d[i[0]] = i
for i, k in d.items():
    if i in q.keys():
        print("{} : {} {},".format(i , q[i], k))
    else:
        print("{} : {},".format(i, k))
"""
