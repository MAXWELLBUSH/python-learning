"""
Let’s say you have two Python files:
 file1.py
print("This is file1")

if __name__ == "__main__":
    print("file1 is running directly")

and file2.py
import file1
print("This is file2")

 You run file1.py directly:
This is file1
file1 is running directly

__name__ becomes "__main__"
So that line runs.

You run file2.py instead:

the output
This is file1
This is file2
Now file1 is imported, not run directly
So __name__ becomes "file1" — not "__main__"
That special line does not run.

if __name__ == "__main__":
    print("Run this only if this file is the one being executed directly")
"""