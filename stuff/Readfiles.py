with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
✅ Explanation:
open('example.txt', 'r'): opens the file in read mode.

.read(): reads the entire content as one long string.

with: automatically closes the file after reading.
    
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
✅ Use cases:
Reading logs

Reading saved notes or messages

Reading simple line-by-line data like to-do lists

