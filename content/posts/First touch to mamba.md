---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OTBB3F%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T193126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7bWIKadR7GJ5pShqK2SPdv4CS4oBcMHS4rqiPl2d1bAiBjwrHMaES6d0PkpHwv7qN6vvRWCm0aQWDLiygYhbPFhiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FnAN8E5vOAqM7yj1KtwDMTLcAXaT2JL7Z1vbbQ29OM3jbxTgmAxVG1oKFx9Hf3rXIKcI%2Bl9ynw5X3DisgjcPxoFrqSbF7ESKISBatZExP9tcFRDQkOLWpJBaNBVnOUByKmlsj6e9LdyXJUB%2FSwbbuM%2BALYNnlokujrW6qsyaBYkw%2FOhnm9r%2B6ByLUW70fzBAtzRJ%2BjqTZyK9UYPLH2l2aaJHRLH2HmLOJ%2BiaufaWuEQkZVikpDs%2Bt4Lf8IKzUtOzErGqO9aGSSaG9DTv3XFNoQYrU3Wsy378sHDYy0aDF%2BBCSO7os4WT8Am80DCWWZYO5OXwc2JsBmsPVTS3CyMZa5HRW0vQXLbRGnSpRnhmdWwgg%2B7wN9y0dJHnXywFVTqgHmU3nNwahyWladUg0fg6%2BHowKJ03ngbNDKgeZazsRG9%2FYXzLbBkIh5J20dRqxnsIsAf2zO%2Bx9%2Fham1cln5cplgH%2Fr9MeA12EJSQSkKUHOPWn7HdDEldtLf7Xc3bIoXC71rJqgj3V0MwEniDtcow1Nbj%2BGtQz1UuW65CY90fia2Zcg7xt6L9kd3%2F0wIKSpLzcjQdqXuNytaknn5gX643%2FiyLw5MXNPQ7%2FjnWW3sVA8GtW4GoUqozE4k21pHDOa8HJfTGmXzmFvAfxW8QwjeiK0gY6pgEp3isZmgwMlmqo5EBouVyrO6ktNnP37LXEMTN66tjsnvI%2FiMxMVoBYFAS326VrYPJCD%2FU08wIKHF6FAOy3lEnX8tasfUMsSkIF9HcJ%2BGFp5dEMP9GjHCORhJOIvpVdxW0BaGoXrvCFfb9aUkd3YpIpwreXQNYCLyTDNHfPnIueQC7cNLTc0CXqUF43r3esFlzgEn4lRWgzZNua1874Z5g7DDHQTU8v&X-Amz-Signature=77ebd6953ea2cd8b61ffa449ec7c06ea95aa0e42ce60c15663d815f59e79ad47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
