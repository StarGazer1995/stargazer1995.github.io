---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DU7VOYL%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T173925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCK8dK4sZmmtHZVxIzZiXYi29efOtPgcveVwz40xKEvdwIhAJCi3xeJd0gNMH7LOwu2IBSVVcVYP%2Fabs3fvdPrE2oOBKv8DCFoQABoMNjM3NDIzMTgzODA1IgxDozZKsDuPqd87GOEq3AN3YEvNH3DJnn%2FnNuElZfm4hpTQoH1nlLJOGIM%2FYhHtIFXbUzinD32kCVNaXFP0uaKTNzXNh8jojMla3IUclEaZ40blAHzv%2BUs0fRr5U0gnKmjBAoxNZtOoc7RwGlWmIKTtWUVQkceP%2BT3KMA9pBOgZP58%2BZsOPcLU%2BFitlE%2FT7CkG9jXhHeznflzlQW80HpFiOzBeizoj9ZYrGmX2Tw6VkvB4vJsTjbf9yu36guziAN5Xbn97KPOqya%2F7CRYSYw%2BRfJg6OEvH738LpmVWnAxKmyrgRMMb9x1A2fbpoikZT%2FGJjKdfOA%2FxbLZIypYrlrBsy9%2BRZZbq5RyfNpEvawmJ4NX8KikZJMEbwHxlDmdUmfqAj1fsXIBHv%2BSx4adrYIyVOyu80cTOvwrGiIQ9LIHaZaVEc9KUwbJ%2BLd7SWmmqRpQKn7BsymdYKj15b7KlZX4GAf%2BubT2YntzCMggSPUn92kbRfzucRH1th%2FocB5fIF0ME1Aeg7v420BNppP9vLGQJ%2FO1VSnxR6InRl7wrZKF8bFzg90XhERABsJG%2FZNF%2FfVAGeUp0FebDxHeJ%2BSGHK1S4q%2Fght2KF1Rzs46cLqmRMAFZzFg2hpuy2LAjPDDW8mGf%2BkHLouB3ZnRwnx3jDhgIHVBjqkAQ8T9McWGNtDP8JeFnDXgJyuHymbWJtUCc9e8DNvQJEkExoeFD18oaai%2FUmx68MjJavVNpJDh8NALgJAMxrfIAcXSN1t0esKA3etc1xHe3xy6QFD4lx8xmX8ERIqdLw%2BYbzXMe3OgUX%2FnPGzWK%2BTW0ju%2FnTh33aGetXzoj2DJNWq43Z7cr0zvaBu0zbUxs%2BmmwLz1DqFysNNaFmpZFMYfhmUw%2B6x&X-Amz-Signature=76ccdff29eedce63abe1ff8b3175655e4df45b94264bb28909353fe112d5ffb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
