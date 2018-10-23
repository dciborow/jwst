from .model_base import DataModel
from .image import ImageModel


__all__ = ['SlitModel', 'SlitDataModel']


class SlitDataModel(DataModel):
    """
    A data model for 2D images.

    Attributes
    __________
    data : numpy float32 array
         The science data

    dq : numpy uint32 array
         Data quality array

    err : numpy float32 array
         Error array

    wavelength : numpy float32 array
         Wavelength array, corrected for zero-point

    barshadow : numpy float32 array
         Bar shadow correction

    area : numpy float32 array
         Pixel area map array

    relsens : numpy table
         relative sensitivity table

    var_poisson : numpy float32 array
         variance due to poisson noise

    var_rnoise : numpy float32 array
         variance due to read noise

    pathloss_pointsource2d : numpy float32 array
         2-d array for pathloss (point source)

    pathloss_pointsource : numpy float32 array
         pathloss array for point sources

    wavelength_pointsource : numpy float32 array
         wavelength array for point sources

    pathloss_uniformsource2d : numpy float32 array
         2-d array for pathloss (uniform source)

    pathloss_uniformsource : numpy float32 array
         pathloss_array for uniform sources

    wavelength_uniformsource : numpy float32 array
         wavelength array for uniform sources

    """

    schema_url = "slitdata.schema.yaml"

    def __init__(self, init=None, **kwargs):
        if isinstance(init, (SlitModel, ImageModel)):
            super(SlitDataModel, self).__init__(init=None, **kwargs)
            self.data = init.data
            self.dq = init.dq
            self.err = init.err
            self.relsens = init.relsens
            self.area = init.area
            if init.hasattr('wavelength'):
                self.wavelength = init.wavelength
            if init.hasattr('var_poisson'):
                self.var_poisson = init.var_poisson
            if init.hasattr('var_rnoise'):
                self.var_rnoise = init.var_rnoise
            for key in kwargs:
                setattr(self, key, kwargs[key])

            if init.meta.hasattr('wcs'):
                self.meta.wcs = init.meta.wcs
            else:
                self.meta.wcs = None
        else:
            super(SlitDataModel, self).__init__(init=init, **kwargs)
            if kwargs:
                for key in kwargs:
                    setattr(self, key, kwargs[key])


class SlitModel(DataModel):
    """
    A data model for 2D images.

    Attributes
    __________
    data : numpy float32 array
         The science data

    dq : numpy uint32 array
         Data quality array

    err : numpy float32 array
         Error array

    wavelength : numpy float32 array
         Wavelength array, corrected for zero-point

    barshadow : numpy float32 array
         Bar shadow correction

    area : numpy float32 array
         Pixel area map array

    relsens : numpy table
         relative sensitivity table

    var_poisson : numpy float32 array
         variance due to poisson noise

    var_rnoise : numpy float32 array
         variance due to read noise

    pathloss_pointsource2d : numpy float32 array
         2-d array for pathloss (point source)

    pathloss_pointsource : numpy float32 array
         pathloss array for point sources

    wavelength_pointsource : numpy float32 array
         wavelength array for point sources

    pathloss_uniformsource2d : numpy float32 array
         2-d array for pathloss (uniform source)

    pathloss_uniformsource : numpy float32 array
         pathloss_array for uniform sources

    wavelength_uniformsource : numpy float32 array
         wavelength array for uniform sources

    int_times : numpy table
         table of times for each integration

    """
    schema_url = "slit.schema.yaml"

    def __init__(self, init=None, **kwargs):
        if isinstance(init, (SlitModel, ImageModel)):
            super(SlitModel, self).__init__(init=None, **kwargs)
            self.update(init)
            self.data = init.data
            self.dq = init.dq
            self.err = init.err
            self.relsens = init.relsens
            self.area = init.area
            if init.hasattr('wavelength'):
                self.wavelength = init.wavelength
            if init.hasattr('var_poisson'):
                self.var_poisson = init.var_poisson
            if init.hasattr('var_rnoise'):
                self.var_rnoise = init.var_rnoise
            if init.hasattr('int_times'):
                self.int_times = init.int_times
            if init.meta.hasattr('wcs'):
                self.meta.wcs = init.meta.wcs
            else:
                self.meta.wcs = None
        else:
            super(SlitModel, self).__init__(init=init, **kwargs)
            if kwargs:
                for key in kwargs:
                    setattr(self, key, kwargs[key])
