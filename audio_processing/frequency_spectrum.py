import numpy as np

def draw_Gaussian(nu,freq,amp,width):

    return amp*np.exp(-(nu-freq)**2/(2*width)**2)
    

# def Hz_decay(freqspec,profile=None,**kwargs):
#     '''
#     None
#     Linear
#     Exponential
#     Logarithmic
#     Gaussian
#     Lorentzian
#     '''
#     if profile==None:
#         out = freqspec
#     if profile== 'Exponential':
#         kwargs['T_C']
#         out = freqspec*np.exp**(-kwargs['T_C'])


