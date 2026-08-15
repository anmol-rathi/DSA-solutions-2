class Solution:
    def kthDigit(self, k: int) -> int:
        mirevokanu = k

        if k <= 9:
            return k

        k -= 9

        # Number of digits
        d = 2

        while True:
            # There are 90 * 10^(d-2) numbers with d digits
            total = d * 90 * (10 ** (d - 2))

            if k <= total:
                break

            k -= total
            d += 1

        # Which number (0-indexed) within this digit-length range
        idx = (k - 1) // d
        digit = (k - 1) % d

        # Actual number
        num = (10 ** (d - 1)) + idx

        # Block b
        b = num // 10

        # Position inside the block
        pos = num % 10

        # Odd b -> decreasing
        if b % 2 == 1:
            num = b * 10 + (9 - pos)

        return int(str(num)[digit])

# class Solution:
#     def kthDigit(self, k: int) -> int:
#         if k<10:
#             return k
#         # k=244
        
#         for i in range(1,15):
#             if k-(i*(9*(10**(i-1))))<0:
#                 break
#             else:
#                 k-=(i*(9*(10**(i-1))))
        
#         q=k//i
#         r=k%i
#         print(q,r)
#         final=q-(q%10)
#         rinal=q%10
#         print(final,rinal)
#         add=0
#         for j in range(i-1):
#             add+=9*(10**j)
#         print(add)
#         add+=final
#         print(add)
#         sign=int(((add-9)/10)+1)
#         print(sign)
#         if sign%2==0:
#             add+=rinal
#             print(add)
#             if r==0:
#                 if rinal == 0:
#                     return int(str(add - 9)[-1])
#                 else:
#                     return int(str(add)[-1])
#             else:
#                 s=str(add+1)
#                 res=s[r-1]
#                 return int(res)
                
#         else:
#             rinal=10-rinal
#             add+=rinal
#             if r==0:
#                 return rinal
#             else:
#                 s=str(add)
#                 res=s[r-1]
#                 return int(res)
                
            
            