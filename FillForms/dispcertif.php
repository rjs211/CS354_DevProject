<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title><?php echo $_SESSION['certifname'] ?></title>
  </head>
  <body>
<h1><?php echo $_SESSION['certifname'] ?> is ready</h1>
<iframe id="fred" style="border:1px solid #666CCC" title="<?php echo $_SESSION['certifname'] ?>" src="<?php echo $_SESSION['pathname'] ?>" frameborder="1" scrolling="auto" height="1100" width="850" ></iframe>
<p> <a href="index.php?logout='1'" style="color: red;">logout</a> </p>
  <p> <a href="listform.php" style="color: blue;">Certificates</a> </p>

  </body>
</html>
