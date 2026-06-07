---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIO4PU2G%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T021329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5nWO1CWI52FgQ5%2FVSIk3rB%2BGrlbre%2FqLItLj9QeZFzgIhAMq%2F4AGuddiJQpNfr34tlSb%2FbTRgqqqf4AbJyJxtsGaDKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUYdH8qLUlt8kYbqMq3ANWnC3DgvM5l1jPV5yyEI4pHMOQK2V%2F19UujGUIJBhxNsglyuZGXlUnKk59E%2BTHaNeSI7UlNnAkWV9jO1q6v92dIwLYel1SBFg1DTgyjHtHw9CDtfXm57ZRCjinckKr%2FFADvih2z4ThXzPXgi0kR1rLbsaGnKdcY98TUPP56XqOoCoIfbZdQSPjZRiYyuwmxtRmanLflYeKQdL05gfrQnlig58iKuLMZogdziHi9WsAD0A0oLUZoyv%2BH%2BzMmC250oeCnMq4a2ndoRYjEa05yNzEksnZhAYQYenE81EreRdm%2FFGOEv2u5xBOJM4oe3o0P%2BmnyLi17UJrFN%2F22UGozfGUvD2SSMf6BmsDaYhcsEfRtmR2chxce5G%2B2YAt%2BngUt8Lzukck56sh7izx0cwlMciIob07sttemQZbfD%2FSHqRB3OQTqU8qPQHtjlMOef6Les7x5DvLHeIBU37IniTBCDcV8Lb5mlgnZAr8z6jgRAVoadw7yYO4haFOG6QsO2HZujSWqZUXETsMT9y7VVEpUd910tZnzepYeUGHqSWOdD55rav%2B%2BiIpESDgw1Qz60y%2FpY%2BzklV6uZd9E4KxzDR0ZFFENccg2eX03IH17oaej8r0YQl5CXtHs%2F85oBvw8jCYg5PRBjqkAXi8TW6Rv0ELdLn6ZPYiGqpEc7aC8a9KDmDtvSnuNned0hFRjkik%2FYDYWJZ2kwb4dXgcKC55Ao8INwH1cuIho39ay9RO8P116ayQvs3aIHcg4oClcQUZsEeKbvr78wkZHEUq40PyOLszQtTDsjwxpqCJnfJcDziDzeNkCy6uyFl1KHeY1mEbAQUQAgFeFhNxxUMSpLhRVecRUl9FfXqUl1rXHrIp&X-Amz-Signature=198fb3cff5386b33376324ff20456bbacf440989212c44a1fce1c10cb46ff7b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
