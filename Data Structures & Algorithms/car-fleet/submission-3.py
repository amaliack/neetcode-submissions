class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_arr = []
        for i in range(len(position)):
            pos_speed_arr.append([position[i], speed[i]])
        pos_speed_arr.sort(key=lambda x: x[0])

        for arr in pos_speed_arr:
            pos, speed = arr[0], arr[1]
            default_end = (target - pos) / speed
            arr.append(default_end)

        # intuition: groups are based on top of stack and anything below that has a
        # default time <= to it

        count = 0
        last_time = pos_speed_arr.pop()[2]
        while pos_speed_arr:
            # we pop from stack until we find a default end > the top
            top = pos_speed_arr[-1][2]
            while pos_speed_arr and top <= last_time:
                pos_speed_arr.pop()
                if pos_speed_arr: top = pos_speed_arr[-1][2]
            count += 1
            if pos_speed_arr: last_time = pos_speed_arr.pop()[2]
            else: last_time = None
        return count if last_time is None else count + 1
