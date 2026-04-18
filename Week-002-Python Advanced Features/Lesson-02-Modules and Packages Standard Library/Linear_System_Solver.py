import numpy as np
def solve_linear_system(A, b):
    try:
        # Solve the linear system Ax = b
        X = np.linalg.solve(A, b)
        labels=['s', 't', 'u', 'v', 'w', 'x', 'y']
        print("Solution:")
        for label, value in zip(labels, X):
            print(f"{label} = {value:.4f}")
        return X
    except np.linalg.LinAlgError as e:
        print("Error solving linear system:","Singular matrix", e)
        return None
if __name__ == "__main__":
    # Tənlikdə olan matris A və vektor b
    A=np.array([[2,-7,3,5,-7,11,8],[5,7,-1,9,-6,3,-5],[13,11,8,7,4,2,1],[12,1,6,5,9,3,11],[1,-4,7,-3,9,-2,6],[4,1,-6,-3,8,-7,-4],[-7,-2,5,1,9,3,-4]])
    b=np.array([114,-11,-25,-37,4,-91,-50])
    solve_linear_system(A, b)


# Outpust Real Results:
# Solution:
# s = 4.999999999999996
# t = -6.999999999999995
# u = 8.0
# v = -6.000000000000003
# w = -9.0
# x = 2.0000000000000053
# y = -2.999999999999998

#outputs Round priced Results:
# Solution:
# s = 5.0000
# t = -7.0000
# u = 8.0000
# v = -6.0000
# w = -9.0000
# x = 2.0000
# y = -3.0000