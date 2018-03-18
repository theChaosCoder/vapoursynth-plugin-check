# vapoursynth-plugin-check
A small python script to check for incorrect vapoursynth plugins in the autoload folder

## Usage
vs_plugin_check.py "path-to-vapoursynth-plugins-folder"

## Todo
- Find and set path of VS installation via registry
- Make it work with VS portable

### Example Output
```
#######################################
VapourSynth Video Processing Library
Copyright (c) 2012-2018 Fredrik Mellbin
Core R43
API R3.5
Options: -

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
