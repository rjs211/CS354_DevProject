

<?php include('server.php') ?>
<?php include('dict.php') ?>

<?php $formname = $_POST['formname'];
      $formfields = $forms[$formname];
 ?>

<!DOCTYPE html>
<html>
<head>
  <title>Filling <?php echo $formname;?></title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div class="header">
  	<h2><?php echo $formname;?></h2>
  </div>

  <form method="post" action="server.php">
  	<?php include('errors.php'); ?>

    <?php foreach ($formfields as $field) { ?>
    <div class="input-group">
  		<label><?php echo $field ?></label>
      <?php
            $username = mysqli_real_escape_string($db, $_SESSION['username']);
            $f = mysqli_real_escape_string($db, $field);
            $query = "SELECT $f FROM users WHERE username = '$username'";
    	      $results = mysqli_query($db, $query);
            $row = mysqli_fetch_assoc($results);
       ?>
  		<input type="text" name="<?php echo $field ?>" value="<?php echo $row[$field] ?>">
  	</div>
    <?php } ?>
  	<div class="input-group">
      <?php $_SESSION['formname'] = $formname ?>
  		<button type="submit" class="btn" name="form_sub">Submit</button>
  	</div>
  </form>
</body>
</html>
