class someTree:
    def find_largest_smaller_key(self, num):
        if not self.root:
            return -1

        self.biggest = -1

        def helper(node):
            if not node:
                return

            # 밑에서 말하는 작을떄만 저장해주므로 이것은 필요하지 않다.
            # if self.biggest > -1:
            #     if self.biggest >= num:
            #         return node.parent

            if num <= node.key:
                helper(node.left)
            else:
                #작을때만 저장해주므로
                self.biggest = node.key
                helper(node.right)
            return
        helper(self.root)
        return self.biggest

