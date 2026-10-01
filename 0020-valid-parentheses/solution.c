#include <stdbool.h>
#include <stdlib.h>

bool isValid(char* s) {
    int len = 0;
    while (s[len] != '\0') {
        len++;
    }

    // If the length is odd, it cannot be balanced
    if (len % 2 != 0) {
        return false;
    }

    char* stack = (char*)malloc(sizeof(char) * len);
    int top = -1;

    for (int i = 0; i < len; i++) {
        char c = s[i];

        // Push closing bracket counterparts when an opening bracket is seen
        if (c == '(') {
            stack[++top] = ')';
        } else if (c == '{') {
            stack[++top] = '}';
        } else if (c == '[') {
            stack[++top] = ']';
        } else {
            // If stack is empty or top item does not match current closing bracket
            if (top == -1 || stack[top] != c) {
                free(stack);
                return false;
            }
            top--;
        }
    }

    bool result = (top == -1);
    free(stack);
    return result;
}
