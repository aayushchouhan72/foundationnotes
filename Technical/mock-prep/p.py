import sys

lst = []
base_size = sys.getsizeof([])  # Base object overhead (56 bytes on 64-bit CPython)
pointer_size = 8               # 8 bytes per pointer on 64-bit systems

for i in range(15):
    lst.append(i)
    current_bytes = sys.getsizeof(lst)
    capacity = (current_bytes - base_size) // pointer_size
    print(f"len={len(lst):2d} | bytes={current_bytes:3d} | capacity={capacity:2d}")