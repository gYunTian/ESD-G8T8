<?php
    session_start();
?>

<html>
    <h3>Hello, <?php echo ucfirst($_SESSION['username']); ?></h3>
    
</html>


