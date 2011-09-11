%from kitems import hms, dlt
%from datetime import datetime
<li><span id="{{todo.get('_id')}}">\\
%if todo.get('tr', False):
{{hms(int(todo.get('ts', 0)) + dlt(todo.get('cs')))}}
%else:
{{hms(int(todo.get('ts', 0)))}}\\
%end
</span> <span>{{todo.get('t')}}</span> <a class="i_edit {{todo.get('_id')}}" href="#">Edit</a> <a class="s_timer {{todo.get('_id')}}" href="#/{{todo.get('_id')}}">\\
%if todo.get('tr', False):
Stop timer\\
%else:
Start timer\\
%end
</a>
<a class="delete {{todo.get('_id')}}" href="#">Delete</a></li>
