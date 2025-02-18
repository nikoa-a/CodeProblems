class MergeSortedArray:

    def merge(self, nums1, m, nums2, n):

        # Third pointer at the end of nums1
        nums1Last = m + n - 1

        while n > 0 and m > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[nums1Last] = nums2[n-1]
                n -= 1
            else:
                nums1[nums1Last] = nums1[m-1]
                m -= 1

            nums1Last -= 1

        # Edge case, fill nums1 with leftovers from nums2
        while n > 0:
            nums1[nums1Last] = nums2[n-1]
            n -= 1
            nums1Last -= 1

        return nums1