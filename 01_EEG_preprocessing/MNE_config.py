# Default settings for data processing and analysis.

from collections.abc import Callable, Sequence
from typing import Annotated, Any, Literal

from annotated_types import Ge, Interval, Len, MinLen
from mne import Covariance
from mne_bids import BIDSPath

from mne_bids_pipeline.typing import (
     ArbitraryContrast,
     DigMontageType,
     FloatArrayLike,
     PathLike,
 )

import numpy as np
import pandas as pd
import os



#______________________________________________________________________________________
# %%
# # General settings

bids_root = '/scratch2/alinat/project/PD-EEG-ANON_eegOnly/sourcedataRest'                             # where data placed
deriv_root = '/scratch2/alinat/project/PD-EEG-ANON_eegOnly/derivatives/mne_pipeline_eye-closed_run1'                     # where save to
subjects_dir = '/scratch2/alinat/project/PD-EEG-ANON_eegOnly/derivatives/FS_SUBJECT_DIR'    # for freesurfer

os.environ['FREESURFER_HOME'] = '/usr/local/freesurfer'
os.environ['SUBJECTS_DIR'] = subjects_dir 
os.environ['FS_LICENSE'] = '/usr/local/freesurfer/.license'


sessions = 'all' #'20210504' #'all'
task = 'restEyesClosed'
task_is_rest = True
runs = ['01']#'all'
#exclude_runs = None

subjects = 'all'
#exclude_subjects = ['NZ000052', 'NZ000681', 'NZ004808', 'NZ007600']

process_empty_room = False
#process_rest = False

ch_types = ['eeg']
data_type = 'eeg'

#eog_channels = ['VEO'] #

eeg_reference = 'average'
#eeg_template_montage = None
#drop_channels = []

plot_psd_for_runs = 'all'

random_state = 42



#______________________________________________________________________________________
# %%
# # Preprocessing

# ## Break detection
#None

# ## Bad channel detection
#None
#detection done before, with pyprep function

# ## Maxwell filter
#None

# ## Filtering & resampling
# ### Filtering
l_freq = 0.5
h_freq = 100
notch_freq = None#[50, 100, 150]
#notch_trans_bandwidth = 
#notch_widths = None

# ### Resampling
raw_resample_sfreq = 250

# ## Epoching
epochs_tmin = 0
epochs_tmax = 3
rest_epochs_duration = 3
rest_epochs_overlap = 1.5
baseline = None

# ## Artifact removal
# ### SSP, ICA, and artifact regression
spatial_filter = 'ica'
ica_reject = 'autoreject_local'
ica_algorithm = 'picard-extended_infomax'

# ### Amplitude-based artifact rejection
reject = 'autoreject_local'
autoreject_n_interpolate = [1, 4, 8, 16, 32]

#______________________________________________________________________________________
# # %%
# # # Sensor-level analysis

# # ## Condition contrasts
# # None, as restng state
# #contrasts = ['rest']

# # ## Decoding / MVPA
# # None, as resting state, by default decode=True
# decode = True
# decoding_which_epochs = 'cleaned'
# #decoding_epochs_tmin = 0
# #decoding_epochs_tmax = None
# decoding_csp = True
# decoding_csp_freqs = { 'delta' : [0.5, 4],
#                        'theta': [4.01, 7.99],
#                        'alpha': [8, 12.99],
#                        'beta' : [13, 30],
#                        'gamma1': [30.01, 49],
#                        'gamma2': [51, 80]
#                        }

# # ## Time-frequency analysis
# time_frequency_conditions =['rest']
# time_frequency_freq_min = 1
# time_frequency_freq_max = 100
# time_frequency_cycles = np.arange(time_frequency_freq_min, time_frequency_freq_max) / 3 #default parameter

# # ## Group-level analysis
# interpolate_bads_grand_average = True


# #______________________________________________________________________________________
# # %%
# # # Source-level analysis

# # ## General source analysis settings
# run_source_estimation = True

# # ## BEM surface
# use_template_mri = "fsaverage"
# adjust_coreg = True
# bem_mri_images = 'auto'
# freesurfer_verbose = True

# # ## Source space & forward solution

# def get_t1_from_eeg(bids_path):
#     anat_bids_path = BIDSPath(subject=bids_path.subject,
#                               session=bids_path.session,
#                               suffix="T1w",  # Suffix for T1-weighted defaced MRI
#                               extension='.nii.gz',   # NIfTI format
#                               datatype='anat',       # Data type is anatomical (anat)
#                               root=bids_path.root)
#     return anat_bids_path

# mri_t1_path_generator = get_t1_from_eeg

# spacing = 'all'


# # ## Inverse solution
# inverse_method = 'dSPM'
# noise_cov = 'ad-hoc'
# noise_cov_method = 'auto'



# #______________________________________________________________________________________
# # %%
# # # Reports


# #______________________________________________________________________________________
# # %%
# # # Caching


# #______________________________________________________________________________________
# # %%
# # # Parallelization
# n_jobs = 10






# #______________________________________________________________________________________
# # %%
# # # Logging



#______________________________________________________________________________________
# %%
# # Error handling
on_error = 'continue'
