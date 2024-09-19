import os
import regex
import subprocess

# Place your lua executables like so:
# gen_test_data.py
# 5.1\
#    luac5.1.exe
#    ...
# 5.2\
#    luac.exe
#    ...
# ...
# version\
#    luac[version].exe

r = regex.compile(r"^luac.*\.exe")

script_dir = os.path.dirname(__file__)
out_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
lua_src_path = out_dir + os.sep + 'source.lua'
print('Script directory:', script_dir)
print('Output directory:', out_dir)
print('Source file:', lua_src_path, '\n')
for lua_version in os.listdir(script_dir):
    abs_path = script_dir + os.sep + lua_version
    if os.path.isdir(abs_path):
        for executable in os.listdir(abs_path):
            if r.match(executable):
                print('Generating test file for Lua %s' % lua_version + '...')
                proc = subprocess.Popen(('-s', '-o', out_dir + os.sep + 'v%s.luac64' % lua_version, lua_src_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable=abs_path + os.sep + executable)
                stdout, stderr = proc.communicate(timeout=30)
                if stderr:
                    print('Error:', stderr.decode('utf-8'))
                elif stdout:
                    print(stdout.decode('utf-8'))
                else:
                    print('Success!')