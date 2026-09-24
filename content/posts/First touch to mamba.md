---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROQWV7IL%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T181039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIB4TLgw6tK%2FisNP2qtjJtM2Vy9blyg963zZ1fDysH3poAiBMp2BoaUeuiIX6G7DZ3y3HSunfeW31Uz97nhNwkqtjmyqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBKJT8A41cz6vIKfxKtwDlOfSVXIafi99qm0PK55byCwT3f6U95UsGx6npB4fXmLzknPlhByeXSB1T3pj9WXkFzJF2Kw71xiys1GHRce8oMgJXyM9%2F1TPodY%2B%2FCxyH%2Fc1pNg%2BZfORZaYWyfRp8DRt%2FzoG9fyl06kZa62jp7lM7n9FKMi0G96nOYRW4jnAMamc2KsPvJIKZLbiQQxyELv1tLs73%2F%2FJmEsq7kVLfhCtEbRSpiJ76s2WTAurqH2y17fEe6L0%2BzkVcmKqI6WXyJ%2B%2B7mOQA9F0BrhhfpdpkyynVXVE6MD%2FGs5AIZNH9a6ogQQds8ypjj0xxeL5p1g6%2BxM1e8CeRhjVhvLwFHr97cI3an15AeteAqqYcimdLsNoCDZwBqogV9Kp4SprkdfdlGokPKbK27CT6cYziig2m3MR1KtDsmcd7kTnu1HecN0fDWjNWCIzX8pyLYFs3PgXkfY%2Fi%2BNO2hZS6IUdAUyHSzV06Lo7lCebeY%2BZkoaPagurMxBzTrsmKkumoEC1JKDJBmcX2Aoen4eD2lIuo63M%2BGEkY%2FpF9zcpqti2t2rN7%2FHUWHnykFQiyXXWhWHrm1ODfW%2BxRl8HuBQnz%2BSnW4RyxGrW%2BGDqtIlAPVkX6m%2B7JgxQ52KtrQv8PpRFORqsOYYw9qnV1QY6pgG2wf6IOQloNZh6%2FqQd8z57KcG0OtyUMLkPcFKcMwv98ttQV981XWtbJxxpBoCgk8eK48oTsbgAabPQVkSPgZtcR5tONRfuStnIe80Nu7ZbRmB0F%2BGLj6LOt7HoqTg7r8g6u%2B1Wzmm5ApVtW7%2F1q1hFa09NlZ%2BtwyW8gSCMTyapua2hAGEqe646PjIgWSzwXEfsyU0zTheAJTYD0rGYYGEuyr9RhmI8&X-Amz-Signature=18adeadc7bf82f456e96c5a19cf1a31e088029fa8bfe253c3ebe4e100f115b95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
