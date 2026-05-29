---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFSBGNZ%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T230325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDTXSDlQMEUgbPyXKKQVFyclm0ZnGa%2FKxSA23pjRNAM0wIgD2XARq%2BH5oybmV4E3TaBCCtObK6ekG0jGhBbbor2rqcqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzGyIMWMITYEA1ooCrcAxpHafHYVp1zjcv%2Bf05yKt42vHjsvMkVxhDg%2B2U%2FpJ7KA%2FDbeDq8DXBvKgTOYpWpMofJpJ3Iq11tTMitx687MxP9NjdHRar2f1FVeFZ1iUSud1Lf%2Bj1olgFuU8uHG61rUqpIXpTLz3k1oJ19SvgwJ9xLc65fZ5zlxOFCni94gARnJZpgkEfKEb7A5pN1caZ48tICOuI00a2zemJGa4UP5FD4r3k65aGCH41yjKnsrcnN6QIZqOGo4o5bkUCMyb05Of4aqrdiUJ%2BJch4iasArmFkLavn6akkvG5YxNhSReJBIiS7i57kBDEXsK5OUsaxWDE6y53SH3Y%2B9GBMzLxdieGzc4LdMHEvQ%2FhfNW33x4CAoH6RSiZpKb6Mc2IRo8ykhRtRX4maF%2B4yHIIBRxU3UDJfOu6S4iEhAaK15Rf%2Fu4HSiKo6dTC0gIH0p0dFybCsaSi2z7ak6nw0Z%2B9tDvoQfUZ4hooL1J1O6nG9mgYV%2BpuRsDTAMiDyx0bhwlhxGvXbUO7RQE9QDeftnB9X2bYKxgw7OJ1CSavrbFVEVcKeBnoGAonxusmgxZvn4gZ30ZYm5usv0fB2djwiKIJ3JDiUwyvEVPJkmH1LxC8gZu%2FGxszLmm%2FfPzAYc7nAMorlzMKOc6NAGOqUByORUN48vLeiR4%2Fgk8Fce0gZTi%2FS%2B%2BMevwaxaMX4KJojTSuHG4UmI10Hai%2FeLiyKrvWmpkrXVdijRE2QJjwr%2BZhAXsWZwSPZppdo4yiGTBRGnyQ1e2pGZ5qJS%2BEXEl1I3oVcEJ8%2BK8I2NrxkyDxnVvzJpvSqQQH2k1W67mHxeJeWRgg75BAkL%2BxnB7QvANod%2Bu8bmnEqTC1jWAd1HYoJjwRc6yXkz&X-Amz-Signature=b86e5c48c2783aa4a6893b88c210fd274bdc8d7ff61f63e46d5eb9f587277b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
