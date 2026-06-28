---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEH3UHA%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T190040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSpLtTqWALZh219ot1pHdmwcVyH2Nuh6NZcpm3uibJ1QIhAJE7OC6aXzspDXMM2ikYhOvma%2BqafzUdHAF3q%2Fw24lwdKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOYBsLDdpDjUBc10wq3ANPywKlsXX06VoB8%2Bkskwv8VkzVauGuGht9cdY3fJth1g2930tyZ5pTbMjWlVrUEj2Ef8m9cDXFc8OsjuapD2BWmMAADJ%2BBbo%2FA1qk19zW7e%2FBSLICpnNqoZwg4Ux%2FjRTsBQwYOCjjKFbHhSrGKsnwEoJl%2BP5J2nYZPmir3JT6cCzfnptf5cqCxac%2BnKQB5bmXLIyjtFGcDjsZgxbZ9C%2BsOB5HoCpWfXIUNrXStzBUt4ncTXmHYNp3GLKMmF8xxdqtKA1J9mStg8dZ%2BI%2BfJX%2BVncKHdKnQwrg8zs6Uz0O%2F22hcjmkm2wJYUgPW4lg4c%2BjrMWj4VvrbM2AfVeg0TpPt7V53Txnbml6fOCfClh318fGc4KZLjGqmR1ubEkf0ZGegMKyqDnMxgBhec%2Bcf6o4tyINe%2BOx2HHgoiDW1JoTFyVUBsiRihMISu2f%2FdZToyGUFR4jLI9XBuXqiKO%2BDMSIBYUvD%2FZbdd2poFx5sDb5aBjj9bSblq9e0RA14rKuHZSg4SUvOwKUrU0h5HpDcdXZYOkNUcf0%2FTPAHGcWXR6daZo7MWLnp1PmX8E9YOUeND5CX6JctHzqQiS0MhYYUE7rO8%2BhkRzGfXj73PkG2onoqq7tJUTQQwy0FGTiBXjTCLsoXSBjqkAS5DJIKkEngLxVas2xNTM1cayG26UeuXayHBV6Vhfr9YLEbzpLZqgz3EJ9GoFlw8dfulXGjsVz0CgNaEx8e2h%2FHTd4ui88qnP8PgJNhspmIpmZk0S6sgBTQeOGcNFcyod6LJVAuuKhbT2fva1p42KIt0zfooRIh0zPN7s4BKjh1YFJ6gkZrfzySjvYa0HJJkT34pu764wh4PAliFy8iqv4nAxZ7W&X-Amz-Signature=a1130b3a64188dca44683d2273babd7fe86a44ef712bb3c4e4e9dc170dcb90c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
