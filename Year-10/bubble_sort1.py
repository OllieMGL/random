nums = [7, 5, 9, 10, 8, 32, 4, 456764, 45, 357, 3565, 46, 56]
print(nums)
print("")
unsorted = True
while unsorted == True:
    unsorted = False
    for pos in range(len(nums)-1):
        currentItem = nums[pos]
        nextItem = nums[pos+1]
        if currentItem > nextItem:
            nums[pos] = nextItem
            nums[pos+1] = currentItem
            unsorted = True
            print(nums)