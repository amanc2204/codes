import QueueLinkedList as queue
class Create_tree():
    def __init__(self,Data):
        self.data=Data
        self.left_child=None
        self.right_child=None
newBt=Create_tree('Drinks')               #initialize root
left_child=Create_tree('Hot')
tea=Create_tree('tea')
coffee=Create_tree('coffee')
right_child=Create_tree('cold')
fanta=Create_tree('fanta')
mazza=Create_tree('mazza')
newBt.left_child=left_child
left_child.left_child=tea
left_child.right_child=coffee
newBt.right_child=right_child
right_child.left_child=fanta
right_child.right_child=mazza
############################################PRE ORDER TRAVERSAL
def preorder(root_node):
    if not root_node:                               #O(1)
        return
    print(root_node.data)                           #O(1)
    preorder(root_node.left_child)                  #O(n/2)
    preorder(root_node.right_child)                 #O(n/2)
print(preorder(newBt))



########################################### INORDER TRAVERSAL
def inorder(root_node):
    if not root_node:                               #O(1)
        return
    inorder(root_node.left_child)
    print(root_node.data)
    inorder(root_node.right_child)
inorder(newBt)
########################################### POSTORDER TRAVERSAL
def postorder(root_node):
    if not root_node:                               #O(1)
        return
    postorder(root_node.left_child)
    postorder(root_node.right_child)
    print(root_node.data)
postorder(newBt)
###########################################LEVEL ORDER TRAVERSAL
def levelorder(root_node):
    if not root_node:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if(root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            if(root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)

levelorder(newBt)

