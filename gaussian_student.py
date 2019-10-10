"""
gaussian_student.py
-------------------

Plot the differences between Gaussian and student.

"""

import numpy as np
from scipy.stats import norm, t
import matplotlib.pyplot as plt


def main():
    """Make pretty plots."""
    xx = np.linspace(0, 6, 1000)

    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.5), dpi=100)
    axes[0].axvline(2, c='k', ls='--', lw=2)
    axes[1].axvline(2, c='k', ls='--', lw=2)
    axes[1].axvline(1, c='gray', ls='--', lw=1)
    axes[1].axvline(3, c='gray', ls='--', lw=1)
    yy = [norm.pdf(x) for x in xx]
    axes[0].plot(xx, yy, c='C0', lw=2, label='Gaussian')
    axes[1].plot(xx, yy, c='C0', lw=2, label='Gaussian')
    yy = [t.pdf(x, 1) for x in xx]
    axes[1].plot(xx, yy, c='C1', lw=2, label='t-Student')
    axes[0].legend(fontsize=8)
    axes[1].legend(fontsize=8)
    axes[0].set_ylabel('Density')
    axes[1].set_ylabel('Density')
    axes[0].set_xlabel('Distance')
    axes[1].set_xlabel('Distance')

    axes[0].set_xticks([0, 2, 4, 6])
    axes[0].set_xticklabels(['0', r'$2\sigma^2$', r'$4\sigma^2$', r'$6\sigma^2$'])
    axes[1].set_xticks([0, 2, 4, 6])
    axes[1].set_xticklabels(['0', r'$2\sigma^2$', r'$4\sigma^2$', r'$6\sigma^2$'])

    plt.subplots_adjust(wspace=0.4)
    plt.savefig('/home/leo/code/dimreduction/gaussian_student.png', bbox_inches='tight')



if __name__ == '__main__':
    main()
