---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNSP6ZJV%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T213036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICFJf95R97eGnXevAi7NbUxs%2By8RHJKqzxYpTDudiI%2FmAiEA6vESMjX7r5cBOhvEyJSovLaCx9tB6%2F30QfR4osNlVeYqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8PmiZlfsu9Y%2BYGKyrcA1ZWbAiANNPGWmSFASGBTq2XjtdqE6J978QGANgjusArfo4As85%2Fa7uEgkRSenChWfntA1l1Tmjn4xSTuRvA3oKfIcu0BLJukiViyC6%2Bm50t%2FMS3Br1FFkpwTJTdgenerGFWa7eVn5kyX6XSt0lGooOmL9wbY78AYY98Ike3m90j9BolZ3MQ4UwMyde5XkW2SSB7gPUN3F4kmxKSu6Z4npS4G4tLFVx4FPHjDUdLPxR328OBuMxr5o4DHTK9Z%2Bb%2B8F3Uu2IhSL2ixwZIcaL%2F0ly%2B3HOKGTqVQtXz2Nd8pLXq9TvpTtSNp2Y6YJDMLeRbO%2BW3flE97w0o16fY3fHF5vS0rW3EQ8lvcXPdus8%2F1Amyu7mR3UyQN8cUvYN1F0tiPJOzPK5Edn87IYr0mJqpJvlbsA8nQD5xSQuTGjknVXftyHQE0r5KbdKXItD1GTQh4k6ZpJYcdWiGTc%2FkFZCdVyu88KCNTMOarjrlThtrFVlQP2PbRfqYyCiBgztpPpBRmM8egTHgOnTajoRgE5aaV7fYgrmNpwxmxj5qW0YXy%2Fh7TVtxCHxoszF%2B9dUBryn6lZsypVpa8FNnN%2BC0NiSHWi9gAoEwp7QX6DMpz85VAWk3rfGclJNjtBlgg2%2F4MLrtodEGOqUBBAwsaSjC2Il5x1vZYR7ZfZaW9J8UaQefn9YW7b7wzzNcDTp5x3huKIsFrzXI40sy2fW%2BN2n%2BXD%2BAzqUnAJqvb4pitzqWJ4J%2BYEHHuy%2Fg38XM%2FtjuPFw10v7nDYA5zygBYW%2FiIcYhYLAs%2BgOSEgjsO%2Fs4JOCCyJ9Wq9BDPBkW%2B1lOl9lyWQjpeCXUdGflBFH6Wej1abJh6qNp%2BGL%2FnUcQ%2F%2F503QQh&X-Amz-Signature=72530d24a14da49c1777e8fa205cc4c941c32e89a9ccd5b2521fe7aa878d3c92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
