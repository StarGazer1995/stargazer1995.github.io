---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBJFUHZY%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T052818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FCtWityJiuVaLB%2FwFWl1gogGlCUyqmczWY9ciFcxwRwIhAMh1GfcxwjPR0BpIiZnsro4ckSTXWDTsJ1%2B83ejO6xJdKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzbuam54p4VWpk7kwoq3AMA1eN91gJaA0POy2cCtk1wpyaeAynhetnpUv1MI4b8DhzoGaHMVhclQcB27BvpFo%2FhshmG6GVag0WhKtONVJ5Irx%2FagZ8wEKLzln6vCcN4yif1BU2%2Fj142awIKkx%2BO0LffVwQJ870L4MNNSCVLw%2BknjiUJU7xAKsCeWVsl5PtGYhnXsbcL0WcE%2BO9eL2pRuQsZZ2MbP6i3O%2F0xGLsgS4vRaEHJ6bsFmL4M2TrbTwJAHdfNAWQc2X005QQ85rjj6uxnkT3RTOFOCgb%2F5SB3AB1V4xPzDwjhG%2FlfAQrf1ugGYkwU7IKCEwPX2KqDb0biWa8%2FMzGqnAF2C4NYZNwDo0jAopFEskZa2DKMmuX0vjHzyhXXD9amFnbrcFsORAbK4cymco71WGA1nvHGvzo5jM%2FA00g6HjcrEvJAm91mUWptnXQCPr7e5OAygEdW8VdKwmlghkqO%2BsQG5gJwJ8arkb5NWE8SQzVjqtyxP26NW%2FT6TinEe45gpID6di0IcRVF7%2FvfXRSaBsWaa3fmEHBK6JccFlmaAy6yNqvWvtjvoRtmAiAHPWjAz8y7h3nh%2BEsx5tyoe6DvE4lUOigZxVPrzTA58%2FQkOgAqfTt1Dt9OqrnFhE9xUj4d%2BHyPZMwmmDDyr%2FbSBjqkASN8cos001yBlyeB6%2BdHumPp2GLGhcE68vFTk7j592RnoE9RRFDELV1taswpUPadGMnPcBBD2P8yPGo13C5o%2FLPlMUWc%2BFNal2Rj%2FT1vaQpgjj%2FVZONuJ5seSAiTqngpXsFHYGiNSC6tvRxAWNnWL37OZsJBPwOA9NZ3FApiehOXmqwQ4ksrvVGPCSYgHj3tzcqRlPae7AlIE%2BgmZslKRCc8BJqa&X-Amz-Signature=f36af703a346b5e7bba228fe7e8d093e5743395408616c37454c7e081e5f39cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
