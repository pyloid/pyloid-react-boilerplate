# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src-pyloid/main.py'],
    pathex=[],
    binaries=[],
    datas=[('src-pyloid/icons/', 'icons/'),
             ('build/', 'build/'),
             ],
    hiddenimports=['PySide6.QtWebEngineCore'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6.QtQml', 'PySide6.QtTest', 'PySide6.Qt3D', 'PySide6.QtSensors', 'PySide6.QtCharts', 'PySide6.QtGraphs', 'PySide6.QtDataVisualization', 'PySide6.QtQuick', 'PySide6.QtDesigner', 'PySide6.QtUiTools', 'PySide6.QtHelp'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pyloid-app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pyloid-app',
)
app = BUNDLE(
    coll,
    name='pyloid-app.app',
    icon='src-pyloid/icons/icon.icns',
    bundle_identifier=None,
)