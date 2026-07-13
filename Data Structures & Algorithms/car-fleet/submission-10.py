class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We need to order based on the position
        pairs = [(p,v) for p,v in zip(position,speed)]
        pairs.sort(key=lambda k: k[0], reverse=True)
        counter = 0
        prev_arrival_time = 0

        for pair in pairs:
            arr_time = (target - pair[0])/pair[1]
            if prev_arrival_time and arr_time <= prev_arrival_time:
                continue
            else:
                counter += 1
                prev_arrival_time = arr_time

        return counter