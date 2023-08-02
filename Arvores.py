                #QUESTAO 21
class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
                
                #QUESTAO 22
    def preorder(self):
        result = []
        result.append(self.value)
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result
    
    
    
            #QUESTAO 23
    def inorder(self):
        result = []
        if self.left:
            result.extend(self.left.inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder())
        return result
    

            #QUESTAO 24
    def postorder(self):
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.value)
        return result
    
    
    
            #QUESTAO26
    def height(self):
        if self.left is None and self.right is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)
    
    
    
            #QUESTAO 27
    def size(self):
        if self is None:
            return 0
        else:
            left_size = self.left.size() if self.left else 0
            right_size = self.right.size() if self.right else 0
            return left_size + right_size + 1