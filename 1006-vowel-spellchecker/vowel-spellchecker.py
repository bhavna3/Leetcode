class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = {"a", "e", "i", "o", "u"}

        def replace(s):
            out = ""
            for ch in s:
                if ch in vowels:
                    out += "#"
                else:
                    out+= ch
            return out
        
        wordlist_set = set(wordlist)
        wordlist_low = dict()

        for w in wordlist:
            if(w.lower() not in wordlist_low):
                wordlist_low[w.lower()] = w
        
        wordlist_replace = dict()

        for low, original in wordlist_low.items():
            replaced = replace(low)

            if(replaced not in wordlist_replace):
                wordlist_replace[replaced] = original
        
        ans = []

        for q in queries:
            if(q in wordlist_set):
                ans.append(q)
            else:
                query_low = q.lower()
                if(query_low in wordlist_low):
                    ans.append(wordlist_low[query_low])
                else:
                    replaced = replace(query_low)
                    
                    if(replaced in wordlist_replace):
                        ans.append(wordlist_replace[replaced])
                    else:
                        ans.append("")         
        return ans