---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SQPXIWN%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T101552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQDHhgWbezY7S0kHjePaAe0bNv3fS%2BL0a4LBcSXrCfYywQIgC0mz945LEZwugVoZZybRH4E9jr2rtOGH8ODD3e84I2sq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDPJjs5N5DzM3xJ%2FTVircA5ScHRfc5ydj6WVgyuu748byeEr3w3WKZbSzUbjY%2BuAHgS%2FnWyfm5yVHXLYuUDH6Ai7DGgH07tKKL7W1Iq%2B7ceEChISOva9mcstHKEB1NZ%2F0hsg7CD6e0sK14b8x1aPBmUrwSwQ3sAUkkT%2ByNgTp7MRLYgBy0gorir2h8NgL%2BViHQKQjxvyHOirSEh7NRDPDJqh8HbilvsMh2NuzyxfA9oUcIIkS7HZnT2Ir1G4NkgN%2BqMmkd7tEjUIJUqSDu4lpdikfTxK%2F7biTlaftDxPj8OvLkBaFk%2FJSOSaYW%2BfwO7ANgm9wPjbJBKpriwf8oZHmbNennryaEeiELI1nUNiptu8yz4%2FS1beHo1IL9JUZSuJMqEvtDClF4awOQ54s%2BwuGvfutYBOOCVfXabCwnU%2BM9YLhUCmc9qYahPI1EUGfub2RCJNrs3q7tVeDnSaORKzLOdLliijJCL8ltTW18xcQGWYN%2BweGUbOOGWEDfOUtcR6ofhKoCwC%2FJpIwt%2F8%2BJbW3SLlEWnF391C82fcfuf5YOaUU%2BLDScY5xJcYOWoeK%2BohLC4H1V%2FSlgPGrcQRuuPZCmoONjXgj1d9eybZWOB%2FK14uVS%2FbGnIQINrNj1BAPBiMT06EVsZNERnH1p4%2FEMIzw6NUGOqUB6IaMNNUQ4hXABuQmjf8l4Dxg5Bqd%2BWiKRPfRfqKgV3duDYEaNWUbmjzBn1Mt7NRW%2FnOXO2V4m43f6O5HXksbASUQcFSH81LNlcQSf0TNRH3Kqo%2FpI8JjTrGirTCrKjjTDSX%2F5xFoAAJ1KcBDD7rjZV2nZM70AM8gYgVyoz89U84%2Fq3yFcgJ77y689LINQ4quJXg%2Ba%2FU2ahO0aeT0OBJeJ9PKmh2p&X-Amz-Signature=7cf6e3ec6689dc3d27917030f581b07615b1400ebddba6eff00c8f0cf85be6c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
