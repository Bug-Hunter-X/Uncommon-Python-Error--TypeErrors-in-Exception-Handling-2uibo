# Uncommon Python Error: TypeErrors in Exception Handling

This repository demonstrates a subtle error that can occur in Python when handling exceptions and performing arithmetic operations. The `function_with_uncommon_error` function aims to safely handle division by zero and type errors; however, it can still encounter unexpected behavior if the input types are not numbers.

**Problem:**

The code is designed to prevent crashes from division by zero and other type errors. However, not all type errors are caught.  The error handling focuses only on explicit exceptions, not implicit errors during operation.  This creates a potential for a silent, unexpected failure, rather than a clear error message.

**Solution:**

The solution file (`bugSolution.py`) enhances error handling by using type checking *before* performing the calculation and raising a more informative custom exception for incompatible types.  This ensures consistent and clear error reporting in all circumstances.

**How to Run:**

1. Clone the repository.
2. Navigate to the repository directory.
3. Run `bug.py` to see the original code's behavior.
4. Run `bugSolution.py` to see the improved solution.
