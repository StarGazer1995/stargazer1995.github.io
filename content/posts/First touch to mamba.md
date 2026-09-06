---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RO75PHWE%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T175101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCqS1ZylSsCOHJZlY7Oprbku3FpILplGj73XID3JoO0NAIhAJLCc6STlAeF%2B1yL73k6Jalu3%2BcbDZ4WCXMwDpTLWtI5Kv8DCCoQABoMNjM3NDIzMTgzODA1IgzhDWmpv2KD5s4hFCQq3ANLiheVfsirN2YizDLwU%2BYkcsuT7FlfVx%2B2FaYig%2BZFFBjoD8ZI9bTgMBBPU1UkZlu2whVDO8czeOqY0WPKKJ6ncCPotEH48YqiFcVOhex3ivf5uOV2485pIqgz15pud8l%2FQC8bzc%2F8AuXlMsST89uPGzI00vS0hTyAzRhsHihtwKLh9KfLgDgYSLkJa65ukIVP%2BDAncDSR1piLfL7szmRK2rigoiF%2BaSt3H45rreGHxnz5NwZdorIDT26wKlV6GSrL37MQlxfWSxIIEEi6VBCc70p4FIc7%2BnwFyxPBie01ibo6e3AZCygj7C3onR%2BXPuBhokgPbTOjV3V9EJA%2F%2ByT0W87gXauogvAYqF76wVH216Uov5JBPg5BcagmfNDNW5ST3JBogIjGKCWVPirNPMnsdddYcj5GJrl8xsYXr53n2knVqwe24UqWW0Je4d9Spl0TBKnawgEsWiudOI0xtNm9sBDXMeqkqPvK6eaU6p33fvoCDTaHvVp8OB3%2BMdu%2BBjwbLfzPeABDF6tTQASaNIMyFNXkcORUZSKBjZiV1c6d%2Fum2SgzUWbu7rtb83t6iB3S03mnuaPG49MfEP9IZH7b6WOkbiQx%2FXC0Lck62MdnKZwYAsL5RgLrggyIbrzC9u%2FbUBjqkAQhy%2BKVaNLRUyNSZJQGwxjhYwQRNax7yOYij5WgjGlzoxEai5Y8m6FrzcLlysY9LCdudDjyEz7Z35BTaGCd83pRQTOZ5t5Bd94xsNlV1how6FPsgGo6jHRORHwxs9Knp5nsKCTX0Q1h%2B%2BAM81go08w%2FIn72lIK7zz5ytmRD7n4NLaVhyGkn1wQo4dkZ17lLzvtrfTUaO3eRESPMTpklYdtu43yzB&X-Amz-Signature=bb7262113402873923cde272425c8090fe7b3fd3080d00841daabe710427f5c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
