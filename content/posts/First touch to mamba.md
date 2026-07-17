---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SFRBRF2%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T223830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKO3tu3946R%2BlHh0ebLbIDCJR38S2kKiVcRR9GCDgn7wIhAIkS4dnn073h5XJegxc1ZAbKxHn9GSXSqhXlyncHAjSBKv8DCGcQABoMNjM3NDIzMTgzODA1IgyDTLXBwJ8YvfwcE9gq3AMgyEUPsuW8hZltWCQu4IyJFKyEV9SMlaY3eS%2FHFG8WSg%2ByeIWDmGph1vFQRmmwBqoQh3c1PBqYT%2FoZHKwb5wOYkKjWjtpBdHx6ckvRjKzucOdkqKfiwYwXhRDtAiTed0Vhrrwa%2Bfq2wtplS4vFzIebvT%2BTl5FQFMWPa78rkOqyY%2BlNbu9iNwS3o0eKM2ccfoPwF%2BXTULVT0LtmQyt9Z3d8qblk2Swb1LhLICFUY6fTauzc5VsbElVfqRzUqhRK5JmYBUNwWr75ZhTszxXtq33pyiqv6XSV3%2Bt00l0WXHl%2FSUZAAFs0Jfr%2FyCQru%2F5uRyKpN4lrXCurT5pHYNJ7u0cEqzFUx85GzN62NGFUComwsor5zG%2FvPPUSNHNoJmJ9LetL%2F80kGkLQi87TMoCv5Dp5YjF9KV3ofvRUxWW8tnzcF5a5suM6RYx7UZ14pwp0XCtGqj46Tgs%2FxK5G23EgHJJL5%2B4d5hIl0gIGOBT0K7yaLWMWUmftYVsNdnVX%2BzufE2P6m7UFzJTrkBeL45v%2BXF6GgaXFc1pozkN8780wky2rqn%2FGkR%2F3ck%2BlURgaBaIDkgrNpZyUVk285oJszGZB%2BlIcUE7gLixb3B1GU8R3gJpctuM808awrCqFGYDafTDFzurSBjqkATYEBnFqsqXULeuQvBgL6Kxx%2Fup388ojp2aUhHHoJjeRxPsXfPq7ty4FK7bPlueQo6fUlClQu2ARw4gp6Kc5FBp31xGHhj6tqod642VaoqJKYsXz8PRvwKJqtw8Yg%2FPMoT1eaTYGPDQpN7jkVRg%2B48H6xYoUrGDJbHbxnZ%2FxwNgRIFsEJdUOe1f1cY8dbM1ID57wPN44ZyQvKd%2Fk2yCJAa40YFxW&X-Amz-Signature=4bac21c065767cf0099bce1d52328f60b278d817a11c459e0cdffc18eccb0a82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
