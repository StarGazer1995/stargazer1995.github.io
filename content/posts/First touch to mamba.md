---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655UONZSN%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T224559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIEz5mNe1NPklu%2BvSH5nJw40Foj4GJ8KwzwZmljqG8n%2FjAiA29fjtmnMbpSlLU%2FVf8%2FGZdQrBRf%2BCZwYyr9ZtgoP0CSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMcx5YRTMsuc92aJrxKtwDH2fPLawB1HPGOVAsIViuUl9y4Xb69HE06Djqw9%2BtTVt4xGbGYhYlwchc8n0gk%2BB97KfCgOkRz2iob2YSh%2BTLFmTi8gtT5xCTexTtyioAHLE1TUbwOYaUctqezW%2F0yPwQ3zNgryY1b36HUI6XVI%2BGprfpmVxuiuaKvxzygyyCPak0S7X%2Bhs2yjnx18BVM%2BecD8zMF3Ybm%2FUpowz7IceFjVPyaOMzQtdrj%2BG2r0i9YHDGV2y%2B%2FJH%2BT2bdgutsklL%2BFrxj9vkwC6Ax0CPutv3PF291%2FtWRCdgFVhuqyqgpkWfoOBZmgsWJAlYKyg7XeLb%2BxiYkkKpI%2BSKm3pbKtcIjXPQQfi0vZBJ4sXOabbL%2F0lrt4wZlqMabMwNfRDFGUOT8j34f%2BDNWXhb9Op%2FITUZQr2Oq4HsbIsYdaEmSacOwatQn8Adcf827XS%2F8SGafq72zUPKM81zzmiZse1VF8ym4pkH4%2BabiySbx0m9DqcJzP9zWHQVeqA3VRWrqXAdx1taoWpSc75dNo%2FN3Jayp9eeH14yMPVxQ1zzSADFd916xMPo4ZTvGAaxuhqGsHQ3KKK2APcv3aeid5C18%2FoP%2Bc8HKGKaiqtmtG3Iui2wTVeC4zi0710sGzSOzgAtB9lcMw9%2Fil0gY6pgEX9oDAGY3wNLxrZ6jMox0yN%2B%2FzSTY23UXDXhRfOxv3uaKtwqANZMbbIg8kj%2F0Ua4K8D4SDkO1PO4ZsJQ4PkzwCKNGpT1Gg3ACklNTKAvrMPtP7qjoe%2B5ZUKUzirdXiIjdICnjT3zfo9gtxj4scIIHKJZWrb%2B7Ilu0OFSUEsBTGa7wsyvojz3xHYJNK3AvFJXvTgn%2BHzhCTx%2FwpJ4vPazuHO9NwuSCN&X-Amz-Signature=29f05855967c86dfaad7dbee4966d5aaf80cba39078057176c009a948fb9faca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
