'''
Given a string S and a pattern P, you need to find if S can be generated by using P one or more times.
For each testcase, print "1"(without quotes), if possible, else print "0"(without quotes).
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        pattern , string = input() , input()
        if len(pattern)>len(string):print(0)
        elif len(string)%len(pattern)!=0:print(0)
        elif string[:len(pattern)]!= pattern:print(0)
        else:print(1)