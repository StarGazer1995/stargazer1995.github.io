---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T64JDDN%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T105922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIAbGQdlf8WLdhCfXqrdbteC5rSyjMJtyYZ7MV6ZQjJDkAiEAjIFp9Kzmi9oeZEG0OaoH75v1b3O2%2BUKzhfx9x1SXdSUq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDO9KOlJhRA1k%2FdtGuCrcA%2FtucBNT1E2tC4ZdpTbZYA67L76JoEcubx2Yq7ShVOFamgR5BkpOkmgnzSwbzcRP0AKBJ3gBiwYSogLb082lOTg8e4bjeh7n4tsKguS9mOtjmct%2FL8SWsBUbWMsiEPeGLbf8epGAM3DNOM39e2k3jfB8PC6TZfIzWzXolV05LLDZ8aZHyzXvn6oas419RzIciME0gdgDBon90epN5JIyVoJAa9ixHyBfLaNB7pSgae%2BqwYcgMN9vNL%2B1ZLJV3YsTVta7FyZz61iN6awnvLS4ahtVpZ55bCY55S3rQztTSLDFAnWpsyxcOzroiNVvcriqYF7%2BKopDTnsCl8DYeltex0GyPttOUmjjmSY6tUDg4HCk2l6HGdZoh4LBkAYPWo1eSglL8AAChNntW2igXOncbm6Vj%2FbmXgjGR2h%2FhEIzPNyFrWCpzuYluLWy%2BVBoehq3vZ3tdilOHilEDr0ifEKpviiMce0oVu6wfNFDibtZxGvCWY%2BOqqiIahxj9kJYM2SHpGlUqCppQFDQVMRfkVM0azFrrJoVTt0N1UPCsyAsXX%2BqQ9zdHBWnJShesO0kb1%2BI9bj%2FMJ507Zgsf9O%2F%2BvkOxxsE48MekMxGSVzz4wucfgHtMDC0WeVBOzZHUJ7pMJCCo9YGOqUB9hBGWmIE1Yltkh6ZLsvkmF%2BlACss5PyLaIPUxnNRAehEIIz9TYZiQpje1zFlGneCnZ5eKMC7myiUEcwPZwf2PE%2BEpzpPlsOhtepNmfjrwYbx2cUYXBsLFQiWXBKxZY%2B9bwCmJ73P96WS1FlGdUlm3%2Bsyry5h0nK%2BeMPhcx6QpwyxrZrSyQU8pygw2dQtRPsIgnDwH11GWSJmJ%2FeY0SEiVvr9Sixf&X-Amz-Signature=dc21a56fbc8a30a4fff5ea4db58180744742a51627665f4c76f01577655472fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
