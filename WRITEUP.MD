Dear people of upper management

The following will be a walkthrough of the 42 Project 'Darkly', which is a docker image which hosts a very vulnerable website, full of angles which can be exploited.

The goal was to elevate priviliges and, on the way, collect up to 10 flags which were hidden in the website, usually only reachable through matters of exploitation.

It was said that the website had at least 15 vulnerabilities and 10 flags, of those, i have found, explained, and documented 14 vulnerabilities and 9 flags.

Now to begin the writeup.

After booting the image and connecting to http://localhost:4942 I was brought to the Homepage of "42".

As a Guest, i had access to the sublinks of /projects, /forum, /newsletter and /login.

In trying to elevate my privileges, I went through the sourcecode of the pages, which were full of comments of people arguing with each other,
downright hinting to work that should be done which had been largely ignored, or simply exposing vulnerabilities straight up.

The forum posts (which were also accessible to read with a guest account), hinted heavily towards bad password practice, with one user exclaiming:

"Hey Wilcity! New student here, finally set up my account 🎸

About me: I rock climb, I'm in a rock band, and I pretty much live for rock. You all rock too, honestly.

Real talk though — I never changed my signup password and I never will. It's short, it's classic, it rocks. Nobody's getting into my account — what are you gonna do, run every word in some giant list against me? 😎"

This was meant as a hint to be using the rockyou.txt to bruteforce this account.

**See step1**

After logging in, we were presented with the Account of Jdoe.

Jdoe's account was of the 'Student' rank.

This opened the ability to create forum posts, access the /agenda site, as well as the /profile/me/settings page which lets you customize your profile settings, as well as your profile picture.

Upon trying to upload a non-picture-file, we were presented with the first Flag, which was FLAG{unr3str1ct3d_upl0ad_g0_brrr} 

**See step2**

The /agenda site offered yet another way to upload files, however this time it was actually sort of 'validating' the files which were uploaded.

They gave an expected xml format like this:

<?xml version="1.0"?>
<agenda>
  <event>
    <title>Piscine day 1</title>
    <date>2042-01-15</date>
  </event>
</agenda>

Any File which didn't follow this format, was rejected as a parsing error.

In the sourcecode of this site, there was a comment which said:
"<!-- NOTE: /internal/config restricted to localhost only. do not expose. -->"
Upon trying to access this site through normal means, I was presented with a 403 forbidden error.

Pushing the boundaries with the file upload however, I managed to make it accept a script which was pointing towards a file I should not have access to as a Student.

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ANY [ <!ENTITY xxe SYSTEM "http://localhost:4942/internal/config"> ]>
<agenda>
	<event>
		<title>&xxe;
		</title>
	</event>
</agenda>

This presented me with the content of the restricted site in the Agenda Tab, abusing this function.
The content being:
"{"jwt_secret":"42network","pb_admin_email":"admin@42network.local","pb_admin_password":"Darkly42Admin!","app_version":"1.0.0","campus":"wilcity","darkly_flag":"FLAG{d3fus3dxml_n3xt_spr1nt_pr0m1s3}"}"

Giving us another flag, as well as, what seems to be admin credentials, which we don't have a use for quite yet.

**See step3**

Upon revisiting the forum pages, there was a post hinting towards the poor password-reset implementation.

citing:

"PSA: the 'forgot password' flow is… not great?
Locked myself out last night and used the password reset. The link worked instantly — no email, the token was just sitting in the URL. And get this: that token is literally the md5 of my email address. Took me ten seconds to spot. Anyone could reset anyone's account this way — and once they're in, your account recovery code is just sitting there on your profile settings page. Reported it, we'll see. 🙃"

It was easily confirmed, You can reset anyone account which are ranked student, without even waiting for a confirmation mail.
Even if you did have to wait for a confirmation mail, the reset token would be plainly visible in the link presented, which was just the email of the student, encoded in MD5.
Making it trivial to generate your own "reset-password confirmation link".

After trying another student's account, resetting the password, logging in successfully and visiting their profile page, we were presented with the next flag: FLAG{r3s3t_t0k3n_w4s_just_md5_lol}.

**See step4**

Inspecting the pages of the website a little more, upon visiting some staff's profile pages, on wil's page, you are presented with another flag.

🔒 Private note
FLAG{1d0r_ur_pr0f1l3_1s_m1n3}


**See step4.5**


Trying out a few common subsites, i stumbled upon robots.txt, which is used for telling compliant web crawlers which websites they should not crawl under.
Obviously, this can also be used as information to see which internal subsites are of potential interest.

Contents included:

User-agent: *
Disallow: /admin
Disallow: /staff
Disallow: /internal
Disallow: /backup
Disallow: /api/grades
Disallow: /_/
Disallow: /static/uploads/

Some of these sites were publicly available, such as /staff and /api/grades

On visiting /api/grades, i was presented with something akin to a datatable of projects, as well as a flag: 

"flag":"FLAG{md5_1s_4_n4m3pl4t3_n0t_4_l0ck}"

**See step5**


On visiting /staff I was presented with a dashboard, which held internal information, but also told me how to patch my account.

⚡ Staff dashboard
Manage students, view evaluation activity, monitor newsletter subscriptions and platform health.

Cadet access required. Try
PATCH /api/profile
with the right fields.

But even without patching anything there were plenty more angles to potentially attack later on:

📡 Platform status
FastAPI app
Running · port 4942
PocketBase
Running · port 8090
File uploads
Enabled (unrestricted)
XML parser
stdlib ET (unsafe)
Session cookie
httponly=false

The most important part here, was that Pocketbase was running on Port 8090 as a backend for this website.

But we will get to that later.

Going back to the patching, I managed to elevate the priviledges of jdoe to "Cadet", which granted me access to /staff/dashboard.

There was another flag: 
🔓 Cadet+ access granted — internal staff flag:
FLAG{just_p4tch_y0ur_0wn_r0l3_lol}

As well as 

🔗 Quick links
API users
↗
API grades
↗
API schema
↗
PocketBase /_/
↗
robots.txt
↗

**See step6**

Accessing the PocketBase /_/ direct link, redirected me to a login field on http://localhost:8090/_/#/login

Trying the credentials we got on step3, got me into the backend without any difficulties.

Here I now had admin access to the backend, which enabled me to manipulate records, change passwords of any users,
disables certain tokens, add or delete or change admin credentials. Anything imaginable except access on the local machine.

As such, on the backend there was a folder called internal_audit, which presented another flag.
god-tier export OK — flag retained for the security audit: FLAG{th3_und3rsc0r3_sl4sh_kn0ws_th3_w4y}

**See step7**








