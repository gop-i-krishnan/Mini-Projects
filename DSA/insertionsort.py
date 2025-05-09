def my_array():
    my_array = []
    n=int(input("Enter the number of elements for array: "))
    
    for i in range(n):
        element=int(input(f"Enter the element at {i+1} : "))
        my_array.append(element)
        print(f"Your array is: {my_array}")
    return my_array


def insertionsort(my_array):
    n=len(my_array)
    for i in range(1,n):
        insert_index=i
        current_value=my_array.pop(i)
        for j in range(i-1,-1,-1):
            if my_array[j]>current_value:
                insert_index=j
        my_array.insert(insert_index,current_value)
    return my_array
        
def main():
    print("WELCOME TO SELECTION SORT PROGRAM!!!")
    array=my_array()
    print(f"Original array:{array}")
    sorted_array=insertionsort(array)
    print(f"Sorted array: {sorted_array}")
    

if __name__ == "__main__":
    main()