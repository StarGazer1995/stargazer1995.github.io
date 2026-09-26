---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3AZR4AO%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T201812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIBwGEK3ztdFqycaAH%2Bz7zmSJVFXQFVhK3RdWlFBSn8npAiA9lfNyWCoIb5V%2BmHp%2Fecr6wkUl%2BSoZQXMU229oRMUMHSr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMybD7NwdeJSqofolaKtwDcAZW9KRrbD40MpiRuwylaeJkh3htqJmohvvVlqQTxRNarE3phC6KddePdhi7DBmXvRY5QuJN3JwmNMw1cu8%2Bflz%2FgwzcCK11s1hjWdKIX3KuKFj0hB7qF9TFYVJOr1KLS3xnEPMpAI1Ep8FNNiRw7wDlOcSH43pCUUiEd5os2NROiYOKTK983JeWdbcQTwFe4RE2ivatEkRISogwqbOv9tneDqp6%2FoPDiXqML1130y%2F3eE%2B3v4Oj00mHjmC6agkAPedA2qBX2GOAWZfdRqPET%2BNu3VWh47YvI8jDCvjSNJ4NXxAN8kK1BLkGSLXswEb28v4AnE0%2FwICWFrbuF9iyEEgQ9FCJywlmL9hw4%2B7JPpq%2FRlehCXMHpZ3VHOfWA3wbUCY1GInFd7GrJVu%2F19brCZlK03YPGSVfAeg75vw7SuFjyp4QXuzgCqMoChgrFhdHNm66%2BRvr%2FtS4s50t63TpcCljLsBaz3%2FT%2FstnQaE8eOMputvg9N6QGU5VKIK1EgQPEBhTZXDL13E2pvzWpGLxgxayy3joWisqtiIcjUXrvyD7W%2FkN4zDs7qgo9be4MT2fY7wyZ%2F0ZTbaHpMCRLB3t111EIWxjricR9aUATSz1j7kDTolJg0cvCHQGuwww%2BK7g1QY6pgEZFRS5AeA97YBEYQ2oTZaag3wDTr66H46GxIS9j9xy1357NAnasVYiu4EmwZH2LKX9JeJIomj57kAqUfVKremtkUluY6hEA8VJY59Sh7nLH8LY4TlUnAuxVaTswxjeAQf4ckX0A%2FNfNUXat4zKVJngFNcV1xHjCHThoaEKHbRzJJOVCCY1pvm4OkNbb22Qc1k6GIT0e%2B72ar2frXEN1c23qNzg%2BLKw&X-Amz-Signature=79e196d948155199b9607ed2bc370757a907bcbc556e87e920eb7e9d06bd4e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
