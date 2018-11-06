<?php
$dir = getcwd();
putenv('HOME=/tmp');
putenv('LD_LIBRARY_PATH');
$result = shell_exec("libreoffice --headless --convert-to pdf:writer_pdf_Export form1.odt  2>&1");
echo $result;
 ?>
