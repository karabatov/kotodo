%include header

<h1>Kotodo login</h1>

%if error:
<h2>{{error}}</h2>
%end

<form action="login" method="post">
<p>Username:&nbsp;<input name="username" type="text" size="16"></p>
<p>Password:<input name="password" type="password" size="16"></p>
<input type="submit" value="Login">
</form>

<p>Click <a href="register">Register</a> to create a new account!</p>

%include footer
