def find132pattern(nums):
    s3 = -10000
    st = []
    for i in range(len(nums)-1,-1,-1):
        if nums[i] < s3:
            return True
        else:
            while st and nums[i] > st[-1]:
                s3 = st[-1]
                st.pop()
        st.append(nums[i])
    return False
find132pattern([4,9,0,2,1,10])
