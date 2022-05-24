import MachineLib

while True:
    num = input("Enter number: ")
    figures = input("Enter number of significant figures: ")
    print(MachineLib.round_xsf(num,figures))
