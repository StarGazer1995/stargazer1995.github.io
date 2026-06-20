---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ7SANQF%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T132335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIFOuPAx0uMMOmgztGXEnBQnsTT2IZQmZj1UeHLJV5KNEAiAM5DUNQ4ZM4bam0vROKpowAYR8AwBhCjkZnBGD04m%2BByqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDmgfzF9Ug5suj4%2FrKtwDGydP46%2BXOUw6%2BUiS7pvwtEcviBgoo9reF3tllVFSwgaS16YZmPCyz5ozoqe1azXXc%2F8N8C1hWcBqMlzlM8jAhM6xUoiFWLLAlhDE5KTR0qrBLg9E%2FN4qlyeZaqjgJZ5WSvgibEOjolbUxrf0o5KWWLWA416%2BPk4vNg0%2BRaxImkT6jW9cQ4clR1If89%2BqqoUlmMxcUuDmY%2BRsuwFtRM0eRsk8Q1zLHHgY5aCF%2BkWRjfiJO3IzVBTI6ebSPtToWyvv8i0aBBovqX8uABkezMJmO8x2YB0dzuzsD2LNdGQZzFaldTBZX3JtJqIcX6GW8iYDJh0RKEYbomFw9TCTDJRs1VS%2F5VPOlZuLbAXeitOH88D2eN6Awl%2FA6iUqvPzxYs0oE0tZLlYtmdxQolw9VST0Ki16USlw12%2BjyTdlp2wMKD%2BZUpVj2DVKo7QrMX6SRumaNO7HWaYSDoEOhuFHA31KmPz4F20CI7a6rvlRj6w3voS9VDNPVvfruLmTLjDPywgrP1xTLSNtNaXzpm3ziuY3yQ%2BW4ZAjC62C1CzNRtRJTbgy39uE4vXONOhywcr21AEuZjJECuwvtBBkZ8kE9OK2FJN1jkMN%2Fs9VtjEefM4H26xxwuWRYn5vl4AAPS0wkOrZ0QY6pgEeCkvJLqfFh5FHO90VF0yYMC2M1zk954n%2BzglQSi4P%2BQ2TymKdkNwUXs0vYLTyWJe6LkVKSVGqdQr%2FaXTjDJkm3yS28x2tr7BHdiwFOHQtjvONcJaP7gi39HNazFd2odgpCJUiPqp1wi5I8yyLQwJKSyHmEEfO1a3gcceI2YmNK%2BQtaWrO62ak%2BPOUjflqT7Rq1sfGaoWBo5iI7JMmQ8Bkm0WoUAQS&X-Amz-Signature=f27efbfc1410b57dab286e67fd6a50edcdba4eb2d907b29810e8ab9e22d70230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
