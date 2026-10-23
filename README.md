# Day 40 - Tree Validation: Validate Binary Search Tree

## Problem Statement
A kingdom archive stores records in a Binary Search Tree (BST).
Corrupted records may violate the BST ordering rules.

Implement a validator that determines whether a binary tree
is a valid BST.

## BST Rules
- Every value in the left subtree must be smaller than its node.
- Every value in the right subtree must be greater than its node.
- All descendants must respect the limits imposed by their ancestors.
- Duplicate values are not allowed.
- An empty tree is considered valid.

## Approach: Range-Based DFS
1. Start at the root with no lower or upper bound.
2. Check whether the current value lies strictly within its range.
3. Traverse the left subtree with the current value as the upper bound.
4. Traverse the right subtree with the current value as the lower bound.
5. Return False immediately if a node violates its range.
6. Return True if all nodes pass validation.

## Example

Valid BST:
        8
       / \
      3   10
     / \    \
    1   6    14

Output: VALID

Invalid BST:
        8
       / \
      3   10
     / \
    1   9

Output: INVALID

Explanation: Node 9 is in the left subtree of 8,
so it must be smaller than 8.

## Test Cases
- Valid BST
- Invalid ancestor violation
- Duplicate value
- Empty tree
- Single-node tree
- Right-skewed valid BST

## Complexity Analysis
- Time Complexity: O(n)
- Auxiliary Space: O(h)
- n = number of nodes
- h = height of the tree

## Real-World Applications
- Database index validation
- Search tree integrity checks
- Data structure testing
- Ordered record management

## Run the Program
python day40_validate_bst.py
