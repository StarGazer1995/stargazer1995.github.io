---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ABS36IS%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T065957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCICruTvxXQxw9Lb4%2BVOJXsg6%2Bf%2B%2BXkwomEji9znQk5WK6AiBpoq469UjR8GECTW3KOIASrHgS%2BBL%2F8wvkJ1dJuYJIJCqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi4B2gFb34nkog%2B0LKtwD%2F7f%2FK8%2BeNeRqsYwIOZUwWjW4G4m3XjJFO5V1XKulFuOI3qLX4wgdL%2BH18Y5uHH9ZgbIo%2BjFSOp9mYDt6v22N%2F%2F9apHGMbjrapCKlr2lcocqMJdFGp7cBDAqQWr0UGbs5NdbaAwcyLSnjkRtJ%2Fg8E3uqCwBG2qgNzHW4AHkrMPOsz1kWBNe0GWCc%2FheI4brc04jiPfobdf%2BEK5iNOEEf%2FE%2FcdxavZEF8szkwycLszlUnAB5F3TMSwvCu7bruJUc0KrB9U4zgFz%2F4CMZYstKDwFluxkXlIl2dK%2FX3uWXrbqeDkedMdzWckKGHymsAGptBGZDZRu1zKsDs5qTrIu9pCjHco1%2Fw%2B8RF0pQIQ%2Fi8%2Fr7ygSHeusQmoTCtuVA1FZlntfeCLyP0y1YQZBmsoSK5o4InW1wsazVTRHnkOUx0itgGbrJVq3NANOJhfHEixmjrl0nvWaS2ZiHGngnzYOnkaevjG3metMz4t9LGnv8nOINR707zG3kma14U%2FF5M3rS5aTaSeQAx0VBBG%2ByqdbWGTM8e0CwyViP7rmlPDt3PLMHrWWzHD8UDgV4kS1NMYRI8rm7fr6BMDgN8044irnR1U%2BQw3CZvzA0PBiqFbKzMDOGM6PEmOUxwW10gKHRMw5fOX0gY6pgGKuqZr%2B%2BP3DfjvXRQhKIOaJVXmg3EwTUzOf4D%2F81e7P15vygXdhOo7nQ0kH8PgqhAijMg4XIOhYdtKKTJbqQ%2FDFcoi8qPME20aJmErjSEdYBtBkt8CzZMSFIttWNW6ikVbjwykkyFPRrKowDrXhZAfy1TEcnoL924TVfd5GAPEVRLF%2BwpMxOBEvxOH6k%2FXC9E%2FRpaa9X6aMD%2BL4aUVT5X1%2FykuLi95&X-Amz-Signature=4861e6241303faa0b99e22711eb21e438afe7503bd77c9ce50ec1aed271c436e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
