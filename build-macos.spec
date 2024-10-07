# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['src-pylon/main.py'],
             pathex=[],
             binaries=[],
             datas=[('src-pylon/icons/', 'icons/'),
             ('src/', 'src/'),
             ],
             hiddenimports=['PySide6.QtWebEngineCore'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pylon-app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='src-pylon/icons/icon.icns',
)

app = BUNDLE(
    exe,
    name='pylon-app.app',
    icon='src-pylon/icons/icon.icns',
    bundle_identifier=None,
)