---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMGXB5BN%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T225500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0gr6ug2ME2f34F93YNV9402OMvFEuCZO0ZsrQ9QOInwIhAOWm85yxJZzVO23g1w5g%2BetbVhmow0Xd%2FBif853mRkNUKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSwHh6Ju1F3MW8ud4q3APqhW3xA9pMCOnZgvkSnISNHpQuf%2FF4N06WV6%2ByUP4vMQBVmbggCYd8561hejL%2BlmU291x1aoSnD%2FGl7ODTJuf3YtPRetjmPtcHPCNuZ9yUiaht%2BYO7mzrpTfhFBCSUVWcFGN77JDi3VXd7NLOvYHV%2F4FxGvtiP34OmxNCxTWTJI3vRnrVnARnGJzx%2BL4gFuEEI%2BtnQoF%2FgRyrAbWAcQE1Nj70JsEudJtSHLXQPKlFn68ki4IcV8Nmts8stP6pSQCcnwcMPz2PwFy3wZU%2Bze7iEhFcW8aggjlRgFFSWhOJbngLRjBALw48vlpNutODTQqzmzEVU6CN2Xc86vQ1bDPw6IQRwa8K8fad8WgIGHQ4NOSKL74lE%2BGl6cvPucv1yEDcv1M0vBIyRDHz7%2FXboaLJdbmcIY9unj4I6AARFEFc60PM6h05pcKPMzraKWfFtrcY5nRwKrtE5Whxbd6Ew%2FAXprIndIiTQrQMV9YvpdxpFGmesCOu%2BfSkBJCGl%2Bdu6ca8UDAX%2BgEgwbd5g4T54xGTnouXh0iv4SzDL4S9KuLtcvI713Ef1mxr7II3zV9CIX1rmyXTP7nnD0lzNhQGqNodO41PDzcQYAWJ7dGOj7qa5PkhHGro8Pn%2BFLtnmtDCBjbvSBjqkAT%2FTd%2BSA38DVUjHsVLE2U42NtzR%2BtXON2Vstdv3L7633jT8u9FVObekiquzdU9cgc0biYDVoyRO1isWn4tb1Fkk3m24rtVXv1GCUTgyefaKRrP8vh2Ifphb2QOCrePvjW26w9D7J6OFxloQYf9Lbd9E7BNXxpIlRingPTTy1esqFBC%2F%2FK7Ta%2BMo1hMCFsywJqUNJjduQUiKnnmc%2FwXpgR%2FWCDj8J&X-Amz-Signature=716df3bcc1582e0570280ee7def87ef3889be6ffe3bca7f5937a0d6456a12af6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
