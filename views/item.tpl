%from kitems import hms, dlt
%from datetime import datetime
%if todo.get('tr', False):
%ts = int(todo.get('ts', 0)) + dlt(todo.get('cs'))
%else:
%ts = int(todo.get('ts', 0))
%end
<li class="ili {{todo.get('_id')}}"><span id="{{todo.get('_id')}}">{{hms(ts)}}</span> <span>{{todo.get('t')}}</span> <a class="i_edit {{todo.get('_id')}}" href="#">Edit</a> <a class="s_timer {{todo.get('_id')}}" href="#/{{todo.get('_id')}}">\\
%if todo.get('tr', False):
Stop timer\\
%else:
Start timer\\
%end
</a>
<a class="delete {{todo.get('_id')}}" href="#/{{todo.get('_id')}}">Delete</a>
<input type="hidden" class="hinput {{todo.get('_id')}}" name="ts" value="{{ts}}" /></li>
