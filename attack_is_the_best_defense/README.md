# Attack Is The Best Defence

### Welcome to this GitHub tutorial 😉. 

I'm excited to share this with you because some of my previous READMEs have been invaluable in guiding me through various challenges, like the one detailing SFTP usage to upload files from local servers to remote ones, found in my (`command_line_for_the_win`) repository.

But let's get straight to the point.

## Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

This task involves sniffing out a password. Initially, I reached out to ChatGPT for clarification since I didn't fully grasp the requirements. However, I was determined to solve it independently to experience that lowkey hacker thrill.

1. **Uploading the Script**: Leveraging my SFTP knowledge, I uploaded the provided script to my remote server, ensuring it landed in the appropriate directory (refer to `command_for_the_win repo` if confused or browse it, I recommend digital ocean).

2. **Using tcpdump**: Following the suggestion, I immediately ran `tcpdump` to monitor network traffic from the start:

    ```bash
    sudo tcpdump -i eth0 -w capture.pcap port 587
    ```

3. **Analyzing with tshark**: As the pcap file was binary, I utilized tshark to decode it. Upon decoding, I extracted the username and password. Since it was encoded using base64, I wrote a Python script (`decode.py`) to convert it to plaintext.

```bash
tshark -r <name of .pcap file>
```
4. **Simultaneous Execution**: Throughout the process, I ran multiple commands simultaneously in different windows, optimizing efficiency.

5. **Running the Main Code**: After ensuring the upload's success by verifying its presence with `ls`, I made the script executable (`chmod +x user_authenticating_into_server`) and executed it (`.\user_authenticating_into_server`).

This completes the rundown for Task 0. For further clarity, the full task description is provided below:

> Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).
>
> Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.
>
> In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.
>
> Sendgrid offers an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: telnet. You can create an account for free, which is what I did, and send an email using telnet:
>
> ```bash
> sylvain@ubuntu$ telnet smtp.sendgrid.net 587
> Trying 167.89.121.145...
> Connected to smtp.sendgrid.net.
> Escape character is '^]'.
> 220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
> EHLO ismtpd0013p1las1.sendgrid.net
> 250-smtp.sendgrid.net
> 250-8BITMIME
> 250-PIPELINING
> 250-SIZE 31457280
> 250-STARTTLS
> 250-AUTH PLAIN LOGIN
> 250 AUTH=PLAIN LOGIN
> auth login
> 334 VXNlcm5hbWU6
> VGhpcyBpcyBteSBsb2dpbg==
> 334 UGFzc3dvcmQ6
> WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
> 235 Authentication successful
> mail from: sylvain@kalache.fr
> 250 Sender address accepted
> rcpt to: julien@google.com
> 250 Recipient address accepted
> data
> 354 Continue
> To: Julien
> From: Sylvain
> Subject: Hello from the insecure world
>
> I am sending you this email from a Terminal.
> .
> 250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
> quit
> 221 See you later
> Connection closed by foreign host.
> sylvain@ubuntu$
> ```
>
> I wrote the script `user_authenticating_into_server` that performs the authentication steps that I just showed above. Your mission is to execute `user_authenticating_into_server` locally on your machine and, using `tcpdump`, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.
>
> DISCLAIMER: you will probably see Authentication failed: Bad username / password in the tcpdump trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!


## ATTENTION!!
I later figured out this blog and it helps as well even thought the difference is that I did task 1 using cli, while they did theirs with gui.

[Click to read the blog on this task especially for 2](https://medium.com/@polalekan/attack-is-the-best-defense-password-cracking-with-network-sniffing-and-dictionary-attack-72fbbf0aa272)
