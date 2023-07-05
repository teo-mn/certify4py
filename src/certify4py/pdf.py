#
# pdf файлтай ажиллах хэсэг
#
import hashlib
from pdfrw import PdfWriter, PdfReader, PdfDict


def hash_certificates(cert_files):
    """
    Hashes (sha256) all files passed as an array and returns them as an array.
    """
    hashes = []
    for f in cert_files:
        with open(f, 'rb') as cert:
            hash_ = hashlib.sha256(cert.read()).hexdigest()
            hashes.append(hash_)
            print(hash_)

    return hashes


def add_metadata(src: str, dest: str, **kwargs):
    pdf = PdfReader(src)
    metadata_dict = PdfDict(**kwargs)
    if pdf.Info is None:
        pdf.Info = {}
    pdf.Info.update(metadata_dict)
    PdfWriter().write(dest, pdf)
