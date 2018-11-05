<?php include('dict.php') ?>
<?php
session_start(); 
if(isset($_POST['formname'])){
  $_SESSION['formname1'] = $_POST['formname'];
  header('location: formview.php');
  exit;
}
 ?>
<!DOCTYPE html>
<html>
  <head>
<link rel="stylesheet" type="text/css" href="style.css">
    <title>Form list</title>
  </head>
  <body>
    <div>
      <?php foreach($forms as $form => $fields) { ?>
        <div>
              <h2><?php echo $form;  ?></h2> <br />
          <p>Some text inside the form</p><br />
          <form method="post" action="listform.php">
              <input type="hidden" name="formname" value="<?php echo $form ?>">
              <input type="submit">
          </form>
        </div>
      <br />
      <br />
      <?php } ?>
    </div>
  </body>
</html>
