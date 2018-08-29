<html>
<head>
<style>
body {
background-color: black;
color: chartreuse;
}
input {
background-color: hotpink;
color: bisque;
}
</style>
</head>
<center>
<marquee direction="down" style="height:100vh">
<?php
if ($_SERVER["REQUEST_METHOD"] === "GET") {
echo "<marquee><h2 style=\"text-color:red\"> WYKRYTO NIEAUTORYZOWANEGO UŻYTKOWNIKA </h2></marquee>";
echo "<marquee><h1 style=\"text-color:yellow\"> ZALOGUJ SIĘ </h1></marquee>";
echo "<form action=\"/\" method=\"post\">";
echo "L0gin: <input type=\"text\" name=\"login\"> <br>";
echo "P@ssw0rd: <input type=\"password\" name=\"password\">";
echo "<br>";
echo "<input type=\"submit\">";
}

//TODO Use some safer seed

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if ($_POST['login'] === "mariusz" && md5($_POST["password"] . "SEED_SEED") === "8c4a3d07f8c353bbaff7b2e5e0890d3f") {
        echo file_get_contents("/flag");
    } else {
        echo "<merquee><h1 style=\"text-color:red\">Do you think like you type?</h1></merquee>";
    }
}
?>
</marquee>
</center>
</html>
