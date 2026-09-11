---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAAF2CX%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T201054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAou2%2FsCnvBIVWR%2Bcl23mkMOA3WbO5JH0cJwiFxzHittAiAlUs3t8QT14gctr2F7AURDKWfnu%2BJkkFoxuSHnJ4ZDBSqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKBa2cAy1IZO0XHuKtwDZAMUReDb9qqyKW3pycXl0ZJdHDvB8ihPWgghPZcIqdlAYfbhbU9KdpCE6jwrkecdrA5JksvCBgERXTAMahzBGyy2KvHHCFR2y%2FUrO68Mk3ZxWYWuppYJbXrVErDCQnlrf2%2FTMOD4rq%2Fnxby2EUeF738l4VMVKNaE3ziB6tYwIoT2t3c45ToeYof5rnJ9XTbHYxsLYCotZs%2BUQ0ILeC7jcoI7dtp2yEjuP0SoGq9wP%2F%2FGNCbMPqFM45KA3qccVhrSOLf7TqGIezp%2BJrOyd8TtMfDKKJMBwj%2Fei1yPl6Yq4G011ZuVCybcQX6Fs39KHJrkA0sda8hfyARFZ6ICXvNvKr6DbmipOYXznDzzqLH2YfdPaM7%2FkeCU85ekAJvaImno6%2Bt55oKQMhMfnJPVYK5395YXk2nT7Vyf%2FkYdeI8aGltI7rV5WsrqYQgIT3vNp56bBpqXbY9H8jbLFNAxnIdGKWivaOgSb2ss9oeMtuTVASlOSHvrs%2BPB8GhWwsIrYB7NO%2BIxulKoLOTyoBnL4rgDtZ3nmuQ9vGZJXu%2BDMxwpFB0%2FXL6XsbZN%2BWJXBe3zbmtBRcc0SUJQVCdadNrGCdK9GMmoOre3DiWJLOIpzgSBrE3rZs4EuO1co7UPL2Uw2t2Q1QY6pgGDVc0wyi7R3ESwvbbjH91Wz%2B%2F%2Fv%2FclFxGzbo%2FWS9K%2FA9RdfWNbl4vP6NmCCcXO69yBtT0qJ%2FE74xLULSAncE%2B9sslQcYdt9xMvq4yiLmxK3Nxj6FwsKW92HUoygpnKkJkZmJy3y6ShmYrEWoklJXb1HuqupyNrOYyIwCDrfYSaVIXJ7w3fwUjtHrQHF8he%2B5rQCzPv9TMTgcazr35ZtuVYhlrpQVd7&X-Amz-Signature=c71901686a7332672374307aa73d61cad508c067222642acfeb531f9a9dea90f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
