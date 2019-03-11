from stacks import Stack

def par_checker(string):
	st=Stack()
	flag=True
	i=0
	while i<len(string) and flag:
		ch=string[i]
		if(ch=="("):
			st.push(ch)
		else:
			if st.is_empty():
				flag=False
			else:
				st.pop()
		i=i+1
	if flag and st.is_empty():
		return True
	else:
		return False

print(par_checker("((()))"))
print(par_checker("(()))"))