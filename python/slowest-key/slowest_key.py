from typing import List


class KeyUtils:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Identifies the key that is pressed for the longest duration.
        """

        releaseTimes.insert(0, 0)
        times = [releaseTimes[i] - releaseTimes[i-1] for i in range(1, len(releaseTimes))]
        key_times = [(k, t) for k, t in zip(keysPressed, times)]
        return sorted(key_times, key=lambda tup: (tup[1], tup[0]))[-1][0]


if __name__ == '__main__':
    obj = KeyUtils()
    print(obj.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed='cbcd'))
