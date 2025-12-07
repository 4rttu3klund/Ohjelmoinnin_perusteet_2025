def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = 0  # index for Left
    j = 0  # index for Right
    k = 0  # index for Merge
    while i < len(PLeft) and j < len(PRight):
        LeftVal = PLeft[i]
        RightVal = PRight[j]
        if PAsc:
            TakeLeft = LeftVal <= RightVal
        else:
            TakeLeft = LeftVal >= RightVal
        if TakeLeft:
            PMerge[k] = LeftVal
            i += 1
        else:
            PMerge[k] = RightVal
            j += 1
        k += 1
    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1
    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    if n <= 1:
        return None
    mid = n // 2
    Left = PValues[:mid]
    Right = PValues[mid:]
    mergeSort(Left, PAsc)
    mergeSort(Right, PAsc)
    merge(Left, Right, PValues, PAsc)
    return None