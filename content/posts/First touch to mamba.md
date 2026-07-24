---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKQATZMY%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T045852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQD6GQMHaiGfxo41yLta5W9o20H1k%2Bxm8oZuqdS7kis2mgIhAIGKKmbSMNEdRSn1pXENKgZstln18YSbKlW2K46MQUjiKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzAnWd%2Fgr9K2HiPPXcq3AOoREhnZzH%2BjGj%2BP4UL4xFQiCzm%2BZLUYufVCYOQ9cfbN4YV3WT5CTyvUwjJiA3CDJltAyzUCIKGCPUjJzQ6JzSP9g1vBS52TOzuzwWiKmGb0WEjBpyhpp9NutPObELxEwxsGU8IcIBCqSApyJrkmUvpW41vFTmc4ZR0RxOvkeeelcrlUfTL5d4LbDTU2xessZUDyC61MRQ6f05LWTCrRXWBJOHUrXKlUzUb%2F9%2FygW0Jm45eaF4rkg%2BPObgebUbAnSV1vpEsQneoV%2BCTkgVONtTVWJizuKPytR4A2RBHJq5Vhl25HJKxZfkhT9D8ryo1vzjhhH5OwZMzF8NS%2FrFTJphvPxT6djq3JFdvipWRTD%2Fdwz7JzzoU%2FUoqczzFADYMtX%2F%2FV2hntJUtom1UVEmqlTnfDquS1cws%2F6%2F0ieGWE04EuXrLYa88mgCO19QSbJr5sXV6GnF5Okf6N5%2BMFST%2Bf40jcEUjoKfJte9IafHLlb9MGDbhDnBLmWYG6E5bgvFvt5tKKJ14mUMONBQ6FttH1FG%2BmMzXtngSf9opA%2FZIfXOISgoVUG0UpbOxydiUxuLWRc%2Flo4mCn8hgLV1Swd6Z%2BL47ajwOkEal3Zzu%2BSjKkw7NnyJ2%2Bqgr0mykmuPLIDC2zIvTBjqkAUHczgmJlNKYcGOEsepStobon%2BveEUwCcMUI8yCSt%2BZANoVbkYHpCgFXU%2Bx6EqNkrn3eHbh6ITKCy00Rnk93T83Xdf4Y7fARe8IhQMjpllWK%2Baq8vluArA3G%2Bv%2F5Gnjie9N00p%2FbGzNPQkvHSltVbv0hsc2N3FIh4HzsBJnlZc04e9nIiz3yH48qtIdQKfE3qF1cuFclsndB19pq6XsdK7HqRRe8&X-Amz-Signature=e888e7798efe24b4cc9aa44575d1e9f08ab3ca55334cd9965706c5df5a7e8189&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
