class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        l = 0
        r = len(arr) - 1
        if not arr or timestamp < arr[l][1]: return ""
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return arr[r][0]