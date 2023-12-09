So It was part of the task to create a tutorial per se on how to use thhr SFTP to upload files, so with that being said, let's get into it.

WELCOME TO MY GITHUB CHANNEL :)

The first step I took was to read through this blog:
- https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server

Then asked any extra questions I had to the web and chat gpt before starting

Now for the steps I took to first of all secure a connection between my local command line that is my pc's command line was to generate a keygen

``` bash
	ssh keygen
```

I do not know if it is meant to be stfp or ssh but i used ssh first to generate the key gen.
The n it will bring out an option on where you want the private id to be saved, you can use the default or specify the path, I let mine be in the root. 
Then it will ak for a paraphrase, for some reasons I did not use it. You ca check it out and know if it is something you might want to use.

The next step I took was to create the connection using the command

``` bash
	sftp username@hostname
```
Replace with your actual username and hostname. I am doing the alx course so there is one provided so we can connect to our sandbox from our local comandline.

After it a password will be requested.

Once that is provided, voila, you have created the connection.

In the blog there, there are command samples you can use to see the things you can do with your sftp.

In my own case, I uploaded an image file from my local repo.

How?

I went to the path i wanted to upload the image to on my sandbox which was opened through the stfp using the 'cd' command.
Then I confirmed the path using 'pwd'.
Next, I copied the absolute path of the image files I wanted to upload then used the 'put' command like this:

``` bash
	put filename
```

This automatically uploaded the file from my local repo, to the sandbox's directory I was in.
After this, I was able to push the image to github.

You're welcome *wink* *wink*
