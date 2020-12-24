"""
CE_Computational_Project

Important Variable List:(Ones not included are not important in the overall outlook of the project)
    LengthOfBeam 
    SupportPositionCoordinates[]
    NumberOfForces
    NumberOfSupports
    ForcesActing[]
    ReactionForces[] 
    SumOfForces
    MomentOfForces - (from origin)
    
    Using the equation : [Coeff][Resultant] = [EqConstant]
    [Resultant] = [CoeffInverse]*[EqConstant]
"""
# importing numpy(not now but can be considered with expansion of project)
import numpy as np

# Initial instructions & guidelines
print(
    "NOTE : The origin of the axis is taken at the left end of the beam and all the distances are measured from the origin. \n For the load acting on the beam, downwards direction is considered positive."
)

# Input length of beam
LengthOfBeam = int(input("Enter the length of the beam : "))

# Input number of supports
NumberOfSupports = int(input("Enter the number of supports(1 or 2):"))

if NumberOfSupports == 1:

    # No. of Forces Acting
    NumberOfForces = int(input("Enter the number of forces acting on the beam : "))

    # List Containing The coordinate and magnitude of acting forces respectively (2-D)
    ForcesActing = []

    for i in range(NumberOfForces):
        # input of coordinate and magnitude of force acting
        ForcesActingInput = input(
            "Enter the value of coordinate and force acting on the bar respectively (with a space in between each values) : "
        )
        # converting the string of input into list with 2 items - coordinate & magnitude of force
        ForcesActingInputList = ForcesActingInput.split(" ")
        # Updating the list ForcesActing with recent input
        ForcesActing.append(
            (float(ForcesActingInputList[0]), float(ForcesActingInputList[1]))
        )

    # Initializing variable SumOfForces and calculating it
    SumOfForces = 0.0
    for i in range(0, len(ForcesActing)):
        SumOfForces = SumOfForces + ForcesActing[i][1]

    print(SumOfForces)

elif NumberOfSupports == 2:
    # Input Coordinates of Support
    SupportPositionInput = input(
        "Enter the coordinates of the 2 support positions(Single Spacing between the two inputs) : "
    )

    # Converting String of Coordinates into List
    SupportPositionCoordinates = SupportPositionInput.split(" ")

    # Converting data type from string to float in List
    for i in range(0, len(SupportPositionCoordinates)):
        SupportPositionCoordinates[i] = float(SupportPositionCoordinates[i])

    # No. of Forces Acting
    NumberOfForces = int(input("Enter the number of forces acting on the beam : "))

    # List Containing The coordinate and magnitude of acting forces respectively (2-D)
    ForcesActing = []

    for i in range(NumberOfForces):
        # input of coordinate and magnitude of force acting
        ForcesActingInput = input(
            "Enter the value of coordinate and force acting on the bar respectively (with a space in between each values) : "
        )
        # converting the string of input into list with 2 items - coordinate & magnitude of force
        ForcesActingInputList = ForcesActingInput.split(" ")
        # Updating the list ForcesActing with recent input
        ForcesActing.append(
            (float(ForcesActingInputList[0]), float(ForcesActingInputList[1]))
        )
        
        
    # Initializing variable SumOfForces and calculating it
    SumOfForces = 0.0
    for i in range(0, len(ForcesActing)):
        SumOfForces = SumOfForces + ForcesActing[i][1]
        
# Initializing and calculating moment of forces from the origin
    MomentOfForces = 0.0
    for i in range(0, len(ForcesActing)):
        MomentOfForces = MomentOfForces + ForcesActing[i][0] * ForcesActing[i][1]        
    
    print(SumOfForces)
    print(MomentOfForces)
    #SumOfMoments = MomentOfForces + SumOfConstantMoments    
    c1 = 0.0
    c2 = 0.0
    d1 = 0.0
    d2 = 0.0     

    
    #If the unknowns are forces :
    c1 = 1
    c2 = 1
    
    d1 = SupportPositionCoordinates[0]
    d2 = SupportPositionCoordinates[1]
    
    Coeff = np.array([[c1, c2],[d1, d2]])
    print(Coeff)
    EqConstant = np.array([[SumOfForces], [MomentOfForces]])
    # Initializing list of the Reaction Forces
    #ReactionForces = []
    CoeffInverse = np.linalg.inv(Coeff)
    print(CoeffInverse)
    Resultant = np.dot(CoeffInverse,EqConstant)
    
    
    print(Resultant[0])
    print(Resultant[1])













    
'''
    # Calculating Reaction Force for support 1
    ReactionForce1 = (MomentOfForces - SupportPositionCoordinates[1] * SumOfForces) / (
        SupportPositionCoordinates[0] - SupportPositionCoordinates[1]
    )

    # Initializing list of the Reaction Forces
    ReactionForces = []

    # Updating the Reaction Forces list with both the reaction forces
    ReactionForces.append(ReactionForce1)
    ReactionForces.append((SumOfForces - ReactionForce1))
    # Test Run
    

else:
    print("Error")
'''