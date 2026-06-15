$html = Get-Content -Raw -Path "c:\Redes_Guia\index.html" -Encoding UTF8
$mod1 = Get-Content -Raw -Path "c:\Redes_Guia\mod_01.html" -Encoding UTF8
$mod2 = Get-Content -Raw -Path "c:\Redes_Guia\mod_02.html" -Encoding UTF8
$mod3 = Get-Content -Raw -Path "c:\Redes_Guia\mod_03.html" -Encoding UTF8

$newMain = $mod1 + "`n" + $mod2 + "`n" + $mod3

$html = $html -replace '(?s)<main class="main-content">.*?</main>', "<main class=`"main-content`">`n$newMain`n    </main>"
$html | Set-Content -Path "c:\Redes_Guia\index.html" -Encoding UTF8
