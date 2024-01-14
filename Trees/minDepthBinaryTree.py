public int minDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        else if (root.left == null){
            return 1+this.minDepth(root.right);
        }
        else if(root.right == null){
            return 1+this.minDepth(root.left);
        }
        else{
            return 1+Math.min(this.minDepth(root.right),this.minDepth(root.left));
        }
    }


# 111. Minimum Depth of Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
