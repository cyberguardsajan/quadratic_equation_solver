import math

a = float(input("Enter the first coefficient (a): "))
b = float(input("Enter the second coefficient (b): "))
c = float(input("Enter the third coefficient (c): "))

discrim = b**2 - (4 * a * c)

if discrim > 0:
    print("The solutions of this equation are:")
    print((-b + math.sqrt(discrim)) / (2 * a))
    print((-b - math.sqrt(discrim)) / (2 * a))

elif discrim == 0:
    print("The solution of this equation is:")
    print(-b / (2 * a))

else:
    print("No real solutions for this equation.")
