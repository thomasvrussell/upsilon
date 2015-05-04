__author__ = 'kim'

try:
    import pyfftw

    print '-------------------'
    print '| pyFFTW detected |'
    print '-------------------'
except:
    print '---------------------------------'
    print '** WARNING: No pyFFTW detected **'
    print '---------------------------------'

from upsilon import utils
from upsilon.extract_features.extract_features import ExtractFeatures
