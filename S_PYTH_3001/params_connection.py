import _io

#===============================================
# constantes
#===============================================
READ_ONLY_MODE = "r"
WRITE_ONLY_MODE = "w"

APPEND_MODE = "a"
APPEND_READ_MODE = "a+"

BINARY_READ_MODE = "rb"
BINARY_WRITE_MODE = "wb"

READ_WRITE_MODE = "r+"
WRITE_READ_MODE = "w+"

BINARY_READ_WRITE_MODE = "rb+"
BINARY_WRITE_READ_MODE = "wb+"

VALID_MODES = (
    READ_ONLY_MODE,
    WRITE_ONLY_MODE,
    APPEND_MODE,
    APPEND_READ_MODE,
    BINARY_READ_MODE,
    BINARY_WRITE_MODE,
    READ_WRITE_MODE,
    WRITE_READ_MODE,
    BINARY_READ_WRITE_MODE,
    BINARY_WRITE_READ_MODE
)

BUFFERED_READER = _io.BufferedReader
BUFFERED_WRITER = _io.BufferedWriter
BUFFERED_RANDOM = _io.BufferedRandom
TEXT_IO_WRAPPER = _io.TextIOWrapper

