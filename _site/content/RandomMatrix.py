import numpy as np

def Generate_GOE(n):
    """Creates nxn GOE"""
    A = np.random.normal(size=[n,n])
    G = (A+A.T)/2
    return G

def Generate_GUE(n):
    """Creates nxn GUE"""
    i = complex(0,1)
    Lambda_real = np.random.normal(size=[n,n])
    Lambda_im = np.random.normal(size=[n,n])
    Lambda = Lambda_real + Lambda_im * i
    G = (Lambda+Lambda.T.conjugate())/2
    return G

def Generate_Ginibre(n):
    """Creates nxn Ginibre matrix"""
    G_real = np.random.normal(scale= np.sqrt(1/(2*n)), size=[n,n])
    G_im = np.random.normal(scale= np.sqrt(1/(2*n)), size=[n,n]) * complex(0,1)
    G = G_real + G_im
    return G

def Generate_Custom(f, n, m):
    """Create a nxm matrix A such that A_ij = f(i,j)"""
    return np.fromfunction(np.vectorize(f, otypes=[float]), (n,m))