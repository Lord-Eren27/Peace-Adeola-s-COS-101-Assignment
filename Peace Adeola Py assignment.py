print('one')

def calculate_density():
    mass=float(input('what is the value for mass'))
    volume = float(input('what is the value for volume'))
    density = mass / volume
    print('density is', density,)
calculate_density()
print('two')
def calculate_volume():
    length = float(input('what is the value of length '))
    breadth = float(input('what is the value of breadth '))
    height = float(input('what is the value of height'))
    volume = length * breadth * height
    print('volume is ', volume,)
calculate_volume()
print('three')
def calculate_area_of_triangle():
    base=float(input('what is the value of base'))
    height=float(input('what is the value of height'))
    area=(base*height)/2
    print('area is',area)
calculate_area_of_triangle()
print('four')
def calculate_area_of_trapezium():
    a = int(input("Enter a of trapezium ") )
    b = int(input(" Enter b of trapezium "))
    height = int(input(" Enter of height of trapezium "))
    area = ( (1/2) * (a + b ) * height )
    print("area is" , area )
calculate_area_of_trapezium()
print('five')
def calculate_work():
    force=float(input('what is the value of force'))
    displacement=float(input('what is the value of displacement'))
    work= force * displacement
    print('work is',work,'j(joules)')
calculate_work()
