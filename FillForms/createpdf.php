<?php

include 'server.php';
include 'funct.php';
//
// if(!isset($_POST['prev_page'])){
//   header('location: listform.php');
// }
// else{
//   unset($_POST['prev_page']);
// }

$formname = $_SESSION['formname1'];
$formfields = $forms[$formname];
$random = rand(100000,999999);
$foldername = $_SESSION['username'] . $formname ."_" . $random;
$dir = getcwd();
$dirpath =  $dir."/".$foldername;
$orgpath = $dir."/origcertifs/".$formname.".odt";
mkdir($dirpath, 0777, true);
$formpath =  $dir."/".$foldername."/". $formname .".odt";
shell_exec("cp ".$orgpath." ".$dirpath);
shell_exec("unzip -d ".$dirpath." ".$formpath);
$dom=new DomDocument();
$dom->preserveWhiteSpace = false;
$dom->load($dirpath."/content.xml");
// The function doesn't return any value


foreach ($formfields as $field) {
  $username = mysqli_real_escape_string($db, $_SESSION['username']);
  $f = mysqli_real_escape_string($db, $field);
  $query = "SELECT $f FROM users WHERE username = '$username'";
  $results = mysqli_query($db, $query);
  $row = mysqli_fetch_assoc($results);
  $replace = $row[$field];
  $search = $placeholders[$field];
  domTextReplace($search, $replace, $dom, $isRegEx = false);
}

//Now the text is replaced in $doc
$dom->save($dirpath."/content.xml");
shell_exec("rm ".$formpath);
chdir($dirpath);
shell_exec("zip -r " . $formname . ".odt mimetype .");
chdir($dirpath);
echo shell_exec("chmod -R 777 .");
putenv('HOME=/tmp');
putenv('LD_LIBRARY_PATH');
$result = shell_exec("libreoffice --headless --convert-to pdf:writer_pdf_Export ".$formname.".odt  2>&1");
echo shell_exec("chmod -R 777 .");
$_SESSION['pathname'] = "http://localhost/FillForms/". $foldername .  "/" .$formname. ".pdf";
header('location: dispcertif.php');
  ?>
