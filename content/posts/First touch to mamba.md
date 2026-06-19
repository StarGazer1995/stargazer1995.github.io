---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DPBTD5K%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T162812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpeUwrdUsLkGmXiqF1liNKq756KeghVEziEKsuMxwvgwIhAMDb7Gf4E2joze16sQhnWyMVTdG1BgN%2BERRQruhww6UcKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs%2B3oyrX8enkRn8wQq3AM3ATyGeAI7%2BxBVfCQs8PIS%2Fs445NVThK7JCfTUy3DsWejvXfunUTQrRZNcmGPB7sbEbDCVHwRag3qy38SWMX%2BjbJ2w0VMapRYb4nzbTMKyCpzUKEBtCfvJmLOhrGzjGC%2BugQq0Tk%2FrkYtznH1gMi24nIQzi5O1QVf3Szs13bG8DGbtZ%2F2UNCpycgkvVeC9SRqpxbrcLQSaT7Itib7epCJpTZd9Jt8BcAu7SzGYpnqcQGtyK1E4gSezH0KROCPmy1werckPMqBXo5KLrGtNXjyHG5RugsmmKuPzkh0lFc%2F8vCbfnN2YWXpjRmUMY0n%2FVHnGay8PIpKGpptPn%2FoLt%2FYSX3CVrf752YIO9u3uSrATyHQ9WA7kqy0vzuOSr73VVvokBoWAkNv1xtvjXjMTGHRBjrzxvLJN5OK18TR7jOKHfvfCPED%2BvU8fVV4b%2Fbb5fgGtTfhrqDoDL26bMxuP5zWHLUdSPl44RQxmxziabVskK3hZa0Pk5RCjvGelNDXUX9FxEMwEZoXiz1T2s4gdHdlsU%2Fg28fnH5vcrU%2BVkuoKr7H81wxYjeLShhs7YISFiKQQg5eteYccmXzRDP5oiKsdQqUaVWEV8ukUb9%2Blht08lgcgWINCbZhDd12vD6DCdy9XRBjqkAbpcxSCqezS6HZozGK15GAxHCHXkHakRnQWcJN3MO00orCDI%2BP3eWZFL5ULCvAuR1mEsSldIK2r4S1NFuJvH7LEU7kyk7zKFajwlGolyVfStsCJAfhK5YrQdP6Qo6ymBa%2BtWdVuzAAql8yCV2BMKy%2BAfUyrult9XRNmpeQm3oOymlZ33V%2Fzm1zUbYNQ9DePfkEF93%2BPhAjI0iibT92Cur41%2BhwN5&X-Amz-Signature=4cd8bac87d4b461a695376156fe436bef63667ad35a399002a7d602b296933dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
