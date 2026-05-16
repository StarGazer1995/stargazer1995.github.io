---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLYAAKX4%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICB8cMYE%2BAPGCfrtwWeLzM884mJtmYXX7yJUm1l5wBPuAiBzQADf9L%2FUQVAIqvZzX7a0%2FVzjAZudh%2FAt6B3L3NrW0CqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMP%2BImOVC%2F7vUYIKJXKtwDtw4YucP4%2FYdGT927CAezQwy3FFS74nB%2BruaicXt%2FaKzkFu3yzAcFf0NTiInj8AUiNEWNeuiB3mQfVV%2F8DQ1Q1AN20iEoUdWRJOHHXxj2dlK7aFxlLsZ2SdkXlbB1Ug7JrB2Al31CUmQFg17zqYxXBkXOSdv8GSIouerYPv6cQJ%2FKy8bwBG4GQW%2BOO7Q0hh4x1oTWxHrE2LinUXdnVZfaV8CMwz%2FbiUDXZB%2BY1IOSOjhAVuAOXEp981JnemQt4lFoKf6VeJcCByBOvNLe22QMvU%2FcWD42905e4jilns4lOeDaiUGT50QvwHk8cYWweHuuS6X5mJAmeQcwJKtPIYujV6UBaey0NeyfnkUdXqK03ekuJ2ZnDKoG0aHCEGKzqoCGrPqQUjUeLHEtkljkuXyjDNZfwWuQ7lpZZC7h%2F%2F9aBQFjevBR4Vm36a%2BSk8N0yXUwYyntQ8ar9Uxf1Esh1qn7L9iitSdzL1vlvHHPyHKMEmswy0vJsrJOHPikYDed1Nr%2BCYeq1MknuTP1BhWfGY9u6NgssVkjRQqPqZxichE8OmmlcCJiaKRmv23PHUxXrFzR9fEuTUTyWAh7rg6DmM1BbjmGISlJun6CIeDlnhA5w4n4SPlqCCkvPakfxX0wqYaf0AY6pgH%2B4dh723xgIfXq9I7J%2Bg%2F8hbXI2BYoQsx3rTSyUrHqt7YiSxGEE7SPeGBv90V%2Fa3E39yEQIx18pC%2FfgoBq8PkYG6Y3OsKLyV3wqYZ1l0gK%2FkB1lxh5y1u3KXfb0X5xOM2nSVaHxMlLS3iCKQSpMQ5aCBTvoREMb0klcS2bLm9%2BFWG%2FQc6RXk%2Bvm9Jnb%2FBY5OOPHSYjPnj9tlUWs4XIyLWJPFAjpRmF&X-Amz-Signature=e4d756fa3b0a44d04503c8d193d11b8d5346bd6ee4f503dcffc6f3fbbb9db477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
