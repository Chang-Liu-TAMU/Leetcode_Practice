# @Time: 2022/5/11 17:21
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-355-design-twitter.py

from collections import defaultdict


class Twitter:

    def __init__(self):
        self.d = defaultdict(list)
        self.t = 0
        self.r = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.r:
            self.r[userId].add(userId)
        self.d[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        a = [self.d[x] for x in self.r[userId]]
        b = [len(x) - 1 for x in a]
        while len(h) != 10:
            flag = False
            max_i = None
            m = -1
            ans = None
            for i, j in enumerate(b):
                if j >= 0:
                    flag = True
                    time, val = a[i][j]
                    if time > m:
                        m = time
                        max_i = i
                        ans = val

            if not flag:
                break
            h.append(ans)
            b[max_i] -= 1
            # print(b)
        return h
        # print(self.d)
        # print(self.r)
        # return [x[1] for x in h]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.r:
            self.r[followerId].add(followerId)
        self.r[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.r[followerId]:
            self.r[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)