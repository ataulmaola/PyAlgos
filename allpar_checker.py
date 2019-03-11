from stacks import Stack

def par_checker(string):
	st=Stack()
	flag=True
	i=0
	while i<len(string) and flag:
		ch=string[i]
		if(ch in "([{"):
			st.push(ch)
		else:
			if st.is_empty():
				flag=False
			else:
				top=st.pop()
				if not equal(top,ch):
					flag=False
		i=i+1
	if flag and st.is_empty():
		return True
	else:
		return False

def equal(x,y):
	begin="([{"
	end=")]}"
	return begin.index(x)==end.index(y)

print(par_checker("{{[()]}}"))
print(par_checker("{{[()]"))