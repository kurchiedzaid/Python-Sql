<?php

$connect = mysqli_connect("localhost","root","","bookstore");

if(mysqli_connect_errno($connect))
{
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else
{
    echo "success";
}

$title = isset($_POST['title']) ? $_POST['title'] : '';

$author= isset($_POST['author']) ? $_POST['author'] : '';

$price= isset($_POST['price']) ? $_POST['price'] : '';

$stock = isset($_POST['stock']) ? $_POST['stock'] : '';

$desc= isset($_POST['description']) ? $_POST['description'] : '';

$type= isset($_POST['type']) ? $_POST['type'] : '';
$dateAdded= isset($_POST['dateAdded']) ? $_POST['dateAdded'] : '';

$query = mysqli_query($connect, "insert into books (title,author,price,stock,description,type,dateAdded) values ('$title','$author','$price','$stock','$desc','$type',now()) ");

mysqli_close($connect);
?>