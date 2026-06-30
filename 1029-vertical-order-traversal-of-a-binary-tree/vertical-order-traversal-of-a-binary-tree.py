from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(lambda: defaultdict(list))
        q = deque()
        sol = []

        q.append((root, 0, 0))

        while q:
            node, col, row = q.popleft()

            dic[col][row].append(node.val)

            if node.left:
                q.append((node.left, col - 1, row + 1))

            if node.right:
                q.append((node.right, col + 1, row + 1))

        for col in sorted(dic.keys()):
            ans = []

            for row in sorted(dic[col].keys()):
                ans.extend(sorted(dic[col][row]))

            sol.append(ans)

        return sol