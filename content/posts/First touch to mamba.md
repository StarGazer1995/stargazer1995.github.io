---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJDZUQ6U%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T162150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHyKLf3UKHV3WDqunffviiNCWnpLWVrFFDuy0MaVCwZQIhAOKiCWeD49Kvc8MHwisEa8gX4OHwzwtnTz60Tj1X6qhwKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwUeFA0oHPm2ADObAq3ANuqugPtesOShSne3O7kYx8czzPGLO7VoUdHE0bDdQ7XCF1crmbfAdAS9MslVnrv7JFJbhHMI9Hjdu8YB4rkwWJ1a3km%2FmHyrGifz4yTHYPAYTEyQIvzyvaIuwySma3rjz4%2B9ju2SlwyapdcyaefScBcsNlbjz%2FjF1zjLO9Z8DaaKVN3Ws5FsZr0O8kKF47ni3aKWITUfH6xAtKF3duILLDA96ml3TeaPKC%2FtmllCDE%2FRwxo8yIcCT3iYWNE%2FkYDHuGb%2FwMdtpmFsvnP02F7mmpseQfta6rzQd8iITclVVKhuzaBE3DufY%2Fm70gT2aqWuKAC%2Bh7IMO4DD0LpIf5psv5XgUZP1%2BidStjaZvFjy7GuAu%2Fz0UtTv6OJ7IR0urZrPppBUs7QpRPqtEZkHYMttzPfgja%2FEp2VbB%2BTxK0YCPL8OsYSkNhQdAyve5lejThyYaQtS2nzCfmdHKRpPusyYhTFp2vPFv%2FFxqp4KC8ayWBxD7LWjNv%2Fj%2FIeRyZrMAjfSyUxjV5GQzqDayuH2vjNvDt%2Fm60%2FaytN2bSxmDnrdcXKBKfKkwB%2BOC7sW0jOrJJVCtwE15CQmWkVkBpiCLPkFyX8WGI1uEtGwaF4Hevpbe6KZmUEAsNDhr7PGbMEzD78L7SBjqkAZyX2zsy8dI5N%2BGd6%2BXEUyTLhl1IJXhEdk2a%2B9uc73b7scLguz5SgZLAs%2B6tW5KhVMe7OaAYiUUpPZHR1mA%2FpIKX2kGT3TbKE3JUSqslCm0HTr3LwKY%2F3GZLhdSW3iKMnSJVKMdvzWBN6EQ5glcq2wkjI95Rrf5PJxeUT7uCNPsB%2FqN1vjTI%2BboghToMeR0Qee7ONW179%2BXKQquXOFgSaII90hZ%2F&X-Amz-Signature=0104179bcc199b974077899fdc49e15add249a6d8b56e928e570f9601640b5f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
