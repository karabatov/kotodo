%from kitems import hms
%include header

<h1>{{username}}'s kotodo list!</h1>

<div id="items">
<ul>
%for todo in items:
%include item todo=todo
%end
</ul>
</div>
<form id="additem" action="item/add" method="post">
<input type="text" name="text" size="140">&nbsp;<input id="addbutton" type="submit" value="Add">
<input type="hidden" name="owner" value="{{username}}">
</form>

%include footer
