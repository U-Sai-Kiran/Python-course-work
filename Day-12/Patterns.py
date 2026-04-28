'''
  0 1 2 3 4
0 * * * * *
1 * * * * *
2 * * * * *
3 * * * * *
4 * * * * *

for row in range(5):
    for col in range(5):
        print('*',end = ' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *

n = int(input("Enter the number: "))
for row in range(n):
    for col in range(row + 1):
        print('*',end = ' ')
    print()

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

n = int(input("Enter the number: "))
for row in range(n):
    for col in range(n-row):
        print('*',end = ' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n = int(input("Enter the number: "))
m=n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print('*',end =' ')
    else:
         for col in range(n-row):
             print('*',end =' ')
    print()

          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
n = int(input("Enter the number: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()

* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          *

n = int(input("enter the number: "))
for row in range(n):
    for col in range(row):
        print(' ',end=' ')
    for spc in range(n-row):
        print('*',end=' ')
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        *
        
n = int(input("enter the number: "))
m=n//2
for row in range(n):
    if row<=m:
        print(' '*(m-row)+'*'*(row+1),end=' ')
    else:
        print(' '*(row-m)+'*'*(n-row),end=' ')
    print()


    *  
   * *  
  * * *  
 * * * *  
* * * * *  
 * * * *  
  * * *  
   * *  
    *
n = int(input("enter the number: "))
m=n//2
for row in range(n):
    if row<=m:
        print(' '*(m-row)+'* '*(row+1),end=' ')
    else:
        print(' '*(row-m)+'* '*(n-row),end=' ')
    print()

01010
10101
01010
10101
01010

n = int(input("enter the number: "))
for row in range(n):
    for col in range(n):
        print(int(row + col) % 2,end = '')
    print()

01010
01010
01010
01010
01010

n = int(input("enter the number: "))
for row in range(n):
    for col in range(n):
        print(col % 2,end = '')
    print()

*****
*   *
*   *
*   *
*****

n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==0 or i==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*****
   * 
  *  
 *   
*****
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or i+j==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*   *
 * * 
  *  
 * * 
*   *

n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i+j==(n-1) or i==j:
             print('*',end='')
        else:
            print(' ',end='')
    print()

*****
*   *
*****
*   *
*   *
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==(n-1) or j==0 or i==(n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*****
*    
*    
*    
*****
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*****
*    
*****
*    
*
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==(n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*****
*    
* ***
* * *
*** *
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==(n-1) and j<=(n//2)) or (j==(n//2) and i>=(n//2)) or i==(n//2) and j>= (n//2) or (j==(n-1) and i>=(n//2)):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*********
    *    
    *    
    *    
*   *    
*   *    
*   *    
*   *    
*****
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j==(n//2) or (i == (n-1) and j <= (n//2)) or (j == 0 and i>=(n//2)):
            print('*',end='')
        else:
            print(' ',end='')
    print()


*                *
 *              * 
  *            *  
   *          *   
    *        *    
     *      *     
      *    *      
       *  *       
        ** 
n = int(input("enter the number: "))
for i in range(n):
    for j in range(2*n):
        if j == i or j == (2*n - i - 1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*       *
*       *
*       *
*       *
*       *
*       *
*       *
*       *
*********

n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == (n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()     

*       *
**     **
* *   * *
*  * *  *
*   *   *
*       *
*       *
*       *
*       *

n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or (i <= (n//2) and (j==i or j == (n-i-1))) or j == n-1 :
            print('*',end='')
        else:
            print(' ',end='')
    print()     

*       *
**      *
* *     *
*  *    *
*   *   *
*    *  *
*     * *
*      **
*       *

n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j==i or j == n-1 :
            print('*',end='')
        else:
            print(' ',end='')
    print() 


*********
    *    
    *    
    *    
    *    
    *    
    *    
    *    
    *  
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j==(n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()

*********
    *    
    *    
    *    
    *    
    *    
    *    
    *    
*********
n = int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j==(n//2) or i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

*       *
*       *
*       *
*       *
*   *   *
*  * *  *
* *   * *
**     **
*       *

n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i >= n//2 and (j == i or j == n-i-1)):
            print('*', end='')
        else:
            print(' ', end='')
    print()


*       *
 *     * 
  *   *  
   * *   
    *    
    *    
    *    
    *    
    *
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if (i<= (n//2) and (j== i or j == n-i-1)) or (i>n//2 and j==n//2):
            print('*', end='')
        else:
            print(' ', end='')
    print()


'''
























































