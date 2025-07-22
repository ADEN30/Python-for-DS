import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    reshaped_array2d = None
    try:
        array2d = np.array(family)
        print(f"My shape is: {array2d.shape}")
        reshaped_array2d = array2d[start:end:, ::]
        print(f"My new shape is: {reshaped_array2d.shape}")
        return reshaped_array2d.tolist()
    except Exception as e:
        print(e)
    
    
    
    
family = [[1.80, 78.4, 7],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]


print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))