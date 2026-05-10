---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2MBFOUP%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T105358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIB%2Fnw7vGvUl5hjC4p08FwwlzD4AwbYifMTdNTJaOUW6PAiEAs6vNkDegz3bsjITk1lpS9MEbSDp2bAKvAPezEIxLzKMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBrHH0TAS5gAfcP6QircA4f0eucm%2FdqYV2KoRDlARuyk6bHG2tztMegpWbDrAkPMvsyUa4C0EpcJ6GUb4WSMrBkhf9D0qpvboFTPOGmaEjuYuISU3Zc9wNG%2FMCnAqRw%2FGkey83fYnxV4EEE4uWGotKjBgIUFeFGZ0ipuzD39y9M9k9BMFfhUkoQPL2ImJ0skbi3sG%2Fye%2Ban4JanqG7Cs8k4s3Pzx%2BUBZk2SODTLKAXJpe3%2FVuqY2JBo6QuG8dmgRbXHIuLASsF4qcXtIv9c7IJkXjzauHUxNfuyGKJSvfXQr69ncw8qydsEOvYmcRoM5YDbCXSXH5m7yGkI9DJs83DVrhgSCuCcPrBfWZ03ei4bayFQv0PkMmg4JCX4GT%2F1eTzReWZE5AbDNxO5XUNufOWJ9aaI%2FNog%2B4oh98H05wCXOstDiUat79EMhV5qrjWkxYTX8Hh9%2FkxqOIM2lTWjXCC3%2FUMI3bm9qIE3p6rIi37wCDv32l3WR%2Bf2H93NbiWQEl6DJwf%2BUgz4O2FXUu5um9TDdgNEQv%2F1AKL%2FHYEgDFQ0yfYKfkdT6wI8Yo24gpqoZJ17ZDzecVjFhoYb%2Ba9JmiUF8JEXaWqneLPz3nmVwMF3XVUsJMH%2BX%2BcYI16hZoMpZkwUten8%2FJc5CuUJNMPGzgdAGOqUBn4eCfkCGYRDRlJdtzvF0nams8OikssK9%2BdP5TumYSbJgFrkd0CjmesD61x6hVkxYCcEf7DdJqGSFNfg48tE6lSKJY1Lsgonfmr7ta5lRfijK7x1ilIWqa789wv6fn1ckFzBblM1a3ZPBBmNJd26PVJP7WlW%2BqQBZclCNyOhMMORJtvKNtMrbbkrZZtj9McZgIilkFvml6SSaM4ix4wB6AMsFcRcc&X-Amz-Signature=76c4153a26a0f7eab8343616530ccd6a36e0017883f2179804b8c50025ed12af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
