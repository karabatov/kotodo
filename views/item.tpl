%from kitems import hms
<li><span id="{{todo[u'_id']}}">{{hms(int(todo.get(u'time_spent', 0)))}}</span> <span>{{todo[u'text']}}</span> <a class="i_edit {{todo[u'_id']}}" href="#">Edit</a> <a class="s_timer {{todo[u'_id']}}" href="#">Start timer</a> <a class="delete {{todo[u'_id']}}" href="#">Delete</a></li>
