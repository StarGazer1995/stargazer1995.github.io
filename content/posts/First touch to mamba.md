---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMB7GZQP%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T000424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDUM5LSDJTt%2BZS36RDLCLKdPw0x9%2F6C18xN6ZOV6Hc5nAIhAKicT3Y3h81pXwLBoPuyZtmtA92XvG%2B7Dmw4zvbLjA6MKogECPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwwtbFPTg182%2B8klYq3AMK0VBL3qqQdssofqMegT6uDpU1uX5DIOAuiNLC1Scp5m%2Fb7XwgWqxSwNYUZe5M2dkGZAEvMM1EBPeu6Q4aAe%2Bl0PGrc0Eabf7wj5pcknr4D49j9acDGygDNn%2BnBXnW%2FMRWXxk6FpJW5En%2B%2Bp8TopxjjQBlUO36kXXojy1yiFAbb0kDoskMjwe5YZUlC16x8XDexCTJAChhsaPfQQsn4PUpay9G4eNxSfW%2F0VRsENpgoDM68BujTdLlHhBFGcIxCRPsbHGiGceIWVYtxVLvVG0lpj%2Bw1YHmkMnd%2FUMI6ozg1xCcSdGhZ78dk0rHTjv%2BBlhqdD%2B%2Fa4c4d55GxHzEPZtXO9UNEdlBPQjrJRVAkHTQXGK9rXmvgL6QlGpvS2WxNjX35igUpuwrUJc9Rzmb9yMkXR6ALF8Tdpavu6GxbdcuUM38S%2BR8pmv9rbWN9viMkf9lciqbS5lZ3Z57GnyenyjsRESrOWfWPSXYXxpt9cGkYZDPbfCespl%2BUotEr03hrpd6IVOOlDgEd5AQ1zJvwvsRKdP0YnW3cpTwrMjoyu3ZMHXSXRKS%2Bd%2BwQSTPhGM%2BupMfvSuN1l2mJ2wDZ9eXs1hJJrmSPlEdrWDelNFktacf8Xos5QBH5MfqgIS2kzD3%2B6HVBjqkAf0ZCyWeL54Dj7Ii1x1SAKDvIiQPm0o7F%2F8YOL2ug8ihkTjK%2FqjiOdIkt1pxChgWnN6i5rA8hHmYLsaKSWmbWD4rWUozB2SZ3VK2YeSApF4pmHoOXXCIdtwovUIqYAdRCYU0uNhhjRoA9t%2F2HXb6eXio0vEXqu3EyPIphfhAayTUIdQVv0EMmkhRIY2NTNiNfu9buFgv9TY8nRKbeeyBb%2FVxjzUf&X-Amz-Signature=fd31200a4cbb62bf06e6c0faef304bd5ac9da411016d84020424297e306840fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
