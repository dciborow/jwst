from .model_base import DataModel

__all__ = ['AmiLgModel']


class AmiLgModel(DataModel):
    """
    A data model for AMI LG analysis results.

    Attributes
    __________
    fit_image : numpy float32 array
         Fitted image

    resid_image : numpy float32 array
         Residual image

    closure_amp_table : numpy table
         Closure amplitudes table

    closure_phase_table : numpy table
         Closure phases table

    fringe_amp_table : numpy table
         Fringe amplitudes table

    fringe_phase_table : numpy table
         Fringe phases table

    pupil_phase_table : numpy table
         Pupil phases table

    solns_table : numpy table
         Solutions table
    """
    schema_url = "amilg.schema.yaml"

    def get_primary_array_name(self):
        """
        Returns the name "primary" array for this model, which
        controls the size of other arrays that are implicitly created.
        This is intended to be overridden in the subclasses if the
        primary array's name is not "data".
        """
        return 'fit_image'
