#include <string.h>
#include <ctype.h>

int myAtoi(char * s){
    int length = strlen(s);
    int flag = 0;
    int i;
    char c;
    for(i = 0; i < length; i++) {
        c = s[i];
        if(c != ' ') {
            if(isdigit(c) || c == 45 || c == 43) {
                if(c == 43)
                    i++;
                if(c == 45) {
                    flag = 1;
                    i++;
                }
                break;
            }
            else
                return 0;
        }
    }
    while(i < length && s[i] == '0')
        i++;
    
    int j = i;
    while(j < length){
        if(isdigit(s[j]))
            j++;
        else
            break;
    }
    j--;
    long count = 0;
    
    if(j - i > 9){
        if(flag)
            return INT_MIN;
        else
            return INT_MAX;
    }
    
    for(;i <= j; i++) {
        count *= 10;
        count += s[i] - 48;
    }
    
    if(flag) {
        printf("hi\n");
        count *= -1;
    }

    if(count > (long)INT_MAX)
        return INT_MAX;
    
    else if(count< (long)INT_MIN)
        return INT_MIN;
    

    
    return count;

}