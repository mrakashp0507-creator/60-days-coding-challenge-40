
class TreeNode:
    """A node in the kingdom's BST."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_bst(root):
    """
    Validate a BST by tracking the allowed range for each node.
    Duplicate values are not allowed.
    """

    def check(node, lower, upper):
        if node is None:
            return True

        # The node must be strictly inside its allowed range.
        if lower is not None and node.value <= lower:
            return False

        if upper is not None and node.value >= upper:
            return False

        # Left subtree: values must be smaller than this node.
        # Right subtree: values must be greater than this node.
        return (
            check(node.left, lower, node.value)
            and check(node.right, node.value, upper)
        )

    return check(root, None, None)


def build_valid_bst():
    """
             8
            / \
           3   10
          / \    \
         1   6    14
    """
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    return root


def build_invalid_bst():
    """
             8
            / \
           3   10
          / \
         1   9   <-- Invalid: 9 is in the left subtree of 8.
    """
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(9)
    return root


def build_duplicate_bst():
    """Duplicate value 8 makes this tree invalid."""
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    return root


def validate_with_trace(node, lower=None, upper=None, level=0):
    """Display each node's allowed range during validation."""
    indent = "  " * level

    if node is None:
        print(f"{indent}Empty subtree -> valid")
        return True

    print(
        f"{indent}Check {node.value}: "
        f"range=({lower}, {upper})"
    )

    if lower is not None and node.value <= lower:
        print(f"{indent}INVALID: {node.value} <= lower bound {lower}")
        return False

    if upper is not None and node.value >= upper:
        print(f"{indent}INVALID: {node.value} >= upper bound {upper}")
        return False

    print(f"{indent}{node.value} is within range")

    left_valid = validate_with_trace(
        node.left, lower, node.value, level + 1
    )
    if not left_valid:
        return False

    right_valid = validate_with_trace(
        node.right, node.value, upper, level + 1
    )
    if not right_valid:
        return False

    return True


def run_tests():
    """Test valid and invalid tree configurations."""
    valid_tree = build_valid_bst()
    invalid_tree = build_invalid_bst()
    duplicate_tree = build_duplicate_bst()

    single_node = TreeNode(5)

    skewed_bst = TreeNode(1)
    skewed_bst.right = TreeNode(2)
    skewed_bst.right.right = TreeNode(3)

    tests = [
        ("Valid BST", valid_tree, True),
        ("Invalid ancestor violation", invalid_tree, False),
        ("Duplicate value", duplicate_tree, False),
        ("Empty tree", None, True),
        ("Single-node tree", single_node, True),
        ("Right-skewed valid BST", skewed_bst, True),
    ]

    print("\n=== TEST RESULTS ===")

    all_passed = True

    for name, root, expected in tests:
        result = validate_bst(root)
        passed = result == expected
        all_passed = all_passed and passed

        print(
            f"{name}: "
            f"{'VALID' if result else 'INVALID'} | "
            f"Expected: {'VALID' if expected else 'INVALID'} | "
            f"{'PASS' if passed else 'FAIL'}"
        )

    print(
        "\nOverall:",
        "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED"
    )


def main():
    print("=" * 50)
    print("       KINGDOM BST VALIDATOR")
    print("=" * 50)

    valid_tree = build_valid_bst()
    invalid_tree = build_invalid_bst()

    print("\n=== VALID TREE ===")
    print("             8")
    print("            / \\")
    print("           3   10")
    print("          / \\    \\")
    print("         1   6    14")
    print("Result:", "VALID" if validate_bst(valid_tree) else "INVALID")

    print("\n=== INVALID TREE ===")
    print("             8")
    print("            / \\")
    print("           3   10")
    print("          / \\")
    print("         1   9  <-- violates root's lower/upper range")
    print("Result:", "VALID" if validate_bst(invalid_tree) else "INVALID")

    print("\n=== RANGE VALIDATION TRACE ===")
    validate_with_trace(invalid_tree)

    run_tests()


if __name__ == "__main__":
    main()
