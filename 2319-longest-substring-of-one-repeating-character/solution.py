class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s)
        
        # Segment tree nodes store: 
        # (max_len, pref_len, suff_len, left_char, right_char)
        tree = [None] * (4 * n)

        def merge(left, right, len_l, len_r):
            m1, p1, s1, lc1, rc1 = left
            m2, p2, s2, lc2, rc2 = right

            lc, rc = lc1, rc2
            
            # Extend prefix length if entire left segment is uniform and matches right prefix
            p = p1 + (p2 if p1 == len_l and rc1 == lc2 else 0)
            
            # Extend suffix length if entire right segment is uniform and matches left suffix
            s = s2 + (s1 if s2 == len_r and rc1 == lc2 else 0)
            
            # Maximum repeating substring length
            m = max(m1, m2)
            if rc1 == lc2:
                m = max(m, s1 + p2)

            return (m, p, s, lc, rc)

        def build(node, l, r):
            if l == r:
                c = s_list[l]
                tree[node] = (1, 1, 1, c, c)
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - l + 1, r - mid)

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (1, 1, 1, ch, ch)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - l + 1, r - mid)

        build(1, 0, n - 1)

        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != ch:
                s_list[idx] = ch
                update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][0])

        return ans
