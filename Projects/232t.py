
def f1(s,c):
    s = "hello world";
    cnt = 0;
    for var in s:          
	if (isdigit(var)):
	    cnt++
	else if (var == c):
	    s += c
    print(s.size())
    return cnt
