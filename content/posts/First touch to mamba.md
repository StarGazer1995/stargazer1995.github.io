---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RDII3Z2%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T060828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBeMJSkkx23anapl2vtIa6zkxBc21n9cXhW2E9r1k08ZAiAPxNUwmHaBnLaC%2FOmPpG6I1p6QppfmybRuUIp8ORzwfyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMLuomHGnqdy%2FFB9kBKtwDbMigkwMeyLXeIPePjar7K4fjaZOAz1wCGeWk4VgtlhIvxFrpU51l8ttTgpB%2B25IC74p%2B08bjaor65ReDCP87HpNvnDZltMh6YTs6SNYwjMVvBrRa7yoShMo%2FlU6MxMOJlkIY7sbs4deeIAC0YC6C4BE9BoQHU5G20LokFS2DTE3wvR0DYexWVZI33N5XpCRr%2ByieAyOa%2FWcQ92ZLViBqtHTC6SvduaP%2BrsBnyEJmqLz%2BtfZnNCgkKg6B9mF%2FyMUuV0RkGVVpo%2Bk60i7CrNTu2K6MXM41wxBFHpZ%2FpbhwgNQ%2F7P3q5C0WiZMYAMx70lpzWbCEfRM1QvyzVZsfgf6QkNbSUT4gczR%2BF8CQ7k5zKlIr9myS7%2BNgmMfivEEt7ivQHiQWSNKJXkodrduJTQhfzxdczBXDLfB8mixUskYLOsO3iErZOqx3eLJHHTOXiIbQv8wuMvtnmB5PCo9I%2FlkNmMj52byl8xe191EcJ0mroBiKEhZAy%2FGR9UfwNYFfoWsNq3iBSCBRbTUUSqX%2Be66NeHWY34xw2Ew3CR4hOCm4lBy%2Bpfj4TYoyP9ZD8vt%2Bl4gYc4k2rTppMdbhEC%2F2XEEsh49dFrPo3CiJjFiPn3rWey6Iy4fX9CojB1VC1QIwzqTt0QY6pgFD48zH8Ayba0hGso48AaOVhRc6K%2BKOc8IBBYM%2Bmb1aHlNSpz5LA0IdNaRFnPDR7zLa3GEkVkpyrS2WOE9ypCoLEzwZLhO6vteoRXF7MPyuR7pO8rDBSipRpWCL5MBjqnwUcDb1Tv2o8DG37h%2BEq42evahAb2%2B2RF0GjfH2b%2Br5MNDqwE8f1YfH7gudnPxmvwQQM%2FJCVB7Oidgs%2Fao3iyIfxu26tDOW&X-Amz-Signature=ddfdb6aa588498feb7d2c444d87dcd8403b2e9b5d243445264ef0b1692c91aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
