class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. input constraints --> length and element size <= 100
        2. empty input --> no
        3. positive/negative --> prices can't be negative
        4. duplicates --> doesn't matter (same price two days)
        5. sorted input --> doesn't matter
        6. modify input --> no, the ordering matters
        7. edge cases --> maybe no profit can be made

        brute force --> try every combination of two numbers (with the right order)
        which would take O(n^2)

        invariant:
        - we need earliest + lowest price to buy and most expensive latest to sell
        - min_so_far and max_so_far, while keeping track of max profit thus far
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
            







