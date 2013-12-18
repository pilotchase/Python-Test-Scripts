# Prints info about the OS you're using
# Made for the sake of refreshing my memory on Python coding
import os
import platform
import sysconfig

print("OS Name:", os.name, "\nmore specifically,\n", platform.platform(aliased=1, terse=0) )

print( "\nLogin Name:", os.getlogin(), "\nUser's ID:", os.getuid() )

print("\nDefault Search Path for Executables:", os.defpath)

print( "\nUsing Python version:", sysconfig.get_python_version() )
