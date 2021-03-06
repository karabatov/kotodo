function hms(seco) {
	var hours=Math.floor(seco/3600); 
	var minutes=Math.floor(seco/60)-(hours*60); 
	var seconds=seco-(hours*3600)-(minutes*60);
	if (hours < 10) { hours = "0" + hours.toString() };
	if (minutes < 10) { minutes = "0" + minutes.toString() };
	if (seconds < 10) { seconds = "0" + seconds.toString() };
	return hours+"h "+minutes+"m "+seconds+"s";
}
function startTimer(itemid) {
$("span#" + itemid).everyTime(1000, itemid, function() {
	//console.log("Now in " + itemid + " timer!");
	//console.log("input val = " + $("input.hinput." + itemid).val());
	var seco = parseInt($("input.hinput." + itemid).val()) + 1;
	//console.log("seco = " + seco);
	$(this).text(hms(seco));
	$("input.hinput." + itemid).val(seco);
});
}
$(document).ready(function() {
    $("#additem").live("submit", function(event) {
        event.preventDefault();
        $.post("item/add", $("#additem").serialize(), function(data) {
            $("#items > ul").append(data);
            $("#additem")[0].reset();
        });
    });
    //console.log("jQuery loaded!")
    $(".s_timer").live("click", function(event) {
        event.preventDefault();
        var itemid = this.href.split("/").pop();
        //console.log("itemid: " + itemid);
        if (this.text == "Start timer") {
            $.post("item/timer/start", {"itemid": itemid}, function(data) {
                console.log("data = " + data);
                // 4e6d39d4fc4e0710e1000000
                $("input.hinput." + itemid).val(data);
                startTimer(itemid);
                $(".s_timer." + itemid).text("Stop timer");
            });
        } else {
            $.post("item/timer/stop", {"itemid": itemid}, function(data) {
            	//console.log("data = " + data);
                $("span#" + itemid).text(hms(parseInt(data)));
                $("span#" + itemid).stopTime(itemid);
                $(".s_timer." + itemid).text("Start timer");
            });
        }
    });
    $(".delete").live("click", function(event) {
        event.preventDefault();
        var itemid = this.href.split("/").pop();
        var answer = confirm("Delete item ?");
        if (answer == true) {
			$.post("item/delete", {"itemid": itemid}, function(data) {
				// 4e6d39d4fc4e0710e1000000
				if (data == "ok") {
					$("li.ili." + itemid).fadeOut(500, function() { $(this).remove(); });
				}
			});
		}
    });    
    $(".s_timer").each( function() {
    	if (this.text == "Stop timer") {
    		var itemid = this.href.split("/").pop();
    		startTimer(itemid);
    	}
    });
});
