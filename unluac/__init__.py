import os
import subprocess
import importlib.resources

from tempfile import NamedTemporaryFile


def get_unluac_jar():
    jar_files = [file for file in importlib.resources.contents("unluac.jar") if file.endswith('.jar')]

    if jar_files:
        latest_jar = sorted(jar_files, reverse=True)[0]
        with importlib.resources.path("unluac.jar", latest_jar) as jar_path:
            return str(jar_path)
    else:
        raise FileNotFoundError('Cannot find any .jar files in package "unluac"')


__unluac_path = get_unluac_jar()


def decompile_file(filepath: str, timeout=30.0) -> str:
    """
    Decompiles the selected file and returns its source code.

    Parameters:
    filepath (str): Lua 5.1 or 5.2 compiled file.
    timeout (float): The maximum execution time after which subprocess.TimeoutExpired exception will be raised.

    Returns:
    str: Decompiled utf-8 source code of the file.
    """

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
    """
    Decompiles data and returns its source code.

    Parameters:
    data (bytes or bytearray): Lua 5.1 or 5.2 compiled code.
    timeout (float): The maximum execution time after which subprocess.TimeoutExpired exception will be raised.

    Returns:
    str: Decompiled utf-8 source code of the data.
    """

    tmp = NamedTemporaryFile(mode='wb', delete=False)
    tmp.write(data)
    tmp.close()
    data = decompile_file(tmp.name)
    os.unlink(tmp.name)
    return data