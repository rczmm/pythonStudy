from collections import Counter


class Solution(object):

    # 下一个排列
    def find_substring(self, s: str, words: list) -> list:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        words_map = Counter(words)  # 统计 words 中每个单词的频率
        result = []

        # 遍历 s 的每个可能起点
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            count = 0  # 当前窗口中匹配的单词数量

            while right + word_len <= len(s):
                # 从 s 中取出一个单词
                word = s[right:right + word_len]
                right += word_len

                if word in words_map:
                    seen[word] += 1
                    count += 1

                    # 如果某个单词频率超过了 words 中的频率，收缩窗口
                    while seen[word] > words_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # 如果窗口中的单词匹配上了 words 的所有单词
                    if count == word_count:
                        result.append(left)
                else:
                    # 如果当前单词不在 words 中，重置窗口
                    seen.clear()
                    count = 0
                    left = right

        return result

    # 最长有效括号
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n  # dp[i] 表示以 i 结尾的最长有效括号长度
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if i - dp[i - 1] >= 2 else dp[i - 1] + 2
                max_len = max(max_len, dp[i])

        return max_len

    # 搜索插入位置
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判断左段是否有序
            if nums[left] <= nums[mid]:
                # 如果目标值在左段范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 如果目标值在右段范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def searchRange(nums: list[int], target: int) -> list[int]:
        def findLeftBoundary(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRightBoundary(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = findLeftBoundary(nums, target)
        right = findRightBoundary(nums, target)

        # 检查目标值是否存在
        if left <= right and 0 <= left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    length = solution.longestValidParentheses("(()")
    print(length)
