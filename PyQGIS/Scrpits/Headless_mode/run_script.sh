OLD_PATH=$PATH
OLD_PYTHONPATH=$PYTHONPATH

QGIS_VERSION="QGIS-LTR"

export PATH=/Applications/$QGIS_VERSION.app/Contents/MacOS/bin:$PATH
export PYTHONPATH=/Applications/$QGIS_VERSION.app/Contents/Resources/python/:/Applications/$QGIS_VERSION.app/Contents/Resources/python/plugins
export QGIS_PREFIX_PATH=/Applications/$QGIS_VERSION.app/Contents/MacOS
export QT_QPA_PLATFORM_PLUGIN_PATH=/Applications/$QGIS_VERSION.app/Contents/PlugIns/platforms/
export DYLD_INSERT_LIBRARIES=/Applications/$QGIS_VERSION.app/Contents/MacOS/lib/libsqlite3.dylib
echo "Using python3 from $(which python3)"

python3 Download_and_process1.py

# restore and clean up
export PATH=$OLD_PATH
export PYTHONPATH=$OLD_PYTHONPATH
unset QT_QPA_PLATFORM_PLUGIN_PATH
unset DYLD_INSERT_LIBRARIES