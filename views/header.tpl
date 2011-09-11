<html>
<head>
<title>Kotodo!</title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>
<script type="text/javascript" src="static/jquery.timers-1.2.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    $("#additem").submit(function(event) {
        event.preventDefault();
        $.post("item/add", $("#additem").serialize(), function(data) {
            $("#items > ul").append(data);
            $("#additem")[0].reset();
        });
    });
    console.log("jQuery loaded!")
    $(".s_timer").click(function(event) {
        event.preventDefault();
        var itemid = this.href.split("/").pop();
        console.log("itemid: " + itemid);
        if (this.text == "Start timer") {
            $.post("item/timer/start", {"itemid": itemid}, function(data) {
                $(itemid + " > span").attr(name, data);
                $(itemid + " > span").everyTime(1000, itemid, function() {
                    console.log("Now in " + itemid + " timer!");
                    var seco = parseInt($(this).attr(name)) + 1;
                    $(this).text(seco);
                    $(this).attr(name, seco);
                });
                $(".s_timer." + itemid).text("Stop timer");
            });
        } else {
            $.post("item/timer/stop", {"itemid": itemid}, function(data) {
                $(itemid + " > span").text(data);
                $(itemid + " > span").stopTime(itemid);
                $(".s_timer." + itemid).text("Start timer");
            });
        }
    });
});
</script>
</head>
<body>
