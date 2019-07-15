def size(node): 
    if node is None: 
        return 0 
    else: 
        return (size(node.left)+ 1 + size(node.right)) 
