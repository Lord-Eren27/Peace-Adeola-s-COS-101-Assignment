n = int(input("Enter the number of terms: "))
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    print("Invalid range!")
else:
    for i in range(end, start, -1):
        print(i)