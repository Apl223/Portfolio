### Creating the script
* To change the password, we will have <input> elements inside a <form> element so that it will submit the values within.
* By inspecting the DVWA page for the <form> element, we can see that it uses the GET method, therefore our form element will have method="GET".
  You can of course find the method via proxy as well when intercepting packets.
* Our <form> will also need a URL to go to of course, so well copy the location of the CSRF page without the parameters: http://192.168.1.8/dvwa/vulnerabilities/csrf/
* As for our parameters, which will be passed via our <input> elements, you'll need to inspect the DVWA page and you will see that they set the new password with password_new and confirm it with password_conf. 
* Therefore our <input> fields will be named after those with the value being set as value="whatever value you want".
* Creating a scenario for a CSRF attack will involve inspecting the original site and the components you are trying to change - ie state changing requests.
