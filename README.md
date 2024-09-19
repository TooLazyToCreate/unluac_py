# Python bindings for the unluac tool
This package makes it easier to interact with the unluac tool (https://sourceforge.net/projects/unluac/).
## Install

    git clone https://github.com/TooLazyToCreate/unluac_py.git
    python -m pip install ./unluac_py
You can easily remove this package using this command:  

    python -m pip uninstall unluac
If you want to replace unluac with another version, just put the version you need in the unluac/jar before installing.
## Usage

    import unluac

    
    # decompile file
    luac_path = "some_file.luac"
    try:
        source = unluac.decompile_file(luac_path)
    except Exception as e:
        print(e)
        exit(1)

    with open("decompiled_file.lua", "w") as f:
        f.write(source)

    
    # or just raw data
    with open(luac_path, 'rb') as f:
        compiled_data = f.read()
    try:
        source = unluac.decompile(compiled_data)
    except Exception as e:
        print(e)
        exit(1)

    with open("same_decompiled_file.lua", "w") as f:
        f.write(source)
