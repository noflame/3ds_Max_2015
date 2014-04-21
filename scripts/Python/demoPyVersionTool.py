version_data = {}

try:
    from sys import version, prefix
    version_data['sys module'] = True
    version_data['Python version'] = version
    version_data['Python prefix'] = prefix
except:
    version_data['sys module'] = False

try:
    import os
    version_data['os module'] = True
    version_data['3ds Max 2014 path environment variable'] = os.getenv("ADSK_3DSMAX_x64_2014")
except:
    version_data['os module'] = False

try:
    import MaxPlus
    version_data['MaxPlus module'] = True
    version_data['3ds Max install path'] = MaxPlus.PathManager.MaxSysRootDir
    version_data['MaxPlus version'] = MaxPlus.__version__
except:
    version_data['MaxPlus module'] = False

try:
    import PyQt4.QtCore
    version_data['PyQt module'] = True
    version_data['PyQt QT version'] = PyQt4.QtCore.QT_VERSION_STR
    version_data['PyQt version'] = PyQt4.QtCore.PYQT_VERSION_STR
except:
    version_data['PyQt module'] = False
    
try:
    import PySide 
    import PySide.QtCore
    version_data['PySide module'] = True
    version_data['PySide version'] = PySide.__version__
    # NOTE: if PyQt is loaded succesfully first, this may return a
    # different version of Qt if the PySide Qt is different.
    # it will just load the DLLs that it found.
    version_data['PySide Qt version'] = PySide.QtCore.__version__
except:
    version_data['PySide module'] = False

for key in sorted(version_data):
    print key, version_data[key]


