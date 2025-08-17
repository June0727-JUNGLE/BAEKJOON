#include <stdio.h>
#include <string.h>

int recursion(const char *s, int l, int r, int *cnt){
    (*cnt)++;
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else return recursion(s, l+1, r-1, cnt);
}

int isPalindrome(const char *s, int *cnt){
    return recursion(s, 0, strlen(s)-1, cnt);
}

int main(){
    int T;
    scanf("%d", &T);
    while (T--) {
        char s[1001];
        scanf("%s", &s);
        int cnt = 0;
        int result = isPalindrome(s, &cnt);
        printf("%d %d\n", result, cnt);
    }
    return 0;
}