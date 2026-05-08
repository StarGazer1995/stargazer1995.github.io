---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYXBLIPW%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T130608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIG29GGF4qFcy2A%2BW7qC5TXYXly3V1%2Fn738lM9zRhsv79AiBK7CULE5lF%2F64sUD1Nig%2Fzbb1iqn08XDsRCB3R%2BZzf%2FSqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1b48eXsT%2FfCdzMYcKtwDjIzKdngwP%2BSIlYF%2Fxomcjk7y7hLkWtj2i6%2FMg8fmgBVbnsk6ZBQvpk1SsFdQi7zunrP2%2FiqU3aAkDYCaBUApBWEA6Qy0fYxs7f1vqOhVzssuEePaMDN7vKOU8mZnEAB0vNAw38uM%2FuBK6GPU5wptb8Y6bwxJZaKbXoRMIDq24dvQ%2Fal%2BDLJsJHKckqeB1Q%2BQtqv3ViDoF30dKDGf1A5kr6ksRuxtvw8xrppZHUIq1KqH0DNmvETqT6wbkgLjHIlSJu8NKmqR8KMLbhA5O7feK2z5EZK1tcUk8eFQd8%2FB5O6wDomqK1%2BLdJUSQkjUeez9PmO74cCsaLn2qK9sB%2FbKMmoIG%2Fyr3mscujAvb9s5z4l0aBI3mpMKwvKKbtdJrdidORxoRxqUFK6zLyfiB9qfzKEwxGmmonK3EZwL%2F7Rh7CSBi1oX2EzrxfD834Ls5eVzpP8HHVFGBXN5e8AWmjdP39JIffh88oV1qdn8ZixPplsDt7I1U9d8hyVnldCknnpmq6hLA8eqTsbDMEZJLjUZj6SmhP80b6ERiAE4ACD%2FGNFUNOrbiaN5nlHegKDG4SVrt4rDQ%2FLbvNb6M5T3cALF6jIyrlyGvtdMe82dAoACNAVZySQS4pTED1QLi6Iwtb33zwY6pgG8HpMI2HKFC2kk%2FylAIzE5Z2iB1CXtLq7pduOQ0vLFK6uFncy7B%2FmwONBcjVpdNSVY98HdewIvFRqg7oe554mWr%2Fjk4oUPE7FyRhtgTuiEPSj%2BuGOQ9hz5Ej6DOb9cbgS4L60x6fNmFcaINDvizNH8%2FBWC14aCr7dfV9IgDNRQ0kwwNzuumIOGO9XsRMmrL7vWYuWg7%2FCihvUYy2j6jxA6qY6u04CX&X-Amz-Signature=9c95b654d3b87f7b59880ccd4e0e05fcc32ba189a1fb9a0b246dce78bbf3dfd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
