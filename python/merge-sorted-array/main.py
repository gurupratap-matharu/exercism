class Solution:
    def tester(self, A):
        A.append(5)

if __name__=='__main__':
    nums1 = [1,2,3]
    Solution().tester(nums1)
    print(nums1)
