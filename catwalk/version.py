_MAJOR = "0"
_MINOR = "2"
# On main and in a nightly release the patch should be one ahead of the last
# released build.
_PATCH = "2"
# This is mainly for pre-releases which have the suffix "rc[0-9]+".
_SUFFIX = ""

VERSION_SHORT = "{0}.{1}".format(_MAJOR, _MINOR)
VERSION = "{0}.{1}.{2}{3}".format(_MAJOR, _MINOR, _PATCH, _SUFFIX)
