# -*- mode: python -*-
import os
from PyQt5 import *
block_cipher = None


a = Analysis(['builder.py'],
             pathex=['C:\\Users\\mitgobla\\Documents\\Python\\Flash-Builder'],
             binaries=[],
             datas=[(os.path.join(q_library_info['DataPath'], 'lib', 'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app', 'Contents', 'MacOS', 'QtWebEngineProcess'), os.path.join('PyQt5', 'Qt', 'lib', 'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app', 'Contents', 'MacOS')),],
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
          name='builder',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='flash-software-128.ico')
