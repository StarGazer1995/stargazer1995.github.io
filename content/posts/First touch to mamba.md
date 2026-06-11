---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSCIYEPK%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T173248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCzYOuQLWgkqb%2F0qplHE%2BoFFqS%2F0u8dq49wWSAc7XXoawIhALXgQSNHklOLlTWDy%2BeVFOWZeNqJyrYbnV14FZGOo41tKv8DCAEQABoMNjM3NDIzMTgzODA1Igyd5ZGEXkxdPD%2FuNcsq3AN1zEwlEyvp30QfV14DpgqvlaBofRSbX5SYAv9Rr8Ioah%2Br%2FoBdg765tVWGv7DAsr%2F1J%2BgMrgtZCF755JDzy6ejqlkTyw242fD6yHsvPyIROMHbdmqackNhlF8GafMZw%2BTzMXpJxDb2dlR0WFfbGKLeTqbRAnyY5Zrjy311jUNgICE2fvYNE1zFE2%2BBlnLv%2Fme19cbiEVEJu2WgSH2XtdPC%2FTYVXgRDzuS%2B6NzMc11jiS2LuX3NHoVROFiJGfe6eqfcmeSjQkt3hc3CZ50ac7HIHNYGnbmBbjo%2FdQGi5ieKXSa69O1ftboO2v9B81xEkfNv6TUwYaIr7DMsAwUwAmQqGI0kqcljFe3NPjcjuL%2B%2FQGqQbdMtLSBIRSKOkLSXX93HTAoEymWbMzQwTzpy%2BsSss37yiw4gR70pIfLuYt9ZvevC41W7YNYi8z52wxevvLnCnvi4%2FfujKzxRVOYCKPbgiozX%2FeKtc%2BcCvUx7T6PwMafag%2FKhIzFcO8wwoSyw%2BXamZaCn5tWYsz2GoqV4CDRON0Lhruc0oyroTGsNDfYLI8kOJ1FM3%2FL7d%2BeNrGKfzADWOTYV2Ekl4sjAUlBfqYWmXXkqv7AA813AUv6d4xcSTVCb%2BjdNs6QT1zM3kTCzwKvRBjqkAQhWApdw8SVFfF1zJczw0bzBrR0IHLx56RCAxs%2F%2BhgTj%2FQPw9A%2BU2rQqawz2cLyktbXNo5A2uGG6E3HHH%2FWPkOzGIXYDGh11HNQEoJYR8pKkU1MNLuv4SoaKzwYL%2F92WQOdd2%2BriBdlhNG5ldYHwK0rJhs4cLr8wLYnqLaqWQVlUs5xAcq3XyLL%2F5GniScEMqBYjpkBysc5AdQL5ck981AR2n3oa&X-Amz-Signature=8bb9bd524335c4b6e5826b919346944568f5842b75f513fbd7a528ab11c3f4b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
