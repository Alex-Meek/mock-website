import os
import numpy as np
from astropy.io import fits
from datetime import datetime, timezone

""" UTILS """
def _formatted_datetime():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]

def _make_data_dir(filepath: str):
    fits_file_output_directory, _ = os.path.split(filepath)
    try:
        os.makedirs(fits_file_output_directory, exist_ok=True)
    except Exception as error:
        print(
            'Could not create directory for fits files. Error type: {}'.format(
                type(error).__name__
            )        
        )
    return None 


""" MOCK DATA GENERATION WITHOUT BASE SAMPLE """
def _generate_mock_fits_primary_hdu_header() -> fits.Header:
    header = fits.Header()
    header['COMMENT'] = 'This is mock data.'
    return header 

def _generate_mock_fits_primary_hdu() -> fits.PrimaryHDU:
    header = _generate_mock_fits_primary_hdu_header()
    return fits.PrimaryHDU(header=header)

def _generate_mock_fits_img_hdu_header() -> fits.Header:
    header = fits.Header()
    header['ORIGIN'] = 'Mock SDO/JSOC'
    header['TELESCOP'] = 'Mock SDO/AIA'
    header['INSTRUME'] = 'Mock AIA_4'
    header['WAVELNTH'] = 94
    header['WAVEUNIT'] = 'angstrom'
    header['DATE'] = _formatted_datetime()
    header['DATE-OBS'] = _formatted_datetime()
    header['CAMERA'] = 4
    header['IMG_TYPE'] = 'LIGHT'
    header['EXPTIME'] = np.random.normal(3, 1, 1)[0]
    header['INT_TIME'] = np.random.normal(3, 1, 1)[0]
    header['PERCENTD'] = 100.
    header['CDELT1'] = 2.4000001000000002
    header['CDELT2'] = 2.4000001000000002
    header['CRPIX1'] = 512.5
    header['CRPIX2'] = 512.5
    header['CRVAL1'] = 0.
    header['CRVAL2'] = 0.
    header['CROTA2'] = 0.
    header['IMSCL_MP'] = 0.60010898099999999
    header['X0_MP'] = 2070.4499500000002
    header['Y0_MP'] = 2007.3699999999999
    header['SAT_Y0'] = 18.8537769
    header['SAT_Z0'] = 4.9396996499999997
    header['SAT_ROT'] = -5.3162264499999997E-05
    header['OBS_VR'] = 1414.4097911788506
    header['OBS_VW'] = 26913.808470297452
    header['OBS_VN'] = 969.31231078239114
    header['R_SUN'] = 1602.13086
    header['CRLN_OBS'] = 12.677167900000001
    header['CRLT_OBS'] = -6.7152929300000004
    header['CAR_ROT'] = 2295
    header['DSUN_OBS'] = 149316509596.3819
    header['CTYPE2'] = 'HPLT-TAN'
    return header

def _generate_mock_fits_img_hdu() -> fits.ImageHDU:
    return fits.ImageHDU(
        header=_generate_mock_fits_img_hdu_header(),
        data=np.random.uniform(size=(1024,1024))
    )

""" MOCK DATA GENERATION WITH BASE SAMPLE """
def _get_sample_fits_hdus(sample_filepath: str) -> tuple[
    fits.PrimaryHDU, fits.ImageHDU
]:
    try:
        with fits.open(sample_filepath) as f:
            primary_hdu, img_hdu = f
    except Exception as e:
        print("Failed to open sample fits file at {} with error: {}".format(
            sample_filepath, type(e).__name__
        ))
    return primary_hdu, img_hdu

def _modify_primary_hdu(primary_hdu: fits.PrimaryHDU) -> fits.PrimaryHDU:
    primary_hdu.header = _generate_mock_fits_primary_hdu_header()
    return primary_hdu

def _modify_img_hdu_header() -> None:
    
    # TODO
    
    return None 

def _modify_img_hdu_data() -> None:
    
    # TODO
    
    return None 

def _modify_img_hdu(img_hdu: fits.ImageHDU) -> fits.ImageHDU:
    img_hdu.header = _modify_img_hdu_header(img_hdu.header)
    img_hdu.data = _modify_img_hdu_data(img_hdu.data)
    return img_hdu
    
def _generate_hdu_obj(
    primary_hdu: fits.PrimaryHDU, img_hdu: fits.ImageHDU
) -> fits.HDUList:
    return fits.HDUList([primary_hdu, img_hdu])
    
def generate_and_write_mock_nasa_aia_fits(
    filepath: str,
    from_sample: bool,
    sample_filepath: str
):

    """_summary_
    Generates mock data mimicking the NASA AIA synoptic data at
    http://jsoc.stanford.edu/data/aia/synoptic/ such that an undue load is 
    not put on the website by analysis and archiving.
    
    Arguments:
        filepath -- (str) Path to save the fits file.
        from_sample -- (bool) Generate the fits file based on a sample containing
        image and header data.
        sample_filepath -- (str) Path to the sample .fits.
    
    Returns:
        None
    """
    
    _make_data_dir(filepath)
    
    if not from_sample:
        hdu_list_obj = _generate_hdu_obj(
            _generate_mock_fits_primary_hdu(),
            _generate_mock_fits_img_hdu()
        )
    else:
        primary_hdu, img_hdu = _get_sample_fits_hdus(sample_filepath)
        primary_hdu = _modify_primary_hdu(primary_hdu)
#        img_hdu = _modify_img_hdu(img_hdu)
        
        hdu_list_obj = fits.HDUList([])
        
    
 #   hdu_list_obj.writeto(filepath)
    return None

if __name__ == '__main__':
    generate_and_write_mock_nasa_aia_fits(
        filepath="./Data/AIA/mostrecent/test.fits",
        from_sample=True,
        sample_filepath='/Users/alexa/AIA Data/sample_mostrecent/AIAsynoptic0094.fits'
    )