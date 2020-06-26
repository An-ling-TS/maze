# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['G:\\python\\pro\\maze\\py_', 'G:\\python\\pro\\maze'],
             binaries=[],
             datas=[('G:\\python\\pro\\maze\\resource\\music\\*','resource\\music'),('G:\\python\\pro\\maze\\resource\\picture\\item\\*','resource\\picture\\item'),('G:\\python\\pro\\maze\\resource\\role\\picture\\*','resource\\role\\picture'),('G:\\python\\pro\\maze\\resource\\picture\\tips\\*','resource\\picture\\tips'),('G:\\python\\pro\\maze\\resource\\picture\\wall\\*','resource\\picture\\wall'),('G:\\python\\pro\\maze\\resource\\picture\\1.jpg','resource\\picture'),('G:\\python\\pro\\maze\\resource\\picture\\robot\\dlam.png','resource\\picture\\robot'),('G:\\python\\pro\\maze\\resource\\picture\\robot\\images\\*','resource\\picture\\robot\\images')],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
