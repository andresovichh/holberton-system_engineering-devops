#include <stdio.h>
#include <stdlib.h>

float _pow_recursion(float x, float y)
{
    if (y == 0)
        return (1);
    if (y < 0)
        return (_pow_recursion(x, y + 1) / x);

    return (_pow_recursion(x, y - 1) * x);
}

int main(void)
{
printf("%f", _pow_recursion(2, -4));
}