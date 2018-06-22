# vapoursynth-plugin-check
A small python script to check for incorrect vapoursynth plugins in the autoload folder

## Usage
vs_plugin_check.py "path-to-vapoursynth-plugins-folder"

for portable VS use this bat example:
```
@ECHO OFF
VapourSynth64\python.exe VapourSynth64\vs_plugin_check.py %cd%\VapourSynth64\vapoursynth64\plugins
pause
```

core.std.LoadPlugin needs a full path otherwise this message is shown **LoadLibraryEx failed with code 87: Update windows and try again**

### Example Output
```
#######################################
VapourSynth Video Processing Library
Copyright (c) 2012-2018 Fredrik Mellbin
Core R43
API R3.5
Options: -

Architecture 64bit - Windows-10-10.0.16299-SP0
Python build: ('v3.6.4:d48eceb', 'Dec 19 2017 06:54:40')

#######################################
checking dlls in E:\PortableApps\VapourSynth\plugins64
#######################################
Errors:
-------
Failed to load E:\PortableApps\VapourSynth\plugins64\bilateralGPU.dll. GetLastError() returned 126. A DLL dependency is probably missing.
Failed to load E:\PortableApps\VapourSynth\plugins64\libIlmImf.dll. GetLastError() returned 126. A DLL dependency is probably missing.
Plugin load failed, namespace focus already populated (E:\PortableApps\VapourSynth\plugins64\libtemporalsoften.dll)

Errors: Not a VS-Plugin
-------
No entry point found in E:\PortableApps\VapourSynth\plugins64\CombMask.dll
No entry point found in E:\PortableApps\VapourSynth\plugins64\ReduceFlicker.dll
No entry point found in E:\PortableApps\VapourSynth\plugins64\XySubFilter.dll

Errors: incorrect bitness (32bit instead of 64bit) or corrupt file.
-------
Failed to load E:\PortableApps\VapourSynth\plugins64\externalfilters.dll. GetLastError() returned 193.
Failed to load E:\PortableApps\VapourSynth\plugins64\scenechange.dll. GetLastError() returned 193.
Failed to load E:\PortableApps\VapourSynth\plugins64\tc2cfr.dll. GetLastError() returned 193.
Failed to load E:\PortableApps\VapourSynth\plugins64\temporalsoften2.dll. GetLastError() returned 193.

Notices:
-------
cudart64_80.dll some dll for CUDA GPU stuff
libfftw3-3.dll is a dependency by fft3dfilter or mvtools-sf
libfftw3f-3.dll is a dependency by fft3dfilter or mvtools-sf
libiomp5md.dll is part of the Waifu2x-w2xc filter
libmfxsw64.dll is part of the DGMVCSourceVS filter
svml_dispmd.dll is part of the Waifu2x-w2xc filter
w2xc.dll is part of the Waifu2x-w2xc filter
#######################################
Found 103 dlls. Errors: 10 Notices: 7
```
