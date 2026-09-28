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

        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]
            max_profit = max(sell_price - buy_price, max_profit)
            if buy_price > sell_price:
                left = right
                right = right + 1
            else:
                right = right + 1
        return max_profit








