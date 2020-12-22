bool isPalindrome(int x){
    //base cases: x < 0, x has 1 digit, x has 2 digits
    if(x < 0)
        return false;
    
    else if(x < 10)
        return true;
    
    else if(x < 100) {
        if(x % 10 == x / 10)
            return true;
        else
            return false;
    }
    
    // for x with 3 or more digits
    else {
        int xc = x;
        long y = 0;
        while(xc > 9) {
            y = y + xc % 10;
            y *= 10;
            xc /= 10;
        }
        y += xc;
        
        return (y == x);   
    }
}