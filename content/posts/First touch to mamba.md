---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6ZRHGMV%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T082337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7UqdA1tU%2BYzT1KMdOFajv5zUtH41Vcgmo8901Dtww1gIgX6HJIcNWQKFfn8Oi6GpQHE4cEam5DJYawcbYQv%2BR%2FIQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNcLxMMXEDFjqqNuwyrcA08Nr8EwCNvxzevJdBsXaWCFjECDjZ%2BVnBjvIfOSB%2BGQPC3cZmp4WREbu8GkQeGJaUu31vyVBySbjS91%2BnjwynDVAy5r0RDtH3sHv%2F82GnHPpIHM6f%2FmZZOYGiwC8m4eB7W%2BTVubhq5d6WXOXSqQTtb%2B26DA4rYrq9cZJVvcnExOJwuYDL4xw8C%2FvwnS3cXO5IBeQIilXeK5bn1GwJLS8MEL9AzqpCnxGrslWaGlMnqF2GzJmn87YefcHErWMcqERIhscBhi6sVd39gPTWwyTfLok%2FZPdQqlsqQOuj79CrsL%2BUt%2FNBY6N2yE8F%2BQTabXWtVGEiayVAnAvHWBdiLz%2BIV8P%2BZEDuKA9YQHxwdhsFJcPa8WkEZf%2FsyAz90nbGN4sR2D1zKXESzT%2FDz7LO5jQziP%2B8vtoZqHa3pOuLVpUjyyC1TzExsE8QIcMSB7oZFAzSPsrbuIDGK19WS3MTYki6%2FXD4S5oLVB0uobm8ti3hA8Ypyzw%2BaWQauIsKaG84Ea181rbpHqGa%2FLzrImZKsr0SwIcqqvgm2lzbT%2BHmnxojPYscIf5FrHjmQUqEYGo1C1anq1ETLcTHZx1ukG5B9ncc0sZjf09EF47uSsfFqi8JZSMXWdDbdbvFx8Y4MMMIOtmtQGOqUBBgFSGQ461qmbxwEzY95T9lO8uNp7xP0o0iI8VOQ6yjc7FyD4X98dg8rcNRgGOllsyVsvWZvxDXorImxwM7GwlxKTE3Xia4DPHNdQHJFDOlPoOshIS55j9q7UQGmeS3tR6Vl4mU%2B3YiQ0hz9YeFQK6bm3Z%2BaXUakAu%2BLw2ITn%2FQ0rxTy6iMLKmhHFThrj1UHhBRlTqq9%2FluMT7Nzhd5qGjXaWF927&X-Amz-Signature=1d25769f8e50c6151e68afb2604f11afd7bcd725aaebf2eb27937a3f36963e57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
