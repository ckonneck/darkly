Vulnerabilities Found

1. Unrestricted File Upload
No file type validation on the avatar upload endpoint. Any file extension accepted, including .js.

2. Path Traversal (Directory Traversal)
/projects/download?file=../private_notes.txt — single-level ../ traversal reads files outside the intended directory. Multi-level blocked but single-level confirmed exploitable.

3. Cross-Site Scripting (XSS)
Newsletter confirmation page echoes the email parameter directly into HTML unescaped. <script> tags execute in any browser that visits the confirmation URL, including the moderator bot.

4. Insecure Direct Object Reference (IDOR)
Profile pages accessible by user ID with no ownership check — /profile/xxv1btvtzaxen5h readable by anyone, exposing private fields.

5. Insecure Password Reset
Reset token is md5(email) — deterministic, guessable, never expires. Anyone knowing a target's email can reset their password instantly without inbox access.

6. XML External Entity Injection (XXE)
Agenda import parses user-supplied XML using stdlib xml.etree with external entities enabled. SYSTEM entity fetches arbitrary URLs server-side, bypassing localhost restrictions — used to read /internal/config.

7. Weak JWT Secret
JWT secret is 42network — 9 bytes, well below the 32-byte minimum recommended for HS256. Tokens are forgeable by anyone who finds or brutes the secret.

8. Sensitive Data Exposure via HTTP Headers
/backup endpoint leaks internal infrastructure details in response headers even on 403: rsync version, backup schedule, destination path, excluded files.

9. Insecure Direct Object Reference on Role Escalation
/api/patch endpoint allows users to modify their own role field directly — a student can elevate themselves to cadet role via a simple PATCH request.

10. MD5 Used for Security-Critical Hashing
Password hints stored as raw MD5 hashes in user records. MD5 is cryptographically broken, trivially reversible.

11. Information Disclosure via HTML Comments
Source code comments in production HTML reveal internal architecture, TODO items, deployment history, known unpatched vulnerabilities, and developer arguments about security decisions.

12. Open Debug Endpoint (/api/collect)
Unauthenticated logging endpoint left in production. Accepts arbitrary data via GET parameter and returns everything logged — functions as a free exfiltration sink for XSS payloads.

13. Weak Default Credentials / Plaintext Secrets in Config
/internal/config stores JWT secret, PocketBase admin credentials, and app secrets in plaintext, accessible via XXE or localhost bypass.

14. Missing HttpOnly Flag on Session Cookie
Session cookie readable via document.cookie in JavaScript — confirmed by successfully stealing it via XSS.

Flags Found: 9/10

upload - flag							FLAG{unr3str1ct3d_upl0ad_g0_brrr}
api/patch - flag 						FLAG{just_p4tch_y0ur_0wn_r0l3_lol}
email reset - flag(through pocketbase) 	FLAG{r3s3t_t0k3n_w4s_just_md5_lol}
xml - flag and admin creds 				FLAG{d3fus3dxml_n3xt_spr1nt_pr0m1s3}
pocketbase - flag 						FLAG{th3_und3rsc0r3_sl4sh_kn0ws_th3_w4y}
forum comments xss - ref txtfile		FLAG{d0t_d0t_sl4sh_4ll_th3_w4y_d0wn}						
forum /api/collect      				FLAG{xss_st0r3d_1s_n0t_4_f34tur3_w1l}
flag on wils profile?					FLAG{1d0r_ur_pr0f1l3_1s_m1n3}
api/docs/internal						FLAG{md5_1s_4_n4m3pl4t3_n0t_4_l0ck}