---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSY2TNRW%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T225247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWtXB%2FuJnfcGWu137E1MuUpyNO0WhUv%2BDaFrMnmWo1qAIhANDTF7dNKsGNvYuMwhH6eD9HDkzBoX9yljzIZz2qEoBCKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyb%2BBfU8qcgwynMD4wq3ANfu6Wi0%2BWPau%2BNsZVOBlME5tsIMgyBhFKF25P7ZZ%2FB5%2FKbTdLM3QwdpDD4ctc0RX%2B3rbQ6xAy9HMIw2UTna3MmOuvCIbUDQMXFO9WDH0kojFarYppv5W9zbq%2FQBuT%2B73AUsaelOhWLQlm931iJZV0dDg9VaVrvUNpY56JvRxt5Zwb%2Fxw99h48Tk1OmDGE09HgqQDd25ybMw80%2BrHAP38ir0OCs55PeC%2FE6N9rJGyniz%2BQx%2FBweFK7P3yF2MEGXA16S1dKpX6a8njhgWxBYKBYryZiANg0jVVCqYnYcO%2Bn0rjx45VNZSq0xvZJ5GTIB01rD5BtxCvEbPbr6xbG8VAsvujGILs0ie8v8CjlgCdQMp%2BBSPhw8c3z6UWxIHTqF591KUjqeTL7SlPVcEOnsT7DO23qrSHGdjo6C9hOwX30wzEbQ5e18FzKqyl6iJiplrAEl7i%2F8CfYZ%2FtmLQCGP0EDNUO2Bewetxgcy6wNiJfmAhCoIwqVGBwUpEkV89h4pOkTlMT0guSeGL4Qjnk0X9449r6B7XlcurHsy4%2B0Q89mGTlOLbXQMVjNFcOrsTOGTAjsYjxOzvEOIJi1Ho0n5SqgokxZItdQg0sC0KoCGc1J6iZGQeh%2BEZUMnAjnTnTCr%2FYDSBjqkAc7esxfDzSvAdIL1MGADXO146LaQ8YaJFx1IffA856ppVsbyUvXGZKemXVNiRtt1pa1aPtuVTPEqRMNkUWIJx%2FqIWLUlIAGAICOwgqyh7Odjgv98XHUUNZVARJvmZ8x7ZINxCj6V5s2vT5m92ANhm%2F8CfSPq37XoPPKMso%2BCkBzG%2BnmVKOljs1k6xMZ0uHWuR1W5aZfa8CZ6IiZFOn4MEGHVKKrW&X-Amz-Signature=4015b8d8d6e500fbca92821c778cc4c10da3a35cdb1b28dff1d3aee4843ce43b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
