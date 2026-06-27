---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBULNDO%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T111916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEHC8L3uG55g2zZ%2FWnlRg%2BGxrVQ9IlVno%2BkjhLHcyrEAIhAIg1Qtu2HZrI5HS6dUjSiyr9PwalfJJZ%2B9XcIgDhMHE%2FKv8DCHsQABoMNjM3NDIzMTgzODA1IgweXe3UbaieY9bmyhUq3AN91i5RH81MGpm%2FO3nwHiEAxWv6FP6qHLwvsl3cJBVYC1x0%2F9IC857FbKOKmMjsHTbKioj8G5b%2FEOp1%2F7CVKqiyF2Cgulbtz4ZO%2BWIDcUoIxwKeFD9vPXyCW2KdruXZQV2zY6k%2BVRhlOLPK5p9rv1rtlsBWfdh0hF1GZr%2FudMDKOGQZqYLeegpUBgqkYLEJo2HIA5NKg3mVHVxo9QZTsKd0gE86m%2B6MT5V%2FTffazd7wD8sxrRZxztTx6jU3S7enDQEjuCknQcph2828O0ckq2dsVTO3PsvrbqMfg2KdgK%2Fjr9mhSzQ5oyooBfgyXdm6%2FGgv7AI6tTMpcBmL%2FFW%2B86huCM%2BOTBXDsBk53FsST36HXsfRUJe9rM0PO9Z4MC%2BZteMDFo1D%2BzWwPmP0gIDipHDf9z3Rf6ouITvHA7hrzSOG40UtDxZJKd2dj1riTU9RfrjJ3vHnTFqYOjt2r38dBKJ3YJy1MKDzdVEtiML7bxVgERsWlPNPxHeFplWNVK3Dqaqbdy3upZn%2BnVVfsrjqGPGJPFCkI%2B4DGIKOqnIz%2BPoQD4bkb4cPLSCKHKx0rtmm%2FT0%2BIzoP3QT3mU0LvO89fY9eXfw%2BsYhi2koQ1DLAQpbVPE%2F%2FIpul21T7K7irODD2yP7RBjqkAeySEuCez0jub1b%2F5oPYz2BuPyeZF29796TQXVwYZcs84BZJsBjtieoV5pJxNoPWSdy8F2vK3LBUke2NjqNLUqxoSI11htDp86azaP15hapDdplhCXIwp%2FM02xy0Nf9N%2FFQjqC1vtRiew5jTwFSYBOCzzz%2B3HZe5vmW8nK5dLBjS6qw4m1XFSb677cJNmJea5ZYS6GW3w0F3aToPoDU88oXr1D%2F1&X-Amz-Signature=c96979f288056a9751548e4c71774f1659fe7d4d1206dcd86c940f7c1a2d8a26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
