/*
slow python version
from numpy import int32
INT_MIN = int32(1<<31)
INT_MAX = int32(~INT_MIN)

x = INT_MAX - 4

if x == INT_MIN or x == INT_MAX:
    print(0) 

flag = 0
if x >> 31 == -1:
    x = (~x) + 1
    flag = 1


if x / 10**9 > 0:
    rev = str(x)
    rev = rev[::-1]
    imax = str(INT_MAX)

    for i in range(9):
        if int(rev[i]) > int(imax[i]):
            print(0)
            quit()
    print(int(rev))
else:
    x = str(x)
    rev = int32(x[::-1])

quit()


for i in range (9, 0, -1):
    print(i)
quit()
# pop operation:
rev = int32(0)
flag = 0


while x > 0:
    pop = int32(x % 10)

    x = int32(x / 10)
    rev = rev*10 + pop

if flag:
    rev = (~rev) + 1

print(rev)
*/
// fast C version
int reverse(int x){
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            
            rev = rev * 10 + pop;
        }
        return rev;
}