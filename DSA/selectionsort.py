def my_array():
    my_array = []
    n=int(input("Enter the number of elements for array: "))
    
    for i in range(n):
        element=int(input(f"Enter the element at {i+1} : "))
        my_array.append(element)
        print(f"Your array is: {my_array}")
    return my_array


def selectionsort(my_array):
    n=len(my_array)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if my_array[j]<my_array[min_index]:
                min_index=j
        my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
    return my_array
        
def main():
    print("WELCOME TO SELECTION SORT PROGRAM!!!")
    array=my_array()
    print(f"Original array:{array}")
    sorted_array=selectionsort(array)
    print(f"Sorted array: {sorted_array}")
    

if __name__ == "__main__":
    main()