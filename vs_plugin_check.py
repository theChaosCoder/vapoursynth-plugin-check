import sys, os, glob
import vapoursynth as vs
import winreg

def print_version(core):
	vs_version = core.version()
	print('#######################################')
	print(vs_version)
	print('#######################################')

def main(argv):
	if(len(sys.argv) > 1):
		path = argv[1]
	else:
		exit("\n\rUsage: vs_plugin_check.py <path-to-vapoursynth-plugins-folder>\n\r")
	
	core = vs.get_core()
	print_version(core)
	plugin_dir = glob.glob(path + '/*.dll')
	
	print("checking dlls in", path)
	print('#######################################')
	
	error = []
	error32bit = []
	errorNoEntry = []
	notice = []
	for dll in plugin_dir:
		try:
			core.std.LoadPlugin(path=dll)
		except Exception as e:
			if "already loaded" not in str(e):
				if "returned 193" in str(e):
					error32bit.append(e)
					continue
					
				#https://github.com/HomeOfVapourSynthEvolution/VapourSynth-Waifu2x-w2xc
				if "libiomp5md.dll" in str(e):
					notice.append("libiomp5md.dll is part of the Waifu2x-w2xc filter")
					continue
				if "w2xc.dll" in str(e):
					notice.append("w2xc.dll is part of the Waifu2x-w2xc filter")
					continue
				if "svml_dispmd.dll" in str(e):
					notice.append("svml_dispmd.dll is part of the Waifu2x-w2xc filter")
					continue
					
				if "cudart64_80.dll" in str(e):
					notice.append("cudart64_80.dll some dll for CUDA GPU stuff")
					continue
					
				if "libmfxsw64.dll" in str(e):
					notice.append("libmfxsw64.dll is part of the DGMVCSourceVS filter")
					continue
					
				if "libfftw3f-3.dll" in str(e):
					notice.append("libfftw3f-3.dll is a dependency by fft3dfilter or mvtools-sf")
					continue
				if "libfftw3-3.dll" in str(e):
					notice.append("libfftw3-3.dll is a dependency by fft3dfilter or mvtools-sf")
					continue
				
				if "No entry point found" in str(e):
					errorNoEntry.append(e)
					continue

				error.append(e)
				
	print("Errors:")
	print("-------")
	for err in error:
		print(err)
		
	print()
	print("Errors: Not a VS-Plugin")
	print("-------")
	for err in errorNoEntry:
		print(err)
	
	print()
	print("Errors: incorrect bitness (32bit instead of 64bit) or corrupt file.")
	print("-------")
	for err in error32bit:
		print(err)
		
	print()
	print("Notices:")
	print("-------")
	for n in notice:
		print(n)
		
	print('#######################################')
	print("Found", len(plugin_dir), "dlls. Errors:", (len(error) + len(error32bit) + len(errorNoEntry)), "Notices:", len(notice))
	print()


if __name__ == "__main__":
	main(sys.argv)