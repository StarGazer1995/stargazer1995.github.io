---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRVZWVVD%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T141239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQChgRTAp86pLJrjO0y1IxAuvKv7xCRIWiZtyx9IBQUt6wIhAOYySxWRmQGl83lsSe1x9YW7xjchUmmiq7nnZtkh4M%2FHKv8DCCsQABoMNjM3NDIzMTgzODA1Igy6pPRYzXEgvic8Ogsq3AMH1PwZSEE3bVFfsuUuddhmiIYwaPCd54oy0IpplpGFw%2BddGtDxodWXXBjtgnUs56PudI2jV8qqUqLqG4AR3%2F7eCcLG0nHH0gkR8qzqtL40e1n2agwqxO2vaP5Eh7vYotsbXFUSoj1HY4Z7FSSy8ygsN%2FqPIElxLwTLi%2FMmrNVb1%2Fkegi1%2BENHyzTGsvd4Q8PX7yyK0wgVvnjj3lySWcn7sQ8VUBwkcAEsj8MbV9kPy0U%2F0fAbkdf7jF4NqqvKJ1JuGkWFwshp62EhuuWdcmsoRmZFnXYQl9SijIhVxhC0OYBXVVw9syqpOjer%2B0H0g%2F6wCkU48CYahJMiJajcsW2wEESBuF7G0uA0nUcKwSv2p7CgVN3pjQUO1bVDnX4ryjW0onaJ%2BGzBWhj5JNzeGShppMf4SKnmFJcZ2%2B4T9QWNLdjjPWUKtIWtzhq8Kd%2FL81pqXU60XqTk1oW37EAQtiWnGDi%2FQke8MnhsNDrItBNRVNxPV9VDlnazIuXWObV1cFHZ0YX0rNiYMiP5BXUBuJAIxc38HIW5JryfZzC70XIe7DaEVkKs%2Bjv3l%2Fe9yVADrw8VAyVeKIDgplmdRTvkmII0LFnNcjJIwTAjt83kE71C%2BJrsJFNvpx54dUNvNsTDsoIbUBjqkAbefOITgvKdXkOw2y5mUmwe%2FsLE0q%2BmDiUBqppMDNwgkTRhcVIlVHv6lYxQ6KzNuTtln3lnhadDK3r1Ics%2FwI67I3xxYl9r2vFMb7tVQXmZUi9FHvXkDnV1OZbI7xVgqn6rabM27rRTRciYuzAcX%2BsxmyIXmX5jsdf%2BvQYXQoHwb0iUr6NkTseDUCgRw0CpWBl2K%2BP9CDXEayqdCv1mhBP1KXIcw&X-Amz-Signature=9b7535e5eddcbfde4569169d32d9d4a6709e3f80687ea21cb7f140a0c93f4bf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
