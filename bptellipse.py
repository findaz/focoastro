import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def BPT_ell(cov, means, ax, col):
    """ Plot confidences interval at 68% and 95% (1 and 2 sigmas)
    in the BPT diagram.
    """
    v, w = np.linalg.eigh(cov[:2,:2])
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan2(u[1], u[0])
    angle = 180 * angle / np.pi  # convert to degrees
    norm_1s = 2 * np.sqrt(2*v)
    norm_2s = 4 * np.sqrt(2*v)

    ell_2s = mpl.patches.Ellipse(xy=means[:2], width=norm_2s[0], height=norm_2s[1],
                                 angle=angle, color=col)
    ell_2s.set_clip_box(ax.bbox)
    ell_2s.set_alpha(0.15)
    ax.add_artist(ell_2s)
    ell_1s = mpl.patches.Ellipse(xy=means[:2], width=norm_1s[0], height=norm_1s[1],
                                 angle=angle, color=col)
    ell_1s.set_clip_box(ax.bbox)
    ell_1s.set_alpha(0.7)
    ax.add_artist(ell_1s)
    
def WHAN_ell(cov, means, ax, col):
    """ Plot confidences interval at 68% and 95% (1 and 2 sigmas)
    in the WHAN diagram.
    """
    v, w = np.linalg.eigh(cov[0:3:2,0:3:2])
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan2(u[1], u[0])
    angle = 180 * angle / np.pi  # convert to degrees
    norm_1s = 2 * np.sqrt(2*v)
    norm_2s = 4 * np.sqrt(2*v)
    
    ell_2s = mpl.patches.Ellipse(xy=means[0:3:2], width=norm_2s[0], height=norm_2s[1],
                                 angle=angle, color=col)
    ell_2s.set_clip_box(ax.bbox)
    ell_2s.set_alpha(0.15)
    ax.add_artist(ell_2s)
    ell_1s = mpl.patches.Ellipse(xy=means[0:3:2], width=norm_1s[0], height=norm_1s[1],
                                 angle=angle, color=col)
    ell_1s.set_clip_box(ax.bbox)
    ell_1s.set_alpha(0.7)
    ax.add_artist(ell_1s)