@echo off
set "baseDir=C:\Users\Administrator\Documents\My Games\vcmi\Mods\h3-themes"
for /r "%baseDir%" %%f in (*.bmp) do (
    echo Converting "%%f" to PNG...
    magick "%%f" "%%~dpnf.png"
)
echo Conversion completed!
pause