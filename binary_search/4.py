# Author: Sakthi Santhosh
# Created on: 15/08/2023
#
# 4 - Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/)
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    nums1_len, nums2_len = len(nums1), len(nums2)

    if nums2_len < nums1_len:
        nums1, nums2 = nums2, nums1
        nums1_len, nums2_len = nums2_len, nums1_len

    left, right = 0, nums1_len - 1
    total_len, merged_half_len = nums1_len + nums2_len, (nums1_len + nums2_len) // 2

    while True:
        mid1 = (left + right) // 2
        mid2 = merged_half_len - mid1 - 2

        nums1_lp = nums1[mid1] if mid1 >= 0 else float("-infinity")
        nums1_rp = nums1[mid1 + 1] if mid1 + 1 < nums1_len else float("infinity")
        nums2_lp = nums2[mid2] if mid2 >= 0 else float("-infinity")
        nums2_rp = nums2[mid2 + 1] if mid2 + 1 < nums2_len else float("infinity")

        if nums1_lp <= nums2_rp and nums2_lp <= nums1_rp:
            if total_len % 2:
                return min(nums1_rp, nums2_rp)
            else:
                return (max(nums1_lp, nums2_lp) + min(nums1_rp, nums2_rp)) / 2
        elif nums1_lp > nums2_rp:
            right = mid1 - 1
        else:
            left = mid1 + 1

if __name__ == "__main__":
    print(find_median_sorted_arrays([], []))
