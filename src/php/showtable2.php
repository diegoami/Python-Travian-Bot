<html><head><title>MySQL Table Viewer</title></head><body>
<?php
$db_host = 'db72a.pair.com';
$db_user = 'clickit_4';
$db_pwd = 'ZbdRUGEf';

$database = 'clickit_travianit9';
$table = 'BERICHTE';

if (!mysql_connect($db_host, $db_user, $db_pwd))
    die("Can't connect to database");

if (!mysql_select_db($database))
    die("Can't select database");
$server = $_GET['server'];
$likserver = '%'.$server.'%';

// sending query
$result = mysql_query("SELECT * FROM {$table}  where server_home like '{$likserver}'  order by id desc");
//$result = mysql_query("SELECT * FROM {$table}" );
// where server_home like \'%s4%\' 
	
if (!$result) {
    die("Query to show fields from table failed");
}

$fields_num = mysql_num_fields($result);

echo "<h1>Table: {$table}</h1>";
echo "<table border='1'><tr>";
// printing table headers
for($i=0; $i<$fields_num; $i++)
{
    $field = mysql_fetch_field($result);
    echo "<td>{$field->name}</td>";
}
	
echo "</tr>\n";
// printing table rows
while($row = mysql_fetch_row($result))
{
    echo "<tr>";

    // $row is array... foreach( .. ) puts every element
    // of $row to $cell variable
	$i = 0;
	while ($i < mysql_num_fields($result))
	  {
		$field_name=mysql_fetch_field($result, $i);
		if ($i == 1) {
			$link = $row[0]. "berichte.php?id=". $row[1] ;
			echo "<td><a href='$link'>" . $row[$i] . "</A></td>";  //Display all the fields on one line
		} else {
			echo "<td>" . $row[$i] . "</td>";  //Display all the fields on one line

		}

		$i++;
	  }


    echo "</tr>\n";
}
mysql_free_result($result);
?>
</body></html>