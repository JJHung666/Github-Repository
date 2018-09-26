# def todecimal(binarynum)
n = [int(x) for x in str(1101)]
answer=sum((2**i)*n[-i] for i in range(len(n))[::-1])
print(answer)
# len(n) = how many letters or numbers are in the list
# x = "hello"
# x[1] = e
# x[0] = h
# def a(x)
# for x in range()
# x ==

# binary numbers count in bases of 2 instead of 10
# 0, 01, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, etc



