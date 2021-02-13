class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        wealth = 0
        i=0
        while i < n:
            if sum(accounts[i]) > wealth:
                wealth = sum(accounts[i])
            i += 1
        return wealth