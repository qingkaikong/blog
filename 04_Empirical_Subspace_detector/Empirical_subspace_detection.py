import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from scipy import signal
import os

points = 100
show_ricker = False
show_first_basis_compare = False
show_second_basis_compare = False

#if you want to normalize the signal for comparison
normalize = True

#check if the figures folder exist, if not, create one
directory = './figures/'
if not os.path.exists(directory):
    os.makedirs(directory)

#generate different width of the mexican hat signal to represent different frequency
for k in range(4, 10):
    
    #generate the mexican hat signal
    a = k + 1
    vec2 = signal.ricker(points, a)
    if show_ricker:
        plt.plot(vec2)
        plt.show()

    #generate the simulated P and S wave
    y_list = []
    fig1 = plt.figure(facecolor='white')

    for i in range(10):
        #white noise 
        sig = (np.random.rand(500) - 0.5) * 0.1

        #for P
        z = np.zeros(400)
        P = np.r_[vec2, z]

        #for S
        z1 = np.zeros(200 + 1 * i)
        z2 = np.zeros(200 - 1 * i)
        S = np.r_[z1, 3 * vec2, z2]
        
        #the whole signal
        y = sig + P + S

        ax = fig1.add_subplot(10, 1, i+1)
        ax.plot(y)
        ax.axes.yaxis.set_ticklabels([])

        if i < 9:
            ax.axes.xaxis.set_ticklabels([])
        
        #put the generated signal into a list
        y_list.append(y)

    #save the figures to the figure folder
    fig1.savefig(directory + 'P_S_wave_k_' + str(k+1) + '.png')   
    
    #form the design set
    y_mat = np.matrix(y_list).T
    
    #get the stack of the waveform
    y_stack = y_mat.mean(axis =1)
    
    #Do the SVD
    U,s,V = np.linalg.svd(y_mat, full_matrices=False)

    #check the svd
    #np.allclose(y_mat, U * np.diag(s) * V)

    #get the first two basis
    Sig = np.matrix(np.eye(2)*s[:2])
    #tak out columns you don't need
    basis = U[:,:2] 
    
    #here I just do a quick check to see if the polarity is wrong and flip the signal if I need
    corr_coef, p = pearsonr(y_stack, basis[:, 0])
    if corr_coef < 0:
        basis[:, 0] *= -1
    
    if normalize:
        y_stack /= np.max(np.abs(y_stack))
        basis[:, 0] /= np.max(np.abs(basis[:, 0]))
    
    fig2 = plt.figure()
    
    plt.plot(y_stack, label = 'Stacking')
    plt.plot(basis[:, 0], 'r', label = '1st basis SVD')
    plt.legend()

    if show_first_basis_compare:
        plt.show()
    
    fig2.savefig(directory + 'first_basis_compare_k_' + str(k+1) + '.png')
    
    #get the derivative of the stacking waveform
    t = np.arange(500)
    y_stack_derivative = np.hstack(np.array(np.diff(y_stack, axis = 0))) / np.diff(t)
    
    #here I just do a quick check to see if the polarity is wrong and flip the signal if I need
    corr_coef, p = pearsonr(y_stack_derivative, np.array(basis[:, 1][0:-1]).flatten())
    if corr_coef < 0:
        basis[:, 1] *= -1
    
    if normalize:
        y_stack_derivative /= np.max(np.abs(y_stack_derivative))
        basis[:, 1] /= np.max(np.abs(basis[:, 1]))
    
    fig3 = plt.figure()
    plt.plot(y_stack_derivative, label = 'Derivative of stacking')
    plt.plot(basis[:, 1], 'r', label = '2nd basis SVD')
    plt.legend(loc = 3)

    if show_second_basis_compare:
        plt.show()
        
    fig3.savefig(directory + 'second_basis_compare_k_' + str(k+1) + '.png')