"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class image_t(object):
    __slots__ = ["utime", "size", "data"]

    __typenames__ = ["int64_t", "int32_t", "byte"]

    __dimensions__ = [None, None, ["size"]]

    def __init__(self):
        self.utime = 0
        self.size = 0
        self.data = ""

    def encode(self):
        buf = BytesIO()
        buf.write(image_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qi", self.utime, self.size))
        buf.write(bytearray(self.data[:self.size]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != image_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return image_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = image_t()
        self.utime, self.size = struct.unpack(">qi", buf.read(12))
        self.data = buf.read(self.size)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if image_t in parents: return 0
        tmphash = (0x6622163ed1a7984d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if image_t._packed_fingerprint is None:
            image_t._packed_fingerprint = struct.pack(">Q", image_t._get_hash_recursive([]))
        return image_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

