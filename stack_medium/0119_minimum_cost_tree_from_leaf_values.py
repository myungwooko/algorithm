"""
1130. Minimum Cost Tree From Leaf Values
Medium

397

36

Favorite

Share
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an "in-order traversal"(left=>root=>right *여기서 이건 크기랑 상관없고 arr에서 나타내는 순서가 그렇다는 말) of the tree.
(Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.



Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4


Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
The thought is quite straight forward.


결국은 node들의 합을 구하는 건데 => 작은것에 작은것을 곱할수록 더 작은게 나오니까 => 작은 것끼리 더할수록 더 작은 값이 나오니깐
"작은 것끼리 더할수록 더 작은 값이 나오니깐" 이게 무슨말이냐면 => 12*4 와 6*8 은 모두 48이다. => 하지만 16 > 14 라는 얘기

Greedy python solution
1. Pick up the leaf node with minimum value.
2. Combine it with its inorder neighbor which has smaller value between neighbors.
#3 => 작은것 부터 시작 옆에 붙어있는 것중 더 작은 것과 곱해서 부모 노드 만들고 => 어쨌든 옆동네 더 큰애(앞으로의 일관성상 이해하기 쉽게 왼쪽에 놓는다고 가정)랑 곱할애는 이제 제일 작은걸 버리고 곱하는 대상이 됐던 엘리먼트
      (버린것을 왼쪽 해당을 오른쪽애 놓는다고 생각) => 결론적으론 그렇게 남긴다는게 제일 작은건 곱셈의 대상으로서 끝났으니 버린다는 얘기가 된다. 결국 그들(완전 왼쪽과 두개의 곱이 만들어낸 두개의 부모둘)이 속한 부모는
      큰 대상으로서 곱셈의 대상에서 빠졌던 이전의 아예 왼쪽과, 곱셈 한 것 중 큰것의 product가 되는 거니까.
3. Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
4. Repeat it until there is only one node.

=> 결국 제일 작은거 찾고 거기서 부터 작은 단위의 tree 부터 하나씩 해결해나가는 것이다.
"""
class Solution:
    def mctFromLeafValues(self, arr):
        res = 0
        # 곱하는 값을 더히는 거니까 하나가 되면 모든 해야할 연산을 마쳤다는 얘기가 된다.
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            if 0 < mini_idx < len(arr) - 1:
                #
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
            else:
                res += arr[1 if mini_idx == 0 else mini_idx - 1] * arr[mini_idx]
            arr.pop(mini_idx)
        return res