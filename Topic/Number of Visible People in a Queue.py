def canSeePersonsCount(self, heights):
    heights = [1000000] + heights
    ans = [0] * len(heights)
    stack = []
    minus = [0,0]
    left = 0
    right = left + 1
    while right < len(heights):
        if heights[left] > heights[right]:
            stack.append(left)
            left = right
            right = left + 1

            minus[-2] += 1
            minus.append(0)

        else:
            ans[left] = right - left - minus[-1]
            left = stack.pop()
            minus[-1] = minus[-2] + minus.pop()
    right = len(heights) - 1
    left = stack.pop()
    minus.pop()
    while stack:
        ans[left] = right - left - minus[-1]
        left = stack.pop()
        minus[-1] = minus[-2] + minus.pop()
    return ans[1:]

print(canSeePersonsCount(0,[4,3,2,1]))