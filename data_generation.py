import os
import numpy as np
from astropy.io import fits
from datetime import datetime, timezone

def formatted_datetime():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]

def nasa_sdo_aia_data_generation (filepath: str):

    """ This should generate data files for the website at a particular directory """

    hdr = fits.Header()
    hdr['COMMENT'] = 'This is mock data.'
    hdu_1 = fits.PrimaryHDU(header=hdr)

    hdr = fits.Header()
    hdr['ORIGIN'] = 'Mock SDO/JSOC'
    hdr['TELESCOP'] = 'Mock SDO/AIA'
    hdr['INSTRUME'] = 'Mock AIA_4'
    hdr['WAVELNTH'] = 94
    hdr['WAVEUNIT'] = 'angstrom'
    hdr['DATE'] = formatted_datetime()
    hdr['DATE-OBS'] = formatted_datetime()
    hdr['CAMERA'] = 4
    hdr['IMG_TYPE'] = 'LIGHT'
    hdr['EXPTIME'] = np.random.normal(3, 1, 1)[0]
    hdr['INT_TIME'] = np.random.normal(3, 1, 1)[0]
    hdr['PERCENTD'] = 100.
    hdr['CDELT1'] = 2.4000001000000002
    hdr['CDELT2'] = 2.4000001000000002
    hdr['CRPIX1'] = 512.5
    hdr['CRPIX2'] = 512.5
    hdr['CRVAL1'] = 0.
    hdr['CRVAL2'] = 0.
    hdr['CROTA2'] = 0.
    hdr['IMSCL_MP'] = 0.60010898099999999
    hdr['X0_MP'] = 2070.4499500000002
    hdr['Y0_MP'] = 2007.3699999999999
    hdr['SAT_Y0'] = 18.8537769
    hdr['SAT_Z0'] = 4.9396996499999997
    hdr['SAT_ROT'] = -5.3162264499999997E-05
    hdr['OBS_VR'] = 1414.4097911788506
    hdr['OBS_VW'] = 26913.808470297452
    hdr['OBS_VN'] = 969.31231078239114
    hdr['R_SUN'] = 1602.13086
    hdr['CRLN_OBS'] = 12.677167900000001
    hdr['CRLT_OBS'] = -6.7152929300000004
    hdr['CAR_ROT'] = 2295
    hdr['DSUN_OBS'] = 149316509596.3819
    hdr['CTYPE2'] = 'HPLT-TAN'

    hdu_2 = fits.ImageHDU(
        header=hdr,
        data=np.random.uniform(size=(1024,1024))
        )
    file = fits.HDUList([hdu_1, hdu_2])
    file.writeto(filepath)
    return None

nasa_sdo_aia_data_generation("./Data/AIA/mostrecent/test.fits")
