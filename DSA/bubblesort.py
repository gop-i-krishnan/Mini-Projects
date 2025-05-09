def array():
    # Initialize an empty list to store array elements
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    
    # Take user input for each element
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))  # Prompt for each element
        arr.append(element)  # Add element to the array
        print(f"Array after entering element {i+1}: {arr}")  # Display the array after each input
    
    return arr

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    print("WELCOME TO BUBBLE SORT PROGRAM!!!")
    
    arr = array()  # Get the array from user input
    print(f"Original Array: {arr}")
    sorted_arr = bubblesort(arr)  # Sort the array
    print(f"SORTED ARRAY: {sorted_arr}")

if __name__ == "__main__":
    main()
