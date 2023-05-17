### Race Conditions
#
* Common programming mistake that allows for multiple requests to be executed at the same time.
  Happens when sections of code are executed out of sequence. It messes with **concurrency**, which is
  executing code simultaneously without affecting the outcome.
* **Multithreading** is the ability of a single CPU to provide multiple threads or concurrency. They dont
  really execut at the same time, they take turns using threads. When one thread is idle, other threads 
  can continue using unused resources. While one waits for input, another could execute its computations.
  Also called **scheduling**, the arrangement of execution of multiple threads.
* In practice, scheduling algorithims are unpredictable. So you won't know when they swap.
* Example: if you were to incremenent the value A to 2 with a starting value of 0, it would take these steps:
    * Read the value of 0
    * Increment the value
    * Write the value of 1
    * Back to step 1 until 2 is written
* However, if there was a race condition vulnerability, it would take these steps:
    * Read it twice first
    * Increase it twice
    * Write the value of 1 twice.
* Therefore, it only has the value of 1 instead of 2.
* **Race conditions happen when the outcome of one thread relies on the outcome of another**]
* **Also called time-of-check or time-of-us vulnerability**. Common in C/C++ apps.
* These are the steps that would be taken if this vulnerability happened on a bank app:
    *  Check your balance twice.
    *  Add x amount to the account twice.
    *  Deduct twice for a bank transfer.
* Race conditions could appear in voting or social media applications.
* Used for bypassing access controls or other vulnerabilities.
### Prevention
#
* Synchronization, resource locks, Principle of least privilege.
### Hunting for RCs
#
* Simple vulnerability, but requires some degree of luck. Look for features that involve calculating numbers.
* Copy HTTP request on Burp with **'Copy as curl command'**. The more requests you send within a short time frame, the luckier
  you'll get. Try a few times before giving up.
* Test for values that should be allowed once, not multiple times.
