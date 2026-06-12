---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QELQZ7A%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T124916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDJkiw%2BrQXBIcljLwS74I5sMBT7RCDq4h%2F59CRolYFZiwIgZfrFx6NZ9tIHH%2BHds9nitrlJYh9zW1CA6NaZBLFAFsIq%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDPpWx1CrNCfPfpX%2BjSrcAyXh6qS0JsEs%2BV8%2BScPNnvujmP6DkVtlgkRVLJzwnW0eTixAi1nicEF9HguTlS17GsvWM5%2FHQTFnjucSKkKec90eZI9qNUYLIOYNfXDveczUPycxH95azvUF6RYF36ybL8taTZRxnIBB42ECz89cbn5P%2Bm50%2FsNrKreD5Fdygnc8QMH0T4poMizCP8KA1WC1FegtPGQoab5qgZ5fs9p%2BXvc3hngUeVzrR8DEk5pLlnbVQ%2FxofZsRH4tCD8Mq6RUhHfOsC%2B4FoFZtmhaDVxnrJ2EhJo0MJ6FdTFpF26uUuzfrYdV0mAstjAUDTXPm8eYxDS9eh6fChSb1YG2RR9dV%2FLf6MmqEk9%2BAhsqvRVBlIqJYp0PJrn0XjAsP1RHxjEv42dAKf2fn9yDzRtC59kg%2ByN%2FQWJPOV5LkVN%2FX95WMa4TirlzAAarmSnMR8O3nruF3H65U1OwgzoQ8FbvFqGiF4W7sMhEGeqbPn2xeQRg4y0v%2BY11UY6VwqWb8iyJu7j7SQN0d7PRNn25HF60h0o1SGjetxlvFKf6%2BBUrF19lZtmOozQmfrQHWq3A5L2WLl91YgajOX%2BhMYrpN4Ugw2HslhH%2FKFgiI5pBKhdQjVLrtTeD6bNoPt4eHxrDh6i%2FgMMygr9EGOqUBvzfmGUogD1vRdLr%2BnvNnpANbF5ZvknoWvS1BaNwDMgM%2FHokay3uyYVEDB7NwaYrsGiIBEZI2sSewr7eg%2BjHU37s6eTmj9li7jcYkkUI6ddCv1GuuOMQdjQL4ItjoGLze9sW8HQs8fFxE3DiUbvxreTSAicH9BItKu1%2BreQP4Im3Af7eoKQ7%2BGCBcI9pTf4xzxJK9hlyrO3qvHHzTdVZ0bBvNpQ%2FE&X-Amz-Signature=8621d9ce150d7a643ebb0af727c7c01a0e13ffb30ef474fde1990fe74f32ba09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
