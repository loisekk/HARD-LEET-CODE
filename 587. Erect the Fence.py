# You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.
# Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if all the trees are enclosed.
# Return the coordinates of trees that are exactly located on the fence perimeter. You may return the answer in any order.

class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(trees) <= 1:
            return trees
        def cross_product(a,b,c):
            return ((b[0] - a[0]) * (c[1] - a[1]) -
                    (b[1] - a[1]) * (c[0] - a[0]))
        trees.sort()
        lower_tree = []
        for i in trees:
            while len(lower_tree) >= 2 and cross_product(lower_tree[-2], lower_tree[-1], i) < 0:
                lower_tree.pop()
            lower_tree.append(i)
        upper_tree = []
        for i in reversed(trees):
            while len(upper_tree) >= 2 and cross_product(upper_tree[-2], upper_tree[-1], i) < 0:
                upper_tree.pop()
            upper_tree.append(i)
        return list(set(map(tuple,lower_tree + upper_tree)))
                