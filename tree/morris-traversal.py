def morris_traversal(root):
  node = root

  while node:
    if node.left is None:
      print(node.val)
      node = node.right
    else:
      inorder_pred = node.left
      while inorder_pred.right is not None and inorder_pred != node:
        inorder_pred = inorder_pred.right

      if inorder_pred.right is None:
        inorder_pred.right = node
      else:
        inorder_pred.right = None
        print(node.val)
        node = node.right

