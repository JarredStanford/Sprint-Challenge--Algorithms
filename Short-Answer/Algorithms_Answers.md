#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(2n) which reduces down to 0(n).

The complexity doesn't grow with the size of the input. There are always two operations performed for each time through the function. First, the while loop performs its check and then the equation is performed. n3/n2 = n. So n requires n passes through the function to fulfill the while loop.


b) o(n log n)

    The inner loop has comoplexity O(log n) since the j is doubling itself each time instead of incrementing normally. This means less passes are required as n grows. The outer loop runs n times.

c) O(n)

     The recursive function is called N times (n is reduced by 1 each time until base case.)

## Exercise II

If the amount of floors is equal to 0, then the minimum number of attempts is 0. If the amount of floors is 1, the minimum number is 1. Using this, we can employ a recursive solution that reduces down to the base case.

We can cache our result for each floor so we only run the function once. If the egg breaks, we lose 1 egg and move down 1 floor. If the egg does not break, we can move up floors equal to the amount of eggs that we have + 1.

Start at floor x + 1 where x is the number of eggs we have. The time complexity is o(n)?

3 eggs, 14 floors.
 Start at floor 4, drop egg. Breaks = floor 3 Survives = floor 8.
