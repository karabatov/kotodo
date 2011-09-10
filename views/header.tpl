<html>
<head>
<title>Kotodo!</title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function() {
$("#additem").submit(function(event) {
    event.preventDefault();

    $.post("item/add", $("#additem").serialize(), function(data) {
        $("#items > ul").append(data);
        $("#additem")[0].reset();
    });
});
});
</script>
</head>
<body>
