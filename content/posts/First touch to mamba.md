---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VC6GMWF%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T172429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDkxymaOsOSgeGrsS8azswBKIS9%2BqEtEe%2FfwcLldMMQwIgcPh%2F58M8BEcc%2FNQDFZVEn5oAR1%2F%2Bjsx76FWIsKR9KWMqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDvG%2BVBPLsqDiID2LSrcA4fJBQ5owUpKeuLgrdksNXB7bYtSkOzCP2wd3qfai1xMLMNzTE6UbEj%2FB2nxtiKMeuCLTreSztfuLd33ezUIwyWCxoTnXAGBrsHRekoxXwGiSoRADKjmN%2FPomtZB8UVm9thbQxyjT2a2GHuLbdvqWhqH3K%2BLk81Js4VCzOGirT63GwRsCHseYlylhdVlQvEv88rknTyD%2BsZFxeajYe3wHTdKole1J8CRf3qV51xBz0uM6V7f4HBPWk8WJuBr%2BO0cBoxCXNGVXFg%2BZN0Id0V03FV3LSd2eO1ggBjWMW2j7w%2FSvQy9DqlCKU5DKp%2FMtNP%2FmTShJIZmpxNVr71rID5bhlCaHin38aBt4due62l8Ml1by7Ii7X6JimozTiBYPgfKYSzFWMVkPoRp7trWFCJ73G2a7vVedZBkmvOfIDvuoSg3R965EMrv8UHU7bXXLnq5png69lVY0dmwBA5TFYeKrF82%2F8M2sFnYrEUKGA%2FEp0xkxsvo6F%2Bcfgtc3tPJmT%2BV8Wp3fF1whpIgdsBcdnL2jAmaCX98RAthe0zQdcDWX7IhVZRp8iy0TmpIqq8atg1dqo4f1C%2F6XaXNofLuypwv9tVleZiynFvFpXkVOlJQGRAh2ZFbh0SZxIsfdkOKMIjZkNUGOqUB9R6IeXG0QsMmXRU70fL724n2rCdULMdh4togR0FS4Nt2KsdBph2RfvgI3s4228IOhwEF0jvGaWOVv%2F8io6LNf1VV3JEj0M4klhJjTfvfB7lmlajT%2FTnKbbFPUIY3B2brMcVQbUv%2BELzlAthXpqI82fBbZqPeWcueCxF9YRhxj5DeNptrrQtY%2Fn31zks90z1ipmO75sLk7ly%2BMaAia4xkU7XXhlGM&X-Amz-Signature=9c4eeba4263daa6c4001519fcda9c2a906a48785260235d47f94bfc174096a66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
