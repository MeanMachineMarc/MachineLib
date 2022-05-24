import MachineLib as L

while True:
    num = input("Enter number: ")
    figures = input("Enter number of significant figures: ")
    print(L.round_xsf(num,figures))
