import magic
import base64

def EncodeBase64(buffer, force_mimetype='', charset=''):
    if force_mimetype:
        mimetype = force_mimetype
    else:
        mimetype = magic.from_buffer(buffer, mime=True)

    header_parts = ['data:' + mimetype]

    if charset:
        header_parts.append('charset=' + charset)

    header_parts.append('base64')

    return ';'.join(header_parts) + ',' + base64.urlsafe_b64encode(buffer)
