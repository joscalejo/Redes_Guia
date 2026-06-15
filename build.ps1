$html = Get-Content -Raw -Path "c:\Redes_Guia\index.html"
$newMain = Get-Content -Raw -Path "c:\Redes_Guia\main_content.html"

# Regex to replace everything between <main class="main-content"> and </main>
$html = $html -replace '(?s)<main class="main-content">.*?</main>', "<main class=`"main-content`">`n$newMain`n    </main>"
$html | Set-Content -Path "c:\Redes_Guia\index.html" -Encoding UTF8
