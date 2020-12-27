'''
def recurse(x, s, state, nstates):
	for i in s:
		print("state: %d, s = %s" %(state, s))
		if s == "":
			return 0
		if state == nstates:
			return 0
		if x[state] == '!':
			return (recurse(x, s, state + 1, nstates) or recurse(x, s[1:], state, nstates))
		elif i == x[state] or x[state] == '.':
			if len(s) == 1:
				if state == nstates - 1:
					return 1
				else:
					return 1
			elif len(s):
				return 0

import numpy as np
s = 'dddabdda'
p = '.*.b.*'
x = []
i = 0
length = len(p) - 1
while i < length:
	if(p[i] == '.') and p[i + 1] == '*' :
		x.append('!')
		i += 2
		continue
	else:
		x.append(p[i])
		i += 1

if(p[length] != '*'):
	x.append(p[length])

print(x)
nstates = 1
for i in x:
	if i !='!':
		nstates += 1

vec = np.zeros(nstates)
print(vec)
nfa = {0: [0,0]}
if x[0] == '!':
	nfa[0][0] = 1

# print(nfa)
i, j = 1, 1
length = len(x) - 1
print(x)
print(x[alength])
while i < length:
	if x[i + 1] == '!':
		nfa[j] = [1, x[i]]
		j += 1
		i += 2
	else:
		nfa[j] = [0, x[i]]
		i += 1
		j += 1

if x[length] != '!':
	nfa[nstates-1] = [0, x[length]]
print(nfa)





#while i < nstates - 1:
	#if x[i] == '!':
		

#start false
ret = 0
state = 0
print(recurse(x, s, state, nstates))
'''



# recursion
s = 'ddcabdd'
p = '.d.a..d'

print("Sad!")
print("p = %s" %(p))
print("s = %s" %(s))
f_m = bool(s) and p[0] in {s[0], '.'}

def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])

x = match(s,p)
print("match returned %s"  %(match(s,p)))


