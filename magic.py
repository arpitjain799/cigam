import binascii


class Match(object):

    def __init__(self, data):
        self.data = data

    def is_apk(self):
        zip_magic = b'504b0304'
        if zip_magic not in binascii.hexlify(self.data[:4]):
            return None

        # AndroidManifest.xml
        manifest_bytes = b'416e64726f69644d616e69666573742e786d6c'
        contains_manifest = manifest_bytes in binascii.hexlify(self.data)

        # classes
        classes_bytes = b'636c6173736573'
        contains_classes = classes_bytes in binascii.hexlify(self.data)

        if contains_classes and contains_classes:
            return ('.apk', 'apk', 'Android application package')
        elif contains_classes:
            return ('.apk', 'apk, without AndroidManifest.xml', 'Android application package')
        else:
            return ('.apk', 'apk, without classes.dex', 'Android application package')

    def is_axml(self):
        magic = binascii.hexlify(self.data[:4])
        if b'03000800' == magic:
            return ('.xml', 'axml', 'Android binary XML')
        elif b'00000800' == magic:
            return ('.xml', 'axml with modified', 'Android binary XML')
        return None

    def is_arsc(self):
        if b'02000c00' == binascii.hexlify(self.data[:4]):
            return ('.arsc', 'arsc', 'Android resources')
        return None

    def is_elf(self):
        if b'7f454c46' == binascii.hexlify(self.data[:4]):
            return ('.so', 'elf', 'Executable and Linkable Format')
        return None

    def is_dex(self):
        if b'6465780a' == binascii.hexlify(self.data[:4]):
            return ('.dex', 'dex', 'Android Dalvik Executable format')
        return None

    def is_sqlite(self):
        if b'53514c69746520666f726d617420' == binascii.hexlify(self.data[:14]):
            return ('.db', 'db', 'SQlite format')
        return None

    def is_odex(self):
        if b'6465790a' == binascii.hexlify(self.data[:4]):
            return ('.odex', 'odex', 'Android Optimized Dalvik EXecutable')
        return None

    def is_zip(self):
        if b'504b0304' == binascii.hexlify(self.data[:4]):
            return ('.zip', 'application/zip', 'ZIP archive')
        return None

    def is_tar(self):
        if b'66697874' == binascii.hexlify(self.data[:4]):
            return ('.tar', 'application/x-tar', 'Tape Archive (TAR)')
        return None

    def is_jpg(self):
        if b'ffd8ff' != binascii.hexlify(self.data[:3]):
            return None
        bytes = binascii.hexlify(self.data[6:10])
        if b'45786966' == bytes:
            return ('.jpg', 'image/jpeg, Exif', 'JPEG images')
        if b'4a464946' == bytes:
            return ('.jpg', 'image/jpeg, JFIF', 'JPEG images')
        return ('.jpg', 'image/jpeg', 'JPEG images')

    def is_png(self):
        if b'89504e47' == binascii.hexlify(self.data[:4]):
            return ('.png', 'image/png', '')
        return None

    def is_ico(self):
        if b'00000100' == binascii.hexlify(self.data[:4]):
            return ('.ico', 'image/ico', 'MS Windows icon resource')
        return None

    def is_gif(self):
        if b'47494638' == binascii.hexlify(self.data[:4]):
            return ('.gif', 'image/gif', 'Graphics Interchange Format (GIF)')
        return None

    def is_ogg(self):
        if b'4f676753' == binascii.hexlify(self.data[:4]):
            return ('.ogg', 'audio/ogg', 'OGG audio')
        return None


class Magic(object):

    def __init__(self, data):
        self.data = data
        self.extension = 'Unknown'
        self.mime = 'Unknown'
        self.doc = 'Unknown'

        if self.istext(data):
            if '<?xml' in data[:5].decode(errors='ignore'):
                self.extension = '.xml'
                self.mime = 'xml/plain'
                self.doc = 'XML document text'
                return

            self.extension = '.txt'
            self.mime = 'text/plain'
            self.doc = 'textual file'
            return

        m = Match(data)
        for mtd in dir(m):
            if mtd.startswith('is_'):
                result = getattr(m, mtd)()
                if result:
                    self.extension, self.mime, self.doc = result
                    break

        if self.mime == 'Unknown':
            self.extension = '.data'

    def istext(self, data):
        try:
            data.decode()
            return True
        except UnicodeDecodeError:
            try:
                data.decode('gbk')
                return True
            except UnicodeDecodeError:
                pass
        return False

    def get_extension(self):
        return self.extension

    def get_mime(self):
        return self.mime

    def get_doc(self):
        return self.doc


if __name__ == "__main__":
    import os
    filepath = "E:\\samples\\vt\\apks\\Adware.Android.Kuguo.A"
    for parent, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            filepath = os.path.join(parent, filename)
            with open(filepath, mode='rb') as f:
                m = Magic(f.read())
                print(filepath, m.get_mime())

    # with open(filepath, mode='rb') as f:
    #     data = f.read()
    #     print(filepath, data[:8])
    #     m = Magic(data)
    #     print(m.get_extension())
