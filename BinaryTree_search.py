class Node:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None

pre_order_answer = ""
in_order_answer = ""
post_order_answer = ""

def solution(s):
    tree = {}
    temp_list = s.split(" ")
    for i in range(int(temp_list[0])):
        temp_root = temp_list[(3 * i) + 1]

        temp_node = Node(temp_root)
        temp_node.left = temp_list[(3 * i) + 2]
        temp_node.right = temp_list[(3 * i) + 3]
        tree[temp_root] = temp_node

    pre_order('A', tree)
    print(pre_order_answer)
    in_order("A", tree)
    print(in_order_answer)
    post_order('A', tree)
    print(post_order_answer)

    return ""


def pre_order(start, tree):
    global pre_order_answer
    pre_order_answer += start
    if tree[start].left != ".":
        pre_order(tree[start].left, tree)
    if tree[start].right != ".":
        pre_order(tree[start].right, tree)

def in_order(start, tree):
    global in_order_answer
    if tree[start].left != ".":
        in_order(tree[start].left, tree)
    in_order_answer += start
    if tree[start].right != ".":
        in_order(tree[start].right, tree)

def post_order(start, tree):
    global post_order_answer
    if tree[start].left != ".":
        post_order(tree[start].left, tree)
    if tree[start].right != ".":
        post_order(tree[start].right, tree)
    post_order_answer += start

print(solution("7 A B C B D . C E F E . . F . G D . . G . ."))