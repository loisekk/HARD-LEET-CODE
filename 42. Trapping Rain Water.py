class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ''' Brute force '''
        # count_block = 0
        # max_val = max(height)
        # max_indexes = []
        # result = []
    
        # def layer_search(height , count_block)
        #     for i in range(len(height) - len(height)):

        #         for j in range(len(height)):
        #             if height[0] == 0 :
        #                 continue
        #             elif height[i] == max(val):
        #                 max_indexes.append(i)

        #             elif len(max_indexes) > 1:
        #                 for i in range(len(max_indexes) - 1):
        #                     first_index = max_indexes[i]
        #                     second_index = max_indexes[i+1]
        #                     sub_array = height[first_index:second_index +1]
        #                     temp = []
        #                     for num in subarray:
        #                         diff = max_val - num
        #                         temp.append(diff)
        #                     result.append(temp)
        #             elif second_max = max(num for num in height if num != max_val):
        #                 for n in range(len(heights)):
        #                     second_indexes.append(i)
        #                 max_index = max_indexes[0]
        #             nearest_index = second_indexes[0]
        #             elif nearest_index < max_index:
        #                 subarray = height[nearest_index : max_index +1]
        #             elif sub_array = height[max_index :nearest_index+1]
        #             temp1 = []
        #         elif height[i-1] == 1 and height[i-1] == 0:
        #             return count_block
        #             break

        '''Fixed indetation error invalid elif got -> 191 / 324 testcases passed using max wall sixe and storing the water inside that currnt loc'''
        # if not height:
        #     return 0

        # total_water = 0

        # # Find highest wall
        # max_val = max(height)

        # # Store indexes of highest wall
        # max_indexes = []
        # for i in range(len(height)):
        #     if height[i] == max_val:
        #         max_indexes.append(i)
        # # CASE 1:
        # # Max appears more than once
        # if len(max_indexes) > 1:
        #     for i in range(len(max_indexes) - 1):
        #         left = max_indexes[i]
        #         right = max_indexes[i + 1]

        #         # Water between same max walls
        #         for j in range(left + 1, right):
        #             trapped = max_val - height[j]
        #             total_water += trapped

        # # CASE 2:
        # # Only one maximum wall
        # else:
        #     max_index = max_indexes[0]
        #     # LEFT SIDE
        #     left_max = 0
        #     for i in range(max_index):
        #         left_max = max(left_max, height[i])
        #         trapped = left_max - height[i]
        #         total_water += trapped

        #     # RIGHT SIDE
        #     right_max = 0

        #     for i in range(len(height) - 1, max_index, -1):
        #         right_max = max(right_max, height[i])
        #         trapped = right_max - height[i]
        #         total_water += trapped

        # return total_water

        '''same approach with boundary and peakcustom'''

        # n = len(height)

        # water = 0

        # for i in range(n):

        #     left_max = height[i]
        #     right_max = height[i]

        #     # LEFT MAX
        #     for j in range(i):
        #         left_max = max(left_max, height[j])

        #     # RIGHT MAX
        #     for j in range(i + 1, n):
        #         right_max = max(right_max, height[j])

        #     # WATER
        #     water += min(left_max, right_max) - height[i]

        # return water
        '''fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'''
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
