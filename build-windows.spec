# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['src-pylon/main.py'],
            pathex=[],
            binaries=[],
            datas=[('src-pylon/icons/', 'icons/'),
            ('src/', 'src/'),
            ],
            hiddenimports=[],
            hookspath=[],
            hooksconfig={},
            runtime_hooks=[],
            excludes=['PySide6.QtQml', 'PySide6.QtSql', 'PySide6.QtTest', 'PySide6.Qt3D', 'PySide6.QtSensors', 'PySide6.QtMultimedia', 'PySide6.QtCharts', 'PySide6.QtGraphs', 'PySide6.QtDataVisualization', 'PySide6.QtQuick', 'PySide6.QtBluetooth', 'PySide6.QtLocation', 'PySide6.QtDesigner', 'PySide6.QtUiTools', 'PySide6.QtHelp', 'PySide6.QtXml', 'Pyside6.QtOpenGL', 'Pyside6.QtPDF'],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
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
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src-pylon/icons/icon.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pylon-app'
)
