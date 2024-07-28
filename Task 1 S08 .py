def sorted(num):
    if len(num) <= 1:
        return True
    
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    
    return True
