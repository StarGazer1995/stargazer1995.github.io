---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24E7WMI%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T110414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDqHDdT%2ByiM0htV2nU%2Flgg45Ef5cd9w6tZCfKGkPfqcIAIhAMJbdSW6DqnTRi7VK9oCqhjn2Jhrxo%2Fro4gX21t1MP9WKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYzrs6d9PmO4LLNAMq3APNBSXNOAYEvZ1273U4b%2BL64eNdU3xh9JQOf8mul2YGj7vSvzelXWL4VjtpFfOqp6R8PW1meDQjKb3vo33zrfYFmioX7jWyJXoNp7CCYzyiUYN1RdXRyT6r0KB5iRO5J%2FF7lJxn15dPgYMZgP%2FMon3F11p3HZnKMbujmxpVocgAYEobFv3OgJVXEkkvVUS2M1HW6glLC4Mo46n6znDv7EpTXJqogf9CjZtWytpAUixdidhqAYCoaJ5s8kGpoy9zKBYUbSRwL343VEWVA90CoQTZEIqWhsltMvlNeF3xz0y6UHlVCDuORFse4DtZjGNTa%2Fihx7QUh2V12v622%2Fcpeh5A90Av3jIjPOwWEQrTgWvgKHqayeeVHtLddb5w6P73iQlREzSNFVW1iGOXsvnJLAjAqtxs%2FUvzNP3J3ru7BAisFDDMVft4mcMUDhgc6W2F95tbSwipED9CKLBjo%2FVWutA46LuFpkcX3aI2c40JQny88y4E0pIY5lX0alHLnPxFOa2S32qWtvvWiCJKggAK1%2Fajr%2BR1RXgoofkZQn%2BQZwSH3LMB116UmjdEQI3B7WYiYgvBlDFNY4U1bcD1bM9Vi57Xg7fTHnyLveZeIPjnrtpgHNwcZU4JXoBieJRRXDDoh83SBjqkAYHf2B7HkIm5oavaufOKkOGccTS2Lk9G52UKB1QU0jqvY6%2BC%2FWDpnWaX9rTlo1ZNsuzQ0Erir%2FNkZeZIiwOEW7gXjlMOnNS46X5bWsnQlxUR3cHIsWICpz7o%2BcN1ouc6byzb4c1oqf8nlQZizpwaIXef36BWGb590mV6hpnz7wx%2FLqufdDNIkWdm9ti8HG8akAWSKA1PfsoC5N3FYgFizuud0QJH&X-Amz-Signature=7e6db45dae9f1eec97371780efe462f4d4bdd7da92c015065f75f6955068cb61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
