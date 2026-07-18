---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X2232BO%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T164256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4X3%2Fux0xZlo%2FHpSIbevsYeaJXnlGcGR3zJ140ct1DHAiByX4Tgzxe0%2Famb%2Bxwvv5TJkl4fHC%2BRAiqBXbWXYsGUICr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMhd%2FHKq4ko5z83wysKtwDyBo%2BVA0xrxOZnkd%2F3AjJKbAQiT8Cm7B%2BH0QqnpBcMGGrCY4fsysuObbUA2zMyUnmy42fnRb1plBu1UjGv80PSZQ129U5HKTBZ%2BPjZbXlgQjknisOE7Pn%2FMIs38y8C7SAttUJ%2F1buewDeoEwfrkGRHiV%2BpsOHYTJbE25mY0mZsQV0GG%2F4yctQHCXHzNVbCKASFksyqt%2B%2BkWagah1HUMWKOKTWx4sJ%2FsZFd1G4BIVFaKGborfX2NzSQXpj4G%2BzlP7CdYORCnIhbI30UCb8%2FYcJtGVD%2F5%2Bs6Qn7d3fuk2ULKbR9Rgv2ZjiMgh8Wh%2BhIUFSxS8RQvKzuumAAjRNR7jbF3v3Dqu8h2%2Fiy3vn46c69TzHKgRYW0upUOea6uphkuE1%2FiZWTUwquWUnJUeZs74JnnsmlO5KZxMwQYAJVUfK4Li2h7AE7PjO2iFhJH7jAQOVAo7ckm7jpSyS6fI56to4yPJo2xNWvPSgiZ%2BXuGEFWi5eCBIkwNwqJ3zuNnvwsE0%2BYU7YjTmbLvfkgXzsrPuPQH09OCpzrUKkgQbfz1brG9GJlTwkq0zZVnfnVc0feoqIYjpG3YacdsitvxRQ%2B5WBXagSLUFBvJGw5emv%2BiXDLW7F9zAR9OcAmslYOSbsw26zu0gY6pgFp0pNlx82%2BGLNw9NdWGXSx2jlvZ9XQ65CnhH2dHEnJyJtZkNC8EjiqgKRUzAD%2FuFPZM5WpEmrpgC2sMm8FgxDlhsyBzQ7OXqfa1S5KhIyIBSr8QKbOflkvKlRyxVdvClhQZfZJVuWIHjhDxf%2BsloUdqhKJcDhoekPU5hFMbsUFujYl2Ebo8NJuZ2sOpNXVffa3K0OxjyZ1jEDi08SFUE4RCd5IqLbJ&X-Amz-Signature=745df41c7eb34e7cb20f86c74b78c5000901708ea840ff912418ee1445316da7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
