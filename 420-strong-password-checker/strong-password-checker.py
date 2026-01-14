import itertools

class Solution:
    low = set('abcdefghijklmnopqrstuvwxyz')
    up = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    
    def strongPasswordChecker(self, s: str) -> int:
        c = set(s)
        
        needs_low = not (c & self.low)
        needs_up = not (c & self.up)
        needs_digit = not (c & self.digit)
        replaces = int(needs_low + needs_up + needs_digit)
        
        inserts = max(0, 6 - len(s))
        deletes = max(0, len(s) - 20)
        
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(deletes):
            apply_best_delete()
        

        group_replaces = sum(
            group // 3
            for group in groups
        )
        
        return (

            deletes
            + max(
                replaces,
                group_replaces,
                inserts,
            )
        )
        