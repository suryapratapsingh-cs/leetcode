class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si = pi = 0
        star_pi = star_si = -1          # last '*' bookmark

        while si < len(s):
            if pi < len(p) and (p[pi] == '?' or p[pi] == s[si]):
                si += 1; pi += 1        # normal match / '?' match

            elif pi < len(p) and p[pi] == '*':
                star_pi = pi            # bookmark '*' position
                star_si = si            # bookmark s position
                pi += 1                 # try '*' = empty first

            elif star_pi != -1:         # mismatch but have a prior '*'
                star_si += 1            # '*' absorbs one more char
                si = star_si
                pi = star_pi + 1        # retry from just after '*'

            else:
                return False            # no '*' to fall back on

        # consume trailing '*'s in pattern
        while pi < len(p) and p[pi] == '*':
            pi += 1

        return pi == len(p)
