@echo off
rem Create exe (Nuitka)
setlocal
.\.venv\Scripts\nuitka ^
    --msvc=14.3 ^
    --follow-imports ^
    --nofollow-import-to=tkinter ^
    --noinclude-unittest-mode=allow ^
    --noinclude-setuptools-mode=allow ^
    --no-deployment-flag=self-execution ^
    --windows-icon-from-ico=./res/console.ico ^
    --file-description="JSON formatting viewer" ^
    --file-version=1.2.0.0 ^
    --company-name="UJRC" ^
    --product-name="JsonViewer" ^
    --product-version=1.2.0 ^
    --copyright="Copyright (c) 2023-2025, UJRC (Takayoshi Tagawa)" ^
    --onefile ^
    --onefile-tempdir-spec="{TEMP}/{COMPANY}/{PRODUCT}" ^
    --output-file=jsonviewer.exe ^
    jsonviewer.py
