class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        mod = 10**9 + 7
        
        # Fast matrix multiplication for m x m matrices
        def mmul(M1, M2):
            res = [[0] * m for _ in range(m)]
            for i in range(m):
                for k in range(m):
                    val = M1[i][k]
                    if not val: 
                        continue
                    M2_k = M2[k]
                    res_i = res[i]
                    for j in range(m):
                        res_i[j] += val * M2_k[j]
                res[i] = [x % mod for x in res[i]]
            return res

        # Base transition blocks
        A = [[1 if j < i else 0 for j in range(m)] for i in range(m)]
        B = [[1 if j > i else 0 for j in range(m)] for i in range(m)]
        
        I = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
        res_X, res_Y, res_diag = I, I, True
        base_X, base_Y, base_diag = A, B, False
        
        # Binary exponentiation for block matrices
        p = n - 1
        while p > 0:
            if p % 2 == 1:
                if res_diag and base_diag:
                    res_X, res_Y, res_diag = mmul(res_X, base_X), mmul(res_Y, base_Y), True
                elif not res_diag and not base_diag:
                    res_X, res_Y, res_diag = mmul(res_X, base_Y), mmul(res_Y, base_X), True
                elif res_diag and not base_diag:
                    res_X, res_Y, res_diag = mmul(res_X, base_X), mmul(res_Y, base_Y), False
                else:
                    res_X, res_Y, res_diag = mmul(res_X, base_Y), mmul(res_Y, base_X), False
            
            if base_diag:
                base_X, base_Y, base_diag = mmul(base_X, base_X), mmul(base_Y, base_Y), True
            else:
                base_X, base_Y, base_diag = mmul(base_X, base_Y), mmul(base_Y, base_X), True
            p //= 2
            
        return (sum(sum(row) for row in res_X) + sum(sum(row) for row in res_Y)) % mod
