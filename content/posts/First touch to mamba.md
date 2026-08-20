---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HLJ3COK%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T101852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEznhaoWN1W1h84tsKn5HVBFlStcKyUlKRasN17QDANwAiAeae%2Bb2vIKTf9IIFNQsPKpHnmt0sB0ESo26rpRmhMlFSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOMF5fzNvgmOMdf16KtwD0jZenYaHK7npgRyYc0SBlDqr10KaY%2BD8a52kDnDsY0P%2FGz92aWaOaxsmf9cdx4Hzsop6d5TDRE01Roxzoni7pz7qXTb5UBsOXxJN48JPMyhEfnAhco3V2tB%2BEJYf4qQuE6elrMI9mnwt90746GAjgLHsJ0lyZKrlaaADhBJHIgZrumLj1jnJbyufGWkTFCKDvztvnMPkru%2FVpUsiVpKAJtUPJNJcvDf3guxX9u%2Bhv3I1RZrxtPXo3oYq84Tgkhdz%2FWaIeWuIKD1%2Bm92js%2F9o6LzNw5g02G0yfXpqpYyiYBsehnpmhGBZE%2B3w%2BAjSEFCiadXDJr3yKFDXk6b3wfLJu4AqJT%2F%2FgEh6GPIxv4zQEHvLZMXRaNXdOVcDiy7nNTNokM10rWZjyRlEM6oGKU1ag%2FuhxLGdfbVnmyGVuY7a2HO4eV89q3%2F0ANxPJKkXsHhD42bw%2BzkSxd53v2bqY8bIXPVt4pVpVxT3WfdjRigt%2BzJOHkerFeQtY%2BQSra71uQWAKp51NoOpUaoekGZuzgwbJcrg8SezzTVraoGwi8glHFea5L%2FZe1MK8XXq5IvBD2TW6gq0xs%2F3BEKLceJiLj1zsT8gm8L79usS4BmJAmBJJQPyojzJ7b%2B%2Feu9QJy4wvPGa1AY6pgHazawdJHHBze17kh3Vc7H7ZCBOM5Qdapv%2B2ntvCIKtxtuXOhQ5ioDXKNakxtCAOYXyXNb5su4Bc31vSoBmw%2BvkygE0aLjhA%2FePE4m1iS5QbBApS3eNxJY8UWQb09hNEKylROrNGiJ%2BsfzSh%2FQ4p7zOVBLxWrTfGurm7hLCQYj1Shkeeg36FouSzO4w%2F2jbHZONl3uUV4wTLsUvpK1ShQY14LnhihPW&X-Amz-Signature=4806a4abc88eaa56af6a1415bb82a1925feeed9d89f51894cc74631959e3139f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
