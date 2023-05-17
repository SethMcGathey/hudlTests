# hudlTests

<p>To run these tests, clone the repo.</p>

<p>Go to your terminal and install all needed requirements by running 
 
```
pip install -r requirements.txt
```

<p>If using pip3 use the below instead</p>

```
pip3 install -r requirements.txt
```
 
<p>Navigate to the "Tests" folder with </p>

 ```
cd Tests
```

<p>Finally, run 
  
```
python -m test_login_page
```
 
<p>If using python3 use the below instead</p>

```
python3 -m test_login_page
```

<p>I have set this up with a generic password to avoid the need for you to change anything in the code.</p>

<p>You should see the browser open to run the following tests.</p>
<p><b>test_unauthenticated_user_cannot_access</b></p>
<p><b>test_valid_login</b></p>
<p><b>test_invalid_username_valid_password</b></p>
<p><b>test_invalid_password_valid_username</b></p>
<p><b>test_no_password_valid_login</b></p>
<p><b>test_no_username_valid_password</b></p>
<p><b>test_no_username_no_password</b></p>
<p><b>test_remember_me_checkbox</b></p>
<p><b>test_signup_link</b></p>
<p><b>test_back_button</b></p>

<p>The <b>test_remember_me_checkbox</b> test fails currently because it does not seem to perform the actions that I would expect a Remember Me checkbox to perform. I wrote the test to check what I would expect of a Remember Me checkbox.</p> 
