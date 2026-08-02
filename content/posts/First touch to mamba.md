---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJMNCMDS%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T224435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIFsKpuzr66taRxor9dWv3nEPBR0RXbtQwj5tP4dZxchPAiBiYtJbUPxmvCPtKswkrVhNY5sywccyBTiBcNJNYnPayyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW17wEwKizFHo6xPdKtwDdwdiXS8%2BhmTHB%2BB%2FNEe%2FFyWf%2FGs0m5vqCdrcRpFaxU7jBxzeurz%2F4ccTKh2W83HygD4GDZU0VS6Pg%2Bt1%2FY1yqitVRxjvjRnGKS07X75nLm4108%2FFa%2FfFNN5UxngTcOHmjyS5tkf4oDBbSVxQVmA%2BnMaU%2F0kVhMKyveoh48lcg8faq7ej8ipbJ8HuYQflHTdva%2FdJ1oVTEnSi%2F0D9a0k2l0uPkXDyHroF8qLggbxmZa%2B94a%2BYt3EzdbXriZ68A%2BuBkvwflGFu1G5bbJ2T3SK%2B8UQqTdnaWKK%2Bk3TY69IlCuhNjUhCZcvhqUgH6HQIfJ43oG1TMLKD1zzOF8%2BMGOhNw5k0mCG%2BGSZ14Kj0NFO%2BOjOAF7jI7alRbipZQPGBfbMfC3lTw%2FniQLgmWD7G9kRim0U0KWq1zTkdbliT%2F2ZuFQ582sRsRCEMccvcA2xFpuhrSUnN2%2B7fbwuzNCBvW6jvzUdo4KJfg2lDzzDDeqSAI16FI1cytpsWWFkO%2FTOamg0ifBHS8jmxD4rbqOAuK5oKeRJQcVmvGPkuJiodthYXZWvuvDr%2Bkt2MZAcQSsgBeqbohlKsU%2Bs1dRoHZl8akIUVQTKHr3HyFcS0NCncDswiJ4V3PwB9YiXtmtBuNjYwyIK%2F0wY6pgEBY%2FIYjLxmUdVwBcbeYz0xPR9bpiRbOEzOqGV7MrFflRqPf0tAYgxBoWrssUqFR3zUsGKgoMhtp%2FOI%2FjLMyDOHVb3ZPlMU156KvvyPPcp71rHcbvuaqSvm401HKoXnadHgYkzY3d%2FeGbfbZ7HKY1CFlFc4C9%2Boh91crHqOB8AMhd3MvWcKdSPBjCU15edor833E%2B5bD7lFiNtVaUE7YspmMXU6j38a&X-Amz-Signature=3530d7385c0d81d5d2cbced90e8ac1984f5f755090c729725562f9c40973e6fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
