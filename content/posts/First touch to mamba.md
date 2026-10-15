---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3H53UIK%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T020654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaihxKZJ%2BzXmE3wF2UHJzDjhZySiwLM5hOMXZmOx0eagIgFw3bGgpDxTe5cdcCDP6SqYGy9IIvHk9JsMzLWbo1Yg4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIe14eg5gWTI8wC11ircAxPGCOfXfKYlbqLXYRRR%2BsqkPn2q3L1dKFVRCEkoLl%2Fg%2FEsfjgnGy6dFfl%2BkHMm4laS0DLuADF2O0e5cAtsWDshLk1G1zoCd1iCjvhu78sZvdyekByXXQx3JzEj0xQKD0%2FFe36M%2Fk4Oo5B35JAmlX51mEHXurCIcGAc6P17UHyRlJN51Wq5QU26q5gBaX2TpjwiqQ5fjKWjXkJoQ3QSC5O6cv33mroJrLFRajKKUR8chANRGhWVYSUwUf2%2FkLywEAsWSmkAxPrMvXa8vMPuJM%2BegQ4SXewGRA8yAGCtzbjwKdQW1g%2FHBCyrkOU196ZkoHyzsyf8Vcm4GhYkX7eDaZLBUGF8MynsUm9RVhkJrrN50xgBmVZpl2txEaRapFIdlaghMclPUG1sd9VDNXrPZNZVS7aIBXU%2FLUHfMGiBHZK7nf9S3FkGz2ZSF5kjZdOtpeMeECnxhu%2FmzRRpq7Hi3TOe7yCCfsCS9lTMpq7PnCPvq1GeIt94y0TnTYa8ynTeviG46SNVbIjTArP4iwqEZGUrxFiehmQAB8RY1yaw%2FJtpOkeqP8w7Yj%2F3GQY0Wfx1JMG45CMeDvijSzyl9%2FArDkc%2FFoiX3dDj8OD%2Bp8ZUiwl%2BG4azGeGkfwq49qWbgMIHawNYGOqUBK2uXw1ja9osTMuTleWJhsPEz2TWs0l%2FUQ7d%2FzeWY2ZBW6qjXF7fClO8yNOuaqit%2FtkF7xH46IosWlfrvOe7w3bWktNV0nquFExTdUbug1jtYVOAi864z5FYX2xVBWJBMEPdQSZMl5vmWyQX2zKtpDTABQBk%2BBAiILhSyWWuN3pIM8d7XJQuerz6OnJJWJA5tlyipgJAyK08fv1kcp4e53mK6PM4S&X-Amz-Signature=8a8caf79843b607f74ef7d0959d3ec6aabc70219df3b7911900ebc922673c9dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
