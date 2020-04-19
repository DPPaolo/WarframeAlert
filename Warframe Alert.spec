# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['warframeAlert\\Warframe Alert.py'],
             pathex=['C:\\Users\\Paolo\\OneDrive\\Miei Tool\\WarframeAlert'],
             binaries=[],
             datas=[
             ('warframeAlert\\assets\\icon\\*.*', 'assets\\icon'),
             ('warframeAlert\\assets\\image\\*.*', 'assets\\image'),
             ('warframeAlert\\translation\\*.qm', 'translation'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Warframe_Alert',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='warframeAlert\\assets\\icon\\Warframe.ico')
