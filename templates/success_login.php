<?php


$s = file_get_contents('http://ulogin.ru/token.php?token=' . $_POST['token'] . '&host=' . $_SERVER['HTTP_HOST']);
$user = json_decode($s, true);

$myfile = fopen("newfile.txt", "w+")
fwrite($myfile, $user['first_name']);
fclose($myfile);

//$user['network'] - соц. сеть, через которую авторизовался пользователь
//$user['identity'] - уникальная строка определяющая конкретного пользователя соц. сети
//$user['first_name'] - имя пользователя
//$user['last_name'] - фамилия пользователя



header("Location: http://www.yourwebsite.com/user.php"); /* Redirect browser */
exit();


?>