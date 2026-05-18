---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST3WIF3Y%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T145202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFF1FSyhE1B6vGJFCj3bcd%2BKELafE%2B34N8Vpf7j2WYOiAiBq03J%2BToFEHpaDGnf0PI9SR6Tncvx63EGeTTHp5t5WJCqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML0kC3QljpMy%2Bf8NEKtwD49e7%2B0VClDZ3rTmso2orGgtQRopI13GYbOgckaow5AklBsAv7Perhpw83fi8R6dImqOFCoMZYV8sd56J7WSKhrqpdWcV47uRjoyERPi4Y0saXrsCj1p0CxpGQuwaPARljalIe7ieRIz0VfQqGQUnqBIjPY1xJmNlCRVdkJexJV5gMsCSla7jxSJrp7l7cmqJRgmZdJizsqiLm%2BjaN7zkVSRvlMl37zBuOq6NIqxrqxGF59GTQ4H9vyZ1z%2F6qcUZJKOpNf60aUbvjj4dDXqCo0Qe6wlCaeSy83wMpU2SQnz6OdP4B8Yvw5NPQJleqzlBpipZ4n8G%2BUytk4md9DnFnTTJGMi1Jbx2HsrMXKiAmLrZQPMqLtEtxj0ixcYOkxtOfu1%2FKSSwTk6rpGKHxS6jETLHs8XCSzmBj0gkk4syy1pOj0hXj%2FaE1b7YuZLe5ABXK%2FBYxJ%2B062%2BG2w76G%2FKeE41QphAF%2FBCBW7nWc8DXFsvj1wwsmhfcUR0gtAj7fjSjWCuBKifxkL6KeJaFLUS1Ps5MiG5Q7igbHBT11tL6JMjff0f5rV1aNl%2BJK5Isoq4QfBXTnB55t%2F%2BAx0q9XFodHarQg11Ss2XvZq%2FPOC6OHCJO6b2VyTOGtFWMt%2Bskwl82s0AY6pgGQKq6jNwdBnv9OsXUU3sQePP5em64Quzp0sM33Yr0k5xVrjpC0s9lMdTCLZgGI6irpiF42QsjHaxwKhcN6Y7feRk9Kp3%2FYmcB8Whmc1Jg5dERZ5LS8coO6Td7BRC2NpsxgCUlh2pUXsItp2XTjv9aVV3eu2P%2BVPFRwDKXC%2FKyJf1%2BwtZ6JFWFFsIetF2edJcD3k%2FinV8gOVPS4GgjSdjLWZ3zNqusy&X-Amz-Signature=2c66f167bbf8778348055e24c55d7722aee7eeee6299242fb9990e3cfaa29d65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
