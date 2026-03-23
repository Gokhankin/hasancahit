@echo off
title Otomatik GitHub Senkronizasyon Araci
color 0A
echo ========================================================
echo Hasan Cahit - Ani Kitabi Otomatik Yedekleme Baslatildi
echo ========================================================
echo.
echo 1/3: Klasordeki tum yeni/degisen dosyalar tespit ediliyor...
git add .

echo.
set /p msg="2/3: Bu yedekleme icin kisa bir not yazar misiniz? (veya bos birakip DIREKT ENTER'a basin): "
if "%msg%"=="" set msg="Yeni dosyalar eklendi ve duzeltmeler yapildi (Otomatik Yedek)"

git commit -m "%msg%"
echo.
echo 3/3: Dosyalar uzak sunucuya (GitHub) yukleniyor lutfen bekleyin...
git push origin master

echo.
echo ========================================================
echo ISLEM TAMAMLANDI! Tum projeniz ve zihnimiz (MEMORY BOOK KURALLARI) guvende!
echo ========================================================
pause
