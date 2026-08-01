---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2BU2CRH%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T095558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEN7N1AZAm9Y5UyMq0zcZKrml%2BjFVSwXR9GJ3wSi9ocfAiAvcltg%2BLd%2BsXfMY1sX%2BI2BOtuGvLy2JWEcY07xINBkQiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPmp0Qrprg5EhOOIKtwDtVS6FyUczD72dHfWALoUEeYW%2FeKfS2GYsBjW7Gd6CFivvrY4ADEN%2BnA9S65F4dbLxQpvouWg01Bx7TtAi7LQZaAl048K7CiLomAaJxsbBziUrvupQxrbJ7k%2BgO%2BLIG2FRdPo4vpNbmYwpI1oQSazpBMCntaamuZoLjbYCOVp23DzIvBod%2F9KER%2FrJsIKH1uYusDIjO2lkoKQW1xWwWunTVgGPvfSx5eEck0ONXG15AOCfAkWtg%2BhvbumCeuzlQV2Sx4ndar5xxSrpm8scr5mWjJZfyV5bYtqeXVW01lmuTXi%2BKvXyQEkzJwelisNdRcrmEs8ejyrOIqi9ppRHdGg5uAJRr0owuUWVBihd8996CXRjgS2oYoP2i8iSHeEvO6iIWA7mOpzMJ%2F4LoURIMQ9LSzwHnNK1VoplcPimgzAcylddLWfTFmrCsVpbcTQ5UfwhXzlVMLMXvtPf6NKnOVIarZ6KKMjoGpudOrnQ0xaIdmmFx9zO7jIJ%2FvljPPIRBw2LpTAgkY1xYdej0YlFegzNWGj55V3TevnNh9R3PIOkH9nFkpM1pkrUniMUFkb6LBYBHr4hqVL1LOodnvMR5px%2FGpgkvqRBKv1U0prgfNuCDiFhHPLk7BbTcguZ0Mw%2Bfi20wY6pgHcAeBk8HL2ku1yd3k5SQbjvzIZ%2BJhTHOnabt2JmdijVOhrg4vqosEjHOa8Y1d4lu4KPtVMvaONP8LbfRVqs54T31ElsKDAESoPIH6aUCYqcgTylnxim%2B3ZtWyKJ2rlVhRvTBlMvuUwbhQxhdXTKzSRZYMU44ksPaXN28XHNuc6sYTqe4hlGLMTMExtnakrcW9R17WzDVyKUcNKD7Q150F%2BZy7TizKs&X-Amz-Signature=8fc9a7bd5adda089fc6bbc2dbed5a70de2df11769def56827c5e1eeb972317a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
