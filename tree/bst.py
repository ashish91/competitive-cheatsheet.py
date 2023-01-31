class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

class BST:
  def __init__(self):
    self.root = None

  def insert(self, root, val):
    if not self.root:
      self.root = Node(val)
      return self.root

    if not root:
      root = Node(val)
    elif val < root.val:
      root.left = self.insert(root.left, val)
    elif val >= root.val:
      root.right = self.insert(root.right, val)

    return root

  def search(self, root, val):
    if not self.root:
      return None

    if not root:
      return None
    elif val < root.val:
      return self.search(root.left, val)
    elif val > root.val:
      return self.search(root.right, val)
    elif val == root.val:
      return True

  def delete(self, root, val):
    if not self.root:
      return None

    if not root:
      return None
    elif val < root.val:
      root.left = self.delete(root.left, val)
    elif val > root.val:
      root.right = self.delete(root.right, val)
    elif val == root.val:
      if not root.left and not root.right:
        return None
      elif root.right and not root.left:
        return root.right
      elif root.left and not root.right:
        return root.left
      else:
        inorder_succ = root.right
        while inorder_succ.left:
          inorder_succ = temp.left

        root.val = inorder_succ.val
        root.right = self.delete(root.right, inorder_succ.val)

    return root
