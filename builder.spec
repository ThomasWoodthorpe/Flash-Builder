# -*- mode: python -*-
import os
from PyQt5 import *
from PyQt5 import QtCore
block_cipher = None

SCRIPT_DIR = os.path.dirname(os.path.realpath('__file__'))
#(os.path.join(QtCore.QLibraryInfo.LibraryLocation(QtCore.QLibraryInfo.DataPath), 'lib', 'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app', 'Contents', 'MacOS', 'QtWebEngineProcess'), os.path.join('PyQt5', 'Qt', 'lib', 'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app', 'Contents', 'MacOS')),
a = Analysis(['builder.py'],
             pathex=[SCRIPT_DIR],
             binaries=[],
             datas=[('.\\Ui_about.py', '.'),('.\\Ui_builder.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='FlashBuilderLaunch',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='flash-software-128.ico')
