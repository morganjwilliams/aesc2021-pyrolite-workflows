import base64
import pandas as pd
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen


def get_onedrive_directlink(onedrive_link):
    """
    Get a public Onedrive filehandle for linking directly to pandas.
    
    Parameters
    -----------
    onedrive_link : str
        Onedrive share URL.
        
    Returns
    -------
    direct_url
        Base64-encoded URL for direct download/for use as a file handle.
        
    Notes
    -----
    Found here:
    https://towardsdatascience.com/how-to-get-onedrive-direct-download-link-ecb52a62fee4
    """
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_string = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    direct_url = "https://api.onedrive.com/v1.0/shares/u!{}/root/content".format(data_bytes64_string)
    return direct_url
