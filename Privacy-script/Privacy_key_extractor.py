bytecode = input("Enter the full constructor bytecode for the Privacy level instance:\n").strip()
length = len(bytecode)
print(f"bytes16 _key is --->    {bytecode[length - 64:length - 32]}")
