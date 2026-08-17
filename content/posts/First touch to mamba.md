---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP4BIL7G%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T201413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvV9BCSJl6Ky47OV5mR4QGc0Lug%2BXv3IWbhNwVIw5uWgIhAL%2BG%2BIrHm4K%2BRRbF5z1N%2BzT6gjlieS24z99OeNARxv8wKv8DCEwQABoMNjM3NDIzMTgzODA1IgxxOaD1bNh2ishClxYq3APOJE1NUQW5iQyJZcMmRf9ET2VrURDJnz1yKePDcJ2jzLeqTy6ejbBP7mwTq%2BIAXK4CWTL88UDmCvlaKUGgVp5wmSMiNunku02DpCvRrOf%2Fbieb4bfWoTaWtGcGwMXTbiMEhiSyVokyR5PGJikkz9FRsdMoAjZrkGxMywZyC8rFVMCAnqNYZuorAHF6imnZIvmY7KVhUdELFFpeKgHKaiB7UyWMzYPbE6C3fQ%2Fy3beKQEwYeiH11BiRKV9gsU2fil8Lt%2BVPbZyV%2BAWXNtjLlb1ZV0mSB%2BEU3XXsIUYtilbU13CoqiKuc9hzgh5A16geZtRjNg8ISGEE%2FeZrzfv9cFafk%2FouswKEsHUjjdl1w7tbnWEoisV9yZbNSUzISNTSL5wFdzBmk%2FWJg%2FFGOZEESItOEo9ValaFSfERMCj6ORbCwlu6c6WS5Wzd%2FutmaF4%2BTkdjM2L%2BCNUF6dQizJh3%2BsmZeZ%2Ff6McgW8xA5rPy%2B9ofJ4gqweIghNMSIq9w4bRH02fr4TM4VdFo5zfOdL7zEnBEBdvkEo8D%2FGmwyTTZ3EMawrJtDC8KsuYmQ8aNtUTW7AX9GRFa1tN2Xr6MvubzVxAfprp52o2UwxZ%2BtT4VspKcaUUvlYapcivSbazbpDCmpo3UBjqkAYLFIDxAlbk2EFUlzfxggqBjwi0GIKyVQjEhBPz5XSKpZwLSsjCaS6cBQRqRmgCjTPDFKNNv8tApZ2p3kZbhJI3kIxccfVWbYYwRyaMj4E0mJByD1sRezUe4AO%2FFeij1svUYainVNFoHtyVWihG8e4fFXHbPuvf6UB7cNuxnHr9DxWzEhMdQRIhn1HhcS87Wmsth4Fov%2FJRe9183sl5bJf71qCRb&X-Amz-Signature=9f34fb900f876231c27c0d977a4020e2323d64af2dc8f62081494a242ad1bba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
