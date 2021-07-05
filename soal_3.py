'''
AREA OF TRIANGLE
    { Calculate the area of triangle}
DICTIONARY
    base, height: integer/float
FUNCTION
    triangle_area(base, height)
DESCRIPTION
    triangle_area(base, height) {
        return 1/2 * Base * Height
    }
'''
def triangle_area(base, height):
    return 1/2*base*height
print(triangle_area(float(input()), float(input())))