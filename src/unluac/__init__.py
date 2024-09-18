import os

if os.system("java -version") != 0:
    raise Exception("Java vm is required")

import subprocess
from tempfile import NamedTemporaryFile

__jar_path = os.path.dirname(__file__) + os.sep + 'jar'
__unluac_path = __jar_path + os.sep + sorted(os.listdir(__jar_path), reverse=True)[0]

def decompile_file(filepath: str, timeout=30) -> str:
    proc = subprocess.Popen(('java', '-jar', __unluac_path, filepath), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        data, errs = proc.communicate(timeout=timeout)
        if len(errs):
            raise Exception(errs)
        return data
    except subprocess.TimeoutExpired as e:
        subprocess.run(('taskkill', '/F', '/T', '/PID', str(proc.pid)), stdout=subprocess.DEVNULL)
        raise e

def decompile(data: bytes | bytearray) -> str:
    if len(data) < 5:
        raise ValueError('data is too short')

    if data[:4] != b'\x1bLua':
        raise ValueError('data is not compiled lua code')

    if data[4] not in (0x51, 0x52):
        raise NotImplementedError('only Lua 5.1 and 5.2 are allowed')
    
    tmp = NamedTemporaryFile(mode='wb', delete=False)
    tmp.write(data)
    tmp.close()
    data = decompile_file(tmp.name)
    os.unlink(tmp.name)
    return data