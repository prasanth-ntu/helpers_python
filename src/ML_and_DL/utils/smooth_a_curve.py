# Title         : Smooth a curve based on moving average (by convolution)
# Date added    : 26 Jun 2019
# Date Modified : 26 Jun 2019

import numpy as np
import matplotlib.pyplot as plt
from math import ceil

def smooth(y, box_pts=10):
    '''Smooth a curve, using a moving average box (by convolution)

    Parameters:
    -----------
    y : 1D numpy array or list
        Signal to be smoothed
    box_pts : int (default:10)
        Moving averge window size

    Returns:
    --------
    y_smooth : 1D numpy array
        Smooted curve using moving average
    '''
    box = np.ones(box_pts)/box_pts

    # For first box_pts, we calculate the average manually #
    y_smooth = []
    for i in range(1,box_pts):
         y_smooth.append(sum(y[0:i])/len(y[0:i]))

    # mode='valid' => Convolution product is only given for points where signals (y and box) completely overlap #
    y_smooth_valid = np.convolve(y,box,mode='valid')
    y_smooth = y_smooth + list(y_smooth_valid)
    return np.array(y_smooth)

if __name__ == '__main__':
    #############################
    ###    Generate signal    ###
    #############################
    # Create an exponential curve #
    y_org = np.concatenate((np.exp(np.arange(3.5,-2,-.005)), np.exp(np.arange(-2,1,.005))))

    # Add a sin wave into it #
    # y_org += np.sin(np.linspace(0,len(y_org), len(y_org)))*.1

    # Add some random noise #
    y_org += np.random.randn(len(y_org))*.02

    # Add random noise to 10% of the signal #
    nums = np.random.randn(len(y_org))*.1
    nums[ceil(len(nums)*.10):] = 0
    np.random.shuffle(nums)
    y_org += nums

    #############################
    ###   Smooth the signal   ###
    #############################
    y_smooth_10 = smooth(y_org, box_pts=10)

    #############################
    ### Find the local minima ###
    #############################
    y_minima = min(y_smooth_10)
    y_minima_index = np.where(y_smooth_10 == y_minima)[0][0]

    #############################
    ###    Plot the signal    ###
    #############################
    plt.figure(figsize=(18,8))

    plt.subplot(1,2,1)
    plt.plot(y_org)
    plt.plot(y_smooth_10, linewidth=2)
    plt.legend(['y_org', 'y_smooth_10'])
    plt.plot([y_minima_index, y_minima_index],[-1,5], 'r--')

    plt.subplot(1,2,2)
    plt.plot(y_org)
    plt.plot(y_smooth_10, linewidth=3)
    plt.ylim([-.2,1]); plt.xlim([600,1600])
    plt.legend(['y_org', 'y_smooth_10'])
    plt.plot([y_minima_index, y_minima_index],[-1,5], 'r--')

    plt.plot()
    plt.show()
