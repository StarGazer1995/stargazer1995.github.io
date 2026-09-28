---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSC4JSWX%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T185934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIA5j90Un1bw4mi%2B%2FVaXQPf2pqrnr1%2Fe1KCvS6WC4lhqGAiA%2BkJdkcIXeWHTJQwUWR6tasYkqjx%2FPlYkrGDzR9npV%2Fir%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMf%2FFI0Ftohma%2BPeSDKtwDiv0w%2Fkrc6%2Bs%2FOvbkdcwf7Y3FZ6%2Ft8dfTwiAUbXtK%2BqAEGpS2rkaemj5KknO3FeiWjam%2FPcv%2BWxeOAKrNGskvpgnU1qV%2FZPGV7pNuGaBh%2Fun8Y56m1x86yH7vio0ZIhG9RHY7RxOwnTtp9BBHnWh4BEZeJcY55zutb4gzz5a9nwieIQCIM90EcfUeZ%2BpgHn2xieckGtYleHZqf2x8dsxUbCl%2F9cL7Cq9zAcNoVY1IL6THjGfgXm6un1DBHQouQdhoc10kF7tyOvSWuTIfMdA5T%2FJZVWtS%2FDDmTv8Ejbu1kDQxaE9aY9BDlhraurkTB6UTVRQ4YJi2cC4ab6ckyyaBzO0SmGG4eMQK87phaSkr8v7AtWxlCHKmzZH%2BtN%2B7uddtNvAx9fd1bHsJ5pvW6pewA3ZLgYVagF4%2BloQg46Fg4cSy3YBk9IpXovG11RPPaJZv%2FRupiEuoOtMZjy%2BySxiwuyNAxL3fm44%2FkmwJw5wcWJceVKc3n1CO%2BeHcHQBukvrsWiXOFRy5DAZWg7jPdVBw%2BOZ60lqN75E%2FgBvR3Vgnc%2BK1NQ7w7ZYre%2FrNYu2Md638fXqmbIWggb2LUiW1LzS3bSQYRtgEvOdkUWmMaqsvaBHP2B%2FvG%2B43tPs%2FW8Uw89jq1QY6pgHA2OaennBsZxGdR9HG7qNmbc6dVD2%2FhoyTebUcahuLsXMGkl%2FBzIAKPXtmGYghGS3PtymUy53JoIHKHlQuN9KsCqMbdaNrKSan%2FgoBHrsfYeXN%2BsoZ1HBcECKKeGMUEfrZT0vPmWf0vZ1WBk9tET28pflMFh8dqos49RdRXyDv68JccfRfIPU0hofA12%2FIDRDmHQ2P%2F%2FMwpWw%2FDMQlk4ay2rvde%2FQo&X-Amz-Signature=56c7c30aa15d9888cf517ac278f36b1a993c86de5e094817d2fe1ee760277469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
