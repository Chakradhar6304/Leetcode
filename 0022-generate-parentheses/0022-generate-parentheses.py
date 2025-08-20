class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(curr, open_count, close_count):
            # If the current string is complete, add to result
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # Add "(" if we still have some left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ")" if it won’t break validity
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
        