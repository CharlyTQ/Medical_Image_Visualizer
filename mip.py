import nibabel as nib

"""
import matplotlib.pyplot as plt

def show_slices(slices):
    _, axes = plt.subplots(1, len(slices))

    if(len(slices) == 1): # Handle the one slice case
        axes.imshow(slices[0].T, cmap="gray", origin="lower")
    else:                 # Multiple slices case
        for i, slice in enumerate(slices):
            axes[i].imshow(slice.T, cmap="gray", origin="lower")
"""

"""
niireader class to load the files and extract the slices
"""
class niireader:
    def __init__(self, filepath = None):
        if filepath != None:
            self.load(filepath = filepath)
        self.nii = None

    def load(self, filepath = None):
        """
        Load the file in the object
        """
        self.nii = nib.load(filepath)
        self.data = self.nii.get_fdata()

    def getSlice(self, slice: int = 0, view = 0):
        """
        Return a slice or the '*.nii' or '*.nii.gz' file.

        slice:
        Slice to extract.

        view:
        View to extract ('axial' or 0, 'sagittal' or 1 and 'coronal' or 2)
        """
        if slice < 0:
            slice = 0

        if view == 0 or view == "axial":
            if slice >= list(self.data.shape)[2]:
                slice = -1

            return self.data[:, :, slice]
        
        elif view == 1 or view == "sagittal":
            if slice >= list(self.data.shape)[0]:
                slice = -1

            return self.data[slice, :, :]

        elif view == 2 or view == "coronal":
            if slice >= list(self.data.shape)[1]:
                slice = -1

            return self.data[:, slice, :]


    def getSliceMax(self, view = 0):
        """
        Return a slice or the '*.nii' or '*.nii.gz' file.

        view:
        View to extract ('axial' or 0, 'sagittal' or 1 and 'coronal' or 2)
        """
        if view == 0 or view == "axial":
            return list(self.data.shape)[2]
        
        elif view == 1 or view == "sagittal":
            return list(self.data.shape)[0]

        elif view == 2 or view == "coronal":
            return list(self.data.shape)[1]

    
