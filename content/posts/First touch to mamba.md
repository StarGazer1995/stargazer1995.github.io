---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSBEDF2L%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T215314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDj%2FaPBR5YXvIOWZbJ50fpBk044N0qmRc7eVK2Mt4Dg5AiAE%2BAHJOnWVQBPD%2FWBRmHdc580BVVSQLpflj6qER6eqzSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMY353%2BmJyA6oPWbujKtwD%2FgXZtX7Dk07QDNQYBNrhHm09mA9Xj32TLe9p8YEVLu1tlGD9oVA4nYCheKm7e2uoCGNSZyFN2NWrW%2BXS0KGfGfn5Ckm41Uf8OuiKloOfs9qTiTVLW6Mb5NZgt%2BogrUrihjM%2BbJJ6S%2FhnOm8qYSD98YUbt0iihHboLQ%2By3gD3b29HrsDiN1YuR06xBuXchCrXmpCS2LheZ63o2%2BxcbTq3E3OOhcriZ6ktmK30Z6zOczqqUt79I7VR83h5ftHF88vL4wTXxp5Hz9%2FKmsmaqMgJnPAoNj%2FG76KT9WeLQtEiYU6N2Y12mgdEgxHKaUye3sMXmIFbRv%2Bin736V8M2yyfg1eq9N2ZP7ssUbojBU4LwYZZUk9egcvFwZpq3%2BgH0RG0bHRYMvZLa%2Belp%2FWKQkxCsvHOWDmgj9oenBU038u7fwcVZh6gBPiWQu8xd1Vgtz4kgJZDrJ%2BDZovMAXtngB0FzuhqZdKNNptWwLxRN9FGeB2OqGrFqTKqMgeMb%2B7oIUTE1TqCJlLiQB8jiNw%2B%2Bb4mXP6T8ULV7U9VWtOXFmKbiUiL4f2R5lObac7E3f97DWjR10mSOT%2FbvtTnLZ%2FaRJkhSWHPjE6iv4WbxO9y3Az8KfFKqnsKukUbNoYgcEH4wkau71QY6pgHH8EiQuMgDERxXvJX0qrBuHAvE0v6o2HsEmbIJmSuCo94HyP%2Bx4aW3gfSr%2FoskUN9IXgdMS6fK4Ek0lZO%2FADXIpg9XfAp8wgPyE6MYXVuyxFew7P83ex8Qz0lokp2wppORQUkihTYXjNyImxYLRSCQGeY5O1%2FCL7W7Lnc3gMxFNefkoyO4bAzJdyNeoxNSURjJAZ%2F93gZHCA2GufW5W7LrDNgElsAg&X-Amz-Signature=d364e06965b539cc53dc5cc7b10bd416ca5b129395795c9f472f1549ae952f9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
