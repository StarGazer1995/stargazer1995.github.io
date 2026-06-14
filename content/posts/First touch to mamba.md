---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI2KBZA5%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T114938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIAdB%2FdzxM6PL2eCVyXRFWKqrG5ZoqdMPHom%2FeHOzx316AiAZCx0ioWBt%2FChLDBqKG9DKgQXIQ3A9CKnLby8ffx8sGSr%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMT0lyLXSPKUvD6XJoKtwDLE0Cwp80rhVTNjNLImwQToOK7eghW%2FSqcrzF%2FwzBuZBscdndwcQh6Nv7XOHerHhXoUt5sp26ThQfUdH3HmCyaG91jF%2BE6YIg%2FlJ2PfhY7bpoR1JkFAu1ELgfVR2MDXMNKWHzyd1e%2BVN2KamtL58KtVhVFMXuh6TxnsOSCG5lclR6hauGwKIwjFdCch%2FwS0NYOoEfDcTbAKwVoBMV8GUYDyWY4bpsf8hWgmE8pjaaM6mBFFSeCRirRqyOGEgD6nCi41qmmr5n%2BcMgWD6BEuLYhyyVJ9uqo6PJhtXKVhVagcNc0IyGeL09XzB1Y11K9ZV7Br0IwCvgJ42s5W4NhtgGEvdCrCZtGp%2BSCHSxnKUP7DnzRwJSv5DjA7gvTjDLvkozEQGRPQ3VcOqUKund1aYGDw6oldTt64m468nEhPOAULuNAk14JjB254ZBbch4yXBhB4RWovAcR0Qg5GOeE9RanlbrciMoqHQIeD5V9REeKxNVRHYCe%2F9EBtabZoeG%2BYF%2FppL0g5dKLcJhwO9uNA9krmNeOjq8aS7sxI8IKSBL0reqQii1I1Y0nnNDLzEzTkK2p9RIQ8uMVEg8Zh6zkMfyUGb1asF00JqxwarklC5Y7h3q4f7jEN1rrB6hJpsw1sS50QY6pgGNVgdEWrptuzJCG2RoVqdqKkYnWNAEL4kjvmUytuuKdwwXso7qyed5S5EC5rbGjJWyPW%2BprBxsJW80Eq%2BeW5SJqeeh7Fqn9tB3R%2FVNhcfZrBTmrx9TBy1SFPujY8qxJxabvrqx5ePnNsQ0%2FmeiFt7x%2FBP%2BWZYQPe7PQIKD9vMWpGsKM6xfxFrjUEC1fMDiZaV7az%2FkeIl5fwzRJ7LRe8v0wGP%2BHmHV&X-Amz-Signature=fa146b7ea6eb14506eb57652568bf2154d1d6f22a5620502675d432e403d5a06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
