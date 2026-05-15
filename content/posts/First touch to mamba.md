---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP7LKV3G%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T191439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjizTJuMUPIK8tur%2Ffp8VSEXKIzYZFW1b5TJlkkNp8QIhAJcOs7OpUtgjSrRNxwtK3Q2hmKeMoV8t3vk2iS3kDJbtKv8DCHwQABoMNjM3NDIzMTgzODA1IgxKVaMcChXFeGEw7QYq3APP8VSaCf2AsJPLGMEQC49vLSj40shYTZmW2jLTH4oOxZ3cGAjUJljvabjonSnBz32r0O5ScngeUPiDcWZ3ib587evsSzdJ1tRCL5KRs1DlE18ltZaJ4UjcQcJZv2w1x08UnwCh%2BD4GtCofeMyMqQ%2BsUGkvMJ7UZOyuT%2FQ08wqYqFTxm5rDo4ockjEbhTUrdhlgHPNfGSv9CHZAYtFIqs7y3aPOVYo7nl4BgUqf4vKaq5IEoN7Elv%2FFVhR3nOAjZFdD4Kn9hOpkL3aJwF%2FavDLLq2iD7J2rRNUf3VYycv%2FGJx1ufkb5Z%2FQTgjyHJSRQH53g7VnPbx40abLMWyd%2FOva66OhQ111uAZuoeHr6c%2B31Qnp87CA9Zv1%2BPjv4tydc2Px8wndhbm8BMu8ygbPSTKF0408iXMofzgRAI45b%2BcJtjVyJD%2B30CZlUXc7tC4EfK8gJzamHhwVzt%2Bo2iijFGScJlq%2BsBK0QsN5dVhLuCOW8V9C4EhqYQLHiA2S7RxueRZmdmMSXZsDqLMPNFwB%2FoIMVPEdnS1fp3gNJ1Moy03W1DgwSPG7daEBag6g5sOifFLCP%2F0SSe9A1QCYbF8fUW%2FKt0urJEgLeohgoVKWaGphoP%2Bqg0e%2BPF24sxBeuMjDC4J3QBjqkAesDsoXxZizG1f3fO%2BghUqgHqXGWfLnL2pf5rmrCjOsj54PBMUTBlWVbJSiP%2BoOviX516SaXMNiXyNsNQgmg1XNbk1nHZoCP43I6SXvx%2FoJOgDZS%2BYz7dLj3igok2VNSXYAZBrJrd8RrA3dvy9DAcIm8yVW7eoxw5dHfCRyI6dW20llzzd0W0pOszjy1jX0T5BDvwFqU%2BaPr9jbB1ZLz3tNwYkC1&X-Amz-Signature=d8ee3bfcc1304e38cb43ef5081a1fb5c358f3f6ec695b41530e53cf2f1ea5626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
