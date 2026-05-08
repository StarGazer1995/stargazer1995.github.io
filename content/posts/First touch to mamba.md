---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOCD6ERO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T151414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDlCvn0GymwPWWKif7UMS7xSWfIO0WQjjesnonIK2s2NAIhANjctnMWHmqg8zyqd6dx0sa1I%2BUwzZUiTamKZ%2FqiXRHtKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwa8Xpix1FBOB9UHhwq3AO0t8jUkC4wM9XyrTBjgnL%2F1CxxPHr8hBNeQ2s45XJH0A%2B6kgPEU93o06Syr62HGXz58iZBWJIqG%2FgZopaSLGkqjPJCzD8OkDvYszWY3tkDBef99Xpc4EiPTHB%2Fnt9UId9XILlkhoG5cowhnk%2BhUVM%2Fuz0%2F%2BsVi%2FRFw7i0BtYV3waK7ZMzepzpJGrdN1kAI1dFQNE1qunjRoGpz5hqPYAdvRAAVJ8LxrPV0Spez%2BcorILNeWYgEm3ONVW5HKpbHaGJNBpw4MJu1pm%2FjldpBhSMC93IOG7bFJy9d3rmjaqU7%2BZqqkHjQsUziarxYiR0BkUJLIDvujppT6ZE3ekeeuYClnysUx3eAqzHKb3VWc1wuQg4Hbnek06%2FhRf%2BikRK%2B%2Fne8TDkGnwVQIyoa6w0gg%2BFY1ZoGCihBkakayHLw1DMraSbG7sUJZ4aEexJq1X3BSImDwa21N%2FndAimw0l4%2FTClxNf%2Bx4eGVuvc1hkt1hCF2Yx9v5TxQjL96bZ8xa19IqQyL3JoBl3aDpnxw7EBZXItdd%2Blzz3udCBjUdoGLoT3r6DGFa2YOwhMIjunrd8NqBmBGvPhoaJOhVffFGXasM%2BJF6fVDl0IdbQAbJuULbaHuFSkCU1e2B3quHu11gjDL3ffPBjqkAcc2gv7ejo%2Fa9Tz0b7DHjh7J6CeYcZYQVfmqyuCLtFRoQOy14uC0t21f7E6GaGLxEsTxdKSUP6TQ7Fw7t8wSDbro2gLBVzwSdXxnKrYralZKf0qflPc4zd%2Bb9a1hznvTyirhtiI9uJZYxVZu8ZBaHx8pym5JnL8KTpGkUYxXhXwDNtorZqoHhaNZkPMfTb8E397DFV13yxik6Tpznd1EhOElf0Jw&X-Amz-Signature=654fecca17fafe4c4afe2ddb32a0b8f178c882183c17e1102db8f62fb5fba9b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
