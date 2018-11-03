<?php include('dict.php') ?>
<?php foreach($forms as $form => $fields) { ?>
    <p><?php echo $form;  ?><p><br />
<?php } ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">

<link rel="stylesheet" type="text/css" href="style.css">
    <title>Form list</title>
  </head>
  <body>
    <div>
      <?php foreach($forms as $form => $fields) { ?>
        <div>
              <h2><?php echo $form;  ?></h2> <br />
          <p>Some text inside the form</p><br />
          <form method="post" action="formview.php">
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
